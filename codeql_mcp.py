import time
import re
import os
import json
import subprocess
import threading
import uuid
from pathlib import Path
from utils.db_lock import remove_db_lock
from utils.log import logger
CODEQL_PATH = "/home/haojie/test/codeql/codeql"

class CodeQLQueryServer:
    def __init__(self, codeql_path=CODEQL_PATH):
        self.registered_dbs = set()
        self.codeql_path = codeql_path
        self.proc = None
        self.reader_thread = None
        self.pending = {}
        self.running = True
        self.id_counter = 1
        self.progress_id = 0
        self.progress_callbacks = {}

    def start(self):
        self.proc = subprocess.Popen(
            [
                self.codeql_path,
                "execute",
                "query-server2",
                "--debug",
                "--tuple-counting",
                "--threads=0",
                "--evaluator-log-level",
                "5",
                "-v",
                "--log-to-stderr",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,  # line-buffered
        )
        self.reader_thread = threading.Thread(
            target=self._read_loop, daemon=True
        )
        self.reader_thread.start()
        self.stderr_thread = threading.Thread(
            target=self._stderr_loop, daemon=True
        )
        self.stderr_thread.start()

    def _stderr_loop(self):
        while self.running:
            line = self.proc.stderr.readline()
            # For debugging
            if line:
                try:
                    logger.info(f"[CodeQL stderr] {line.strip()}")
                except ValueError:
                    # Handle the case where stderr is closed
                    break

    def _read_loop(self):
        logger.info("[*] Read loop started")
        while self.running:
            line = self.proc.stdout.readline()
            if not line:
                logger.info("[*] Read loop: EOF or closed stdout")
                break
            logger.info(f"[stdout] {line.strip()}")
            if line.startswith("Content-Length:"):
                try:
                    length = int(line.strip().split(":")[1])
                    blank = self.proc.stdout.readline()
                    content = self.proc.stdout.read(length)
                    logger.info(f"[raw response body] {content.strip()}")
                    message = json.loads(content)
                    self._handle_message(message)
                except Exception as e:
                    logger.info(f"[!] Failed to parse message: {e}")

    def _handle_message(self, message):
        logger.info(f"\n[←] Received response:\n{json.dumps(message, indent=2)}\n")

        if message.get("method") == "ql/progressUpdated":
            params = message.get("params", {})
            progress_id = params.get("id")
            callback = self.progress_callbacks.get(progress_id)
            if callback:
                callback(params)
            else:
                logger.info(
                    f"[ql-progress:{progress_id}] step={params.get('step')} / {params.get('maxStep')}"
                )
            return

        if "method" in message and message["method"] == "evaluation/progress":
            progress_id = message["params"].get("progressId")
            msg = message["params"].get("message")
            callback = self.progress_callbacks.get(progress_id)
            if callback:
                callback(msg)
            else:
                logger.info(f"[progress:{progress_id}] {msg}")
            return

        if "id" in message and "result" in message:
            request_id = message["id"]
            if request_id in self.pending:
                callback, progress_id = self.pending[request_id]
                callback(message["result"])
                del self.pending[request_id]
                if progress_id in self.progress_callbacks:
                    del self.progress_callbacks[progress_id]
        elif "id" in message and "error" in message:
            logger.info(
                f"[!] Error response to request {message['id']}:\n{json.dumps(message['error'], indent=2)}"
            )

    def _send(self, payload):
        if not self.proc or not self.proc.stdin:
            logger.info("[!] Tried to send but process not running.")
            return

        data = json.dumps(payload)
        content = f"Content-Length: {len(data)}\r\n\r\n{data}"
        logger.info(f"\n[→] Sending request:\n{json.dumps(payload, indent=2)}\n")
        self.proc.stdin.write(content)
        self.proc.stdin.flush()

    def send_request(self, method, params, callback, progress_callback=None):
        req_id = self.id_counter
        self.id_counter += 1

        if isinstance(params, dict) and "progressId" in params:
            self.progress_callbacks[params["progressId"]] = progress_callback

        payload = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params,
        }

        self.pending[req_id] = (
            callback,
            params.get("progressId") if isinstance(params, dict) else None,
        )
        self._send(payload)

    def stop(self):
        self.running = False
        if self.proc:
            self.proc.terminate()

    def find_class_identifier_position(self, filepath, class_name):
        """
        Find the 1-based position of the class name identifier in a QL file.
        Returns: (start_line, start_col, end_line, end_col)
        """
        path = Path(filepath)
        lines = path.read_text().splitlines()

        for i, line in enumerate(lines):
            match = re.search(rf"\bclass\s+{re.escape(class_name)}\b", line)
            if match:
                start_line = i + 1
                start_col = (
                    match.start(0) + line[match.start(0) :].find(class_name) + 1
                )
                end_col = start_col + len(class_name)
                return start_line, start_col, start_line, end_col

        raise ValueError(
            f"Class name '{class_name}' not found in file: {filepath}"
        )

    def find_predicate_identifier_position(self, filepath, predicate_name):
        """
        Find the 1-based position of a predicate name in a QL file.
        Supports: predicate name(...), name(...) (inside class), etc.
        Returns: (start_line, start_col, end_line, end_col)
        """
        path = Path(filepath)
        lines = path.read_text().splitlines()

        for i, line in enumerate(lines):
            match = re.search(rf"\b{re.escape(predicate_name)}\s*\(", line)
            if match:
                start_line = i + 1
                start_col = match.start() + 1
                end_col = start_col + len(predicate_name)
                return start_line, start_col, start_line, end_col

        raise ValueError(
            f"Predicate name '{predicate_name}' not found in file: {filepath}"
        )

    def register_databases(
        self, db_paths, callback=None, progress_callback=None
    ):
        resolved = [str(Path(p).resolve()) for p in db_paths]
        
        # 修复：遍历每个数据库路径，而不是整个列表
        new_dbs = []
        for db_path in resolved:
            if db_path not in self.registered_dbs:
                self.registered_dbs.add(db_path)  # 使用add而不是append
                new_dbs.append(db_path)
            else:
                logger.info(f"[!] Database {db_path} already registered.")
        # 修复：在每个数据库路径上调用remove_db_lock
        for db_path in new_dbs:
            remove_db_lock(db_path)
        # 如果没有新的数据库需要注册，直接返回
        if len(new_dbs) == 0:
            logger.info("[INFO] No new databases to register.")
            # return
        
        progress_id = self.progress_id
        self.progress_id += 1

        params = {"body": {"databases": new_dbs}, "progressId": progress_id}

        logger.info(
            f"[DEBUG] Sending evaluation/registerDatabases with progressId={progress_id}"
        )
        self.send_request(
            "evaluation/registerDatabases",
            params,
            callback or (lambda r: logger.info("[registerDatabases] done:", r)),
            progress_callback=progress_callback,
        )

    def deregister_databases(
        self, db_paths, callback=None, progress_callback=None
    ):
        resolved = [str(Path(p).resolve()) for p in db_paths]
        
        # 修复：遍历每个数据库路径，而不是整个列表
        removed_dbs = []
        for db_path in resolved:
            if db_path in self.registered_dbs:
                self.registered_dbs.discard(db_path)  # 使用discard而不是remove
                removed_dbs.append(db_path)
            else:
                logger.info(f"[!] Database {db_path} not registered.")
        
        # 如果没有数据库需要注销，直接返回
        if not removed_dbs:
            return
            
        progress_id = self.progress_id
        self.progress_id += 1

        params = {"body": {"databases": removed_dbs}, "progressId": progress_id}

        logger.info(
            f"[DEBUG] Sending evaluation/deregisterDatabases with progressId={progress_id}"
        )
        self.send_request(
            "evaluation/deregisterDatabases",
            params,
            callback or (lambda r: logger.info(f"[deregisterDatabases] done: {r}")),
            progress_callback=progress_callback,
        )

    def evaluate_queries(
        self,
        query_path,
        db_path,
        output_path,
        callback=None,
        progress_callback=None,
    ):
        db = str(Path(db_path).resolve())
        query_path = str(Path(query_path).resolve())
        output_path = str(Path(output_path).resolve())

        progress_id = self.progress_id
        self.progress_id += 1

        params = {
            "body": {
                "db": db,
                "queryPath": query_path,
                "outputPath": output_path,
                "target": {"query": {}},
                "additionalPacks": [""],
                "externalInputs": {},
                "singletonExternalInputs": {},
            },
            "progressId": progress_id,
        }

        def on_done(result):
            logger.info(f"[evaluateQueries] done: {result}")
            if result.get("resultType") != 0:
                raise RuntimeError(
                    f"CodeQL evaluation failed: {result.get('message', 'Unknown error')}"
                )

        logger.info(
            f"[DEBUG] Sending evaluation/runQuery with progressId={progress_id}"
        )

        self.send_request(
            "evaluation/runQuery",
            params,
            callback or on_done,
            progress_callback=progress_callback,
        )

    def evaluate_and_wait(self, query_path, db_path, output_path):
        progress_id = self.progress_id
        progress_cb, done = self.wait_for_progress_done(progress_id)
        self.evaluate_queries(
            query_path, db_path, output_path, progress_callback=progress_cb
        )
        done.wait()
        logger.info("[evaluate_and_wait] Query completed.")

    def quick_evaluate_and_wait(
        self,
        query_path,
        db_path,
        output_path,
        start_line,
        start_col,
        end_line,
        end_col,
    ):
        progress_id = self.progress_id
        progress_cb, done = self.wait_for_progress_done(progress_id)
        self.quick_evaluate(
            query_path,
            db_path,
            output_path,
            start_line,
            start_col,
            end_line,
            end_col,
            progress_callback=progress_cb,
        )
        done.wait()
        logger.info("[evaluate_and_wait] Query completed.")

    def quick_evaluate(
        self,
        file_path,
        db_path,
        output_path,
        start_line,
        start_col,
        end_line,
        end_col,
        callback=None,
        progress_callback=None,
    ):
        progress_id = self.progress_id
        self.progress_id += 1

        params = {
            "body": {
                "db": str(Path(db_path).resolve()),
                "queryPath": str(Path(file_path).resolve()),
                "outputPath": str(Path(output_path).resolve()),
                "target": {
                    "quickEval": {
                        "quickEvalPos": {
                            "fileName": str(Path(file_path).resolve()),
                            "line": start_line,
                            "column": start_col,
                            "endLine": end_line,
                            "endColumn": end_col,
                        }
                    }
                },
                "additionalPacks": [],
                "externalInputs": {},
                "singletonExternalInputs": {},
            },
            "progressId": progress_id,
        }

        def on_done(result):
            logger.info(f"[quickEvaluate] done: {result}")
            if result.get("resultType") != 0:
                raise RuntimeError(
                    f"CodeQL evaluation failed: {result.get('message', 'Unknown error')}"
                )

        logger.info(
            f"[DEBUG] Sending evaluation/evaluateQueries (quickEval) with progressId={progress_id}"
        )
        self.send_request(
            "evaluation/runQuery",
            params,
            callback or on_done,
            progress_callback=progress_callback,
        )

    def decode_bqrs(self, bqrs_path, output_format="json"):
        bqrs_path = str(Path(bqrs_path).resolve())

        if not os.path.exists(bqrs_path):
            raise FileNotFoundError(f"BQRS file not found: {bqrs_path}")

        result = subprocess.run(
            [
                self.codeql_path,
                "bqrs",
                "decode",
                "--format",
                output_format,
                bqrs_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"Failed to decode BQRS: {result.stderr.strip()}"
            )

        return result.stdout

    def wait_for_progress_done(self, expected_progress_id):
        event = threading.Event()

        def progress_callback(message):
            if (
                isinstance(message, dict)
                and message.get("id") == expected_progress_id
                and message.get("step") == message.get("maxStep")
            ):
                event.set()

        return progress_callback, event

    def wait_for_completion_callback(self):
        done = threading.Event()
        result_holder = {}

        def callback(result):
            result_holder["result"] = result
            done.set()

        return callback, done, result_holder