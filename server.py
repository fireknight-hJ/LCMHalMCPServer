#!/usr/bin/env python3
from fastmcp import FastMCP, Context
from codeql_mcp import CodeQLQueryServer
from pathlib import Path
from utils import db_file, db_cache
import uuid
import shutil
import os
import fastmcp

mcp = FastMCP("LCMHalMCP", version="1.0.0")
qs = CodeQLQueryServer()
qs.start()


@mcp.tool()
async def register_database(db_path: str) -> str:
    """This tool registers a CodeQL database given a path"""
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}"

    db_entry = {
        "uri": Path(db_path).resolve().as_uri(),
        "content": {
            "sourceArchiveZip": (Path(db_path) / "src.zip").resolve().as_uri(),
            "dbDir": Path(db_path).resolve().as_uri(),
        },
    }
    callback, done, result_holder = qs.wait_for_completion_callback()
    qs.register_databases(
        [db_path],
        callback=callback,
        progress_callback=lambda msg: print("[progress] register:", msg),
    )
    done.wait()
    return f"Database registered: {db_path}"


@mcp.tool()
async def quick_evaluate(
    file: str, db: str, symbol: str, output_path: str = "/tmp/quickeval.bqrs"
) -> str:
    """This will allow you to quick_evaluate either a class or a predicate in a codeql query"""
    try:
        start, scol, end, ecol = qs.find_class_identifier_position(file, symbol)
    except ValueError:
        start, scol, end, ecol = qs.find_predicate_identifier_position(
            file, symbol
        )
    try:
        qs.quick_evaluate_and_wait(
            file, db, output_path, start, scol, end, ecol
        )
    except RuntimeError as re:
        return f"CodeQL evaluation failed: {re}"
    return output_path


@mcp.tool()
async def decode_bqrs(bqrs_path: str, fmt: str) -> str:
    """This can be used to decode CodeQL results, format is either csv for problem queries or json for path-problems"""
    return qs.decode_bqrs(bqrs_path, fmt)


@mcp.tool()
async def evaluate_query(
    query_path: str, db_path: str, output_path: str = "/tmp/eval.bqrs"
) -> str:
    """Runs a CodeQL query on a given database"""
    try:
        qs.evaluate_and_wait(query_path, db_path, output_path)
    except RuntimeError as re:
        return f"CodeQL evaluation failed: {re}"
    return output_path


@mcp.tool()
async def find_class_position(file: str, name: str) -> dict:
    """Finds startline, startcol, endline endcol of a class for quickeval"""
    start, scol, end, ecol = qs.find_class_identifier_position(file, name)
    return {
        "start_line": start,
        "start_col": scol,
        "end_line": end,
        "end_col": ecol,
    }


@mcp.tool()
async def find_predicate_position(file: str, name: str) -> dict:
    """Finds startline, startcol, endline endcol of a predicate for quickeval"""
    start, scol, end, ecol = qs.find_predicate_identifier_position(file, name)
    return {
        "start_line": start,
        "start_col": scol,
        "end_line": end,
        "end_col": ecol,
    }

@mcp.tool()
async def driver_info_driverfromfunction_collector(db_path: str) -> str:
    """Collect driverfrom function query on a given database, returns JSON results"""
    # 从当前目录的codeql_scripts文件夹中获取对应ql文件
    query_path = str(Path(__file__) / "codeql_scripts" / "driver_info_driverfromfunction_collector.ql")
    # 输出目录在db_path同目录新建新建tmp文件夹中 eg: /home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer -> +lcmhal_tmp
    output_path = str(Path(db_path) / "lcmhal_tmp" / str("driver_info_driverfromfunction_collector" + ".bqrs"))
    # 从db_path中提取数据库名称
    # db_path = db_path.split("/")[-1]
    if not Path(db_path, "lcmhal_tmp").exists():
        Path(db_path, "lcmhal_tmp").mkdir(parents=True, exist_ok=True)
    if not Path(output_path).exists():
        try:
            qs.evaluate_and_wait(query_path, db_path, output_path)
        except RuntimeError as re:
            return f"CodeQL evaluation failed: {re}"
    return qs.decode_bqrs(output_path, output_format="json")

    # # 从当前目录的codeql_scripts文件夹中获取对应ql文件
    # query_path = str(Path(__file__) / "codeql_scripts" / "driver_info_driverfromfunction_collector.ql")
    # output_path = str(Path(__file__) / "tmp" / "driver_info_driverfromfunction_collector" + str(uuid.uuid4()) + ".bqrs")
    # # 从db_path中提取数据库名称
    # db_path = db_path.split("/")[-1]
    # try:
    #     qs.evaluate_and_wait(query_path, db_path, output_path)
    # except RuntimeError as re:
    #     return f"CodeQL evaluation failed: {re}"
    # return qs.decode_bqrs(output_path, output_format="json")

@mcp.tool()
async def get_file_content(db_path: str, file_path: str) -> str:
    """Reads and returns the content of a specified file in a CodeQL database."""
    return db_file.read_file_from_db_zip(db_path, file_path)

@mcp.tool()
async def clear_cache(db_path: str, query_infos: list = []) -> str:
    """clear lcmhalmcp tmp cache, used when db is updated"""
    db_cache.clear_cache(db_path, query_infos)
    return "Cache cleared"

# @mcp.tool()
# async def get_struct_content_from_startline(file_path: str, start_line: int) -> str:
    

if __name__ == "__main__":
    print("Starting CodeQL MCP server...")
    mcp.run()