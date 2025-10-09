from fastmcp import FastMCP, Context
from codeql_mcp import CodeQLQueryServer
from pathlib import Path



mcp = FastMCP("LCMHalMCP", version="1.0.0")

@mcp.tool()
async def register_and_analyze_database(db_path: str) -> str:
    """This tool registers a CodeQL database, and analyze it given a path"""
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

