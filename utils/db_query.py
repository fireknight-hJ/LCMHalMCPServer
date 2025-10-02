
import subprocess
import json
from config.collector_infos import *

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

    output_path = "/tmp/eval.bqrs"
    try:
        qs.evaluate_and_wait(query_path, db_path, output_path)
    except RuntimeError as re:
        return f"CodeQL evaluation failed: {re}"
    return qs.decode_bqrs(output_path, "json")

def run_query_and_return_json_server(db_path: str, query_path: str, output_path: str = "/tmp/eval.bqrs") -> str:
    """Runs a CodeQL query on a given database and returns JSON result."""
    # result = evaluate_query(query_path, db_path, output_path)
    # if "CodeQL evaluation failed" in result:
    #     return result
    # return decode_bqrs(result, "json")
    return ""

def run_query_and_return_json(db_path: str, query_path: str, output_path: str = "/tmp/eval.bqrs") -> str:
    """Runs a CodeQL query on a given database and returns JSON result."""
    run_query_and_return_json_directly(db_path, query_path)
