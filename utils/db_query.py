
import subprocess
import json
from config.collector_infos import *
from codeql_mcp import CodeQLQueryServer
import uuid

qs = CodeQLQueryServer()
qs.start()

def run_query_and_return_json_directly(db_path: str, query_path: str) -> str:
    """Runs a CodeQL query on a given database and returns JSON result. directly run the query and decode the result."""
    try:
        subprocess.run([
            "codeql", "query", "run", query_path,
            "--database", db_path,
            "--output", output_bqrs,
        ], check=True, capture_output=True)
        
        subprocess.run([
            "codeql", "bqrs", "decode", output_bqrs,
            "--output", output_json,
            "--format", "json"
        ], check=True, capture_output=True)
        
        with open(output_json, "r", encoding="utf-8") as fp:
            result = json.load(fp)
            return result["#select"]["tuples"]
            
    except Exception as e:
        print(f"[ERROR] 运行查询失败: {e}")
        return None

def run_query_and_return_json_server(db_path: str, query_path: str) -> str:
    """Runs a CodeQL query on a given database and returns JSON result."""
    output_path = "/tmp/" + str(uuid.uuid4()) + ".bqrs"
    # register the db
    callback, done, result_holder = qs.wait_for_completion_callback()
    qs.register_databases(
        [db_path],
        callback=callback,
        progress_callback=lambda msg: print("[progress] register:", msg),
    )
    done.wait()

    # create the tmp file
    with open(output_path, "w") as fp:
        pass
    try:
        qs.evaluate_and_wait(query_path, db_path, output_path)
        print(f"[INFO] 输出路径: {output_path}")
    except RuntimeError as re:
        return f"CodeQL evaluation failed: {re}"
    # decode the bqrs file and return json
    return qs.decode_bqrs(output_path, "json")
    # result = evaluate_query(query_path, db_path, output_path)
    # if "CodeQL evaluation failed" in result:
    #     return result
    # return decode_bqrs(result, "json")
    # return ""

def run_query_and_return_json(db_path: str, query_path: str, output_path: str = "/tmp/eval.bqrs") -> str:
    """Runs a CodeQL query on a given database and returns JSON result."""
    # run_query_and_return_json_directly(db_path, query_path)
    return run_query_and_return_json_server(db_path, query_path)

if __name__ == "__main__":
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    query_path = "/home/haojie/workspace/lcmhalmcp/queries/collectors/driver/driver_info_driverfromexpr_collector.ql"
    result = run_query_and_return_json_server(db_path, query_path)
    print(result)