from fastmcp import FastMCP
from pathlib import Path
import argparse
import config.globs as globs
import sys

# 导入collector核心模块
from tools.collector.core import (
    register_db, get_files_in_db_zip, get_tree_in_db_zip,
    get_mmio_func_list, get_mmio_files, get_mmio_func_info,
    get_function_info, get_struct_or_enum_info, get_func_call_stack,
    get_driver_info, validate_database
)

mcp = FastMCP("LCMHalMCP", version="1.0.0", port=8112)

@mcp.tool()
async def list_files_in_db_zip() -> str:
    """Lists all files of the srcfile in project inside database directory."""
    try:
        files = get_files_in_db_zip(globs.db_path)
        return f"Files in src.zip: {files}"
    except Exception as e:
        return f"Error listing files in src.zip: {e}"

@mcp.tool()
async def list_tree_in_db_zip() -> str:
    """Lists all files of the srcfile in project inside database directory."""
    try:
        tree = get_tree_in_db_zip(globs.db_path)
        return f"Tree in src.zip: {tree}"
    except Exception as e:
        return f"Error listing tree in src.zip: {e}"

@mcp.tool()
async def register_and_analyze_database() -> str:
    """This tool registers a CodeQL database and analyzes it"""
    if not globs.db_path:
        return "Database path not set. Please provide db_path via command line argument."
    
    # 验证数据库
    validation = validate_database(globs.db_path)
    if not validation["valid"]:
        return validation["error"]
    
    # 注册数据库
    try:
        success = register_db(globs.db_path)
        if success:
            return f"Database registered and analyzed: {globs.db_path}"
        else:
            return f"Failed to register database: {globs.db_path}"
    except Exception as e:
        return f"Failed to initialize codebase info: {e}"

# mmio相关工具
@mcp.tool()
async def collect_mmio_func_list() -> str:
    """This tool collects the mmio function list from the registered database"""
    try:
        func_list = get_mmio_func_list(globs.db_path)
        return f"MMIO function list: {func_list}"
    except Exception as e:
        return f"Error collecting MMIO function list: {e}"

@mcp.tool()
async def collect_mmio_files() -> str:
    """This tool collects the mmio files from the registered database"""
    try:
        mmio_files = get_mmio_files(globs.db_path)
        return f"MMIO files: {mmio_files}"
    except Exception as e:
        return f"Error collecting MMIO files: {e}"

@mcp.tool()
async def collect_mmio_func_info(func_name: str) -> str:
    """This tool collects the mmio infos and function info from the registered database given a mmio function name"""
    try:
        result = get_mmio_func_info(globs.db_path, func_name)
        if "error" in result:
            return result["error"]
        return f"MMIO Exprs info: {result['mmio_exprs_info']}\nFunction info: {result['function_info']}"
    except Exception as e:
        return f"Error collecting MMIO function info: {e}"

# common相关工具
@mcp.tool()
async def collect_function_info(func_name: str) -> str:
    """This tool collects the function info from the registered database given a function name"""
    try:
        func_info = get_function_info(globs.db_path, func_name)
        if not func_info:
            return f"Function not found: {func_name}"
        return f"Function info: {func_info}"
    except Exception as e:
        return f"Error collecting function info: {e}"

@mcp.tool()
async def collect_struct_or_enum_info(struct_name: str) -> str:
    """This tool collects the struct or enum info from the registered database"""
    try:
        result = get_struct_or_enum_info(globs.db_path, struct_name)
        if "error" in result:
            return result["error"]
        
        if result["type"] == "struct":
            return f"Struct info: {result['info']}"
        else:
            return f"Enum info: {result['info']}"
    except Exception as e:
        return f"Error collecting struct or enum info: {e}"

@mcp.tool()
async def collect_func_call_stack(func_name: str) -> str:
    """This tool collects the function call stack given a function name"""
    try:
        result = get_func_call_stack(globs.db_path, func_name)
        if "error" in result:
            return result["error"]
        return f"Function call to info: {result['call_to_info']}\nFunction call from info: {result['call_from_info']}"
    except Exception as e:
        return f"Error collecting function call stack: {e}"

# driver相关工具
@mcp.tool()
async def collect_driver_info(driver_name: str) -> str:
    """This tool collects the driver info from the registered database given a driver name"""
    try:
        driver_info = get_driver_info(globs.db_path, driver_name)
        if not driver_info:
            return f"Driver not found: {driver_name}"
        return f"Driver info: {driver_info}"
    except Exception as e:
        return f"Error collecting driver info: {e}"

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="LCMHalMCP Server")
    parser.add_argument("--db-path", type=str, required=True, help="Path to the CodeQL database")
    parser.add_argument("--transport", type=str, default="streamable-http", 
                       choices=["streamable-http", "sse", "stdio"],
                       help="Transport method (default: streamable-http)")
    return parser.parse_args()

if __name__ == "__main__":
    # 解析命令行参数
    args = parse_args()
    globs.db_path = args.db_path
    transport = args.transport
    
    # 验证数据库路径
    db_path_resolved = Path(globs.db_path).resolve()
    if not db_path_resolved.exists():
        print(f"Error: Database path does not exist: {globs.db_path}")
        sys.exit(1)
    
    # 初始化全局codebase_infos
    try:
        success = register_db(globs.db_path)
        if not success:
            print(f"Error initializing codebase info for: {globs.db_path}")
            sys.exit(1)
    except Exception as e:
        print(f"Error initializing codebase info: {e}")
        sys.exit(1)
    
    # 启动MCP服务器
    mcp.run(transport=transport)