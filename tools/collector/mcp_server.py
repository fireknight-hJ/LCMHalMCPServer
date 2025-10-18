from fastmcp import FastMCP, Context
from pathlib import Path
from tools.collector.common import *
from tools.collector.driver import *
from tools.collector.mmio import *
import argparse
import sys

mcp = FastMCP("LCMHalMCP", version="1.0.0", port=8112)

# 全局变量存储命令行参数中的db_path
GLOBAL_DB_PATH = ""

# 存储全部三类代码信息
class CodebaseInfos:
    def __init__(self, db_path: str = ""):
        self.db_path = db_path
        if not db_path:
            return
        self.common_infos = create_commoncodebase_info(db_path, force_refresh=False)
        self.driver_infos = create_drivercodebase_info(db_path, force_refresh=False)
        self.mmio_infos = create_mmiocodebase_info(db_path, force_refresh=False)

# 全局codebase_infos_dict只留一份
codebase_infos_dict: Dict[str, CodebaseInfos] = {}

def get_global_codebase_infos() -> CodebaseInfos:
    """获取全局的codebase_infos实例"""
    global GLOBAL_DB_PATH, codebase_infos_dict
    if not GLOBAL_DB_PATH:
        raise ValueError("Database path not set. Please provide db_path via command line argument.")
    
    if GLOBAL_DB_PATH not in codebase_infos_dict:
        codebase_infos_dict[GLOBAL_DB_PATH] = CodebaseInfos(GLOBAL_DB_PATH)
    
    return codebase_infos_dict[GLOBAL_DB_PATH]

@mcp.tool()
async def list_files_in_db_zip() -> str:
    """Lists all files of the srcfile in project inside database directory."""
    try:
        files = list_files_in_db_zip(GLOBAL_DB_PATH)
        return f"Files in src.zip: {files}"
    except Exception as e:
        return f"Error listing files in src.zip: {e}"

@mcp.tool()
async def list_tree_in_db_zip() -> str:
    """Lists all files of the srcfile in project inside database directory."""
    try:
        tree = list_tree_in_db_zip(GLOBAL_DB_PATH)
        return f"Tree in src.zip: {tree}"
    except Exception as e:
        return f"Error listing tree in src.zip: {e}"

@mcp.tool()
async def register_and_analyze_database() -> str:
    """This tool registers a CodeQL database and analyzes it"""
    global GLOBAL_DB_PATH
    if not GLOBAL_DB_PATH:
        return "Database path not set. Please provide db_path via command line argument."
    
    db_path_resolved = Path(GLOBAL_DB_PATH).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {GLOBAL_DB_PATH}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {GLOBAL_DB_PATH}"
    
    # 初始化代码信息
    try:
        codebase_infos_dict[GLOBAL_DB_PATH] = CodebaseInfos(GLOBAL_DB_PATH)
    except Exception as e:
        return f"Failed to initialize codebase info: {e}"
    
    return f"Database registered and analyzed: {GLOBAL_DB_PATH}"

# mmio
@mcp.tool()
async def collect_mmio_func_list() -> str:
    """This tool collects the mmio function list from the registered database"""
    try:
        codebase_infos = get_global_codebase_infos()
        func_list = list(codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.keys())
        return f"MMIO function list: {func_list}"
    except Exception as e:
        return f"Error collecting MMIO function list: {e}"

@mcp.tool()
async def collect_mmio_files() -> str:
    """This tool collects the mmio files from the registered database"""
    try:
        codebase_infos = get_global_codebase_infos()
        mmio_files = set()
        for mmio_info in codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.values():
            if isinstance(mmio_info, list):
                for info in mmio_info:
                    mmio_files.add(info.file_path)
            else:
                mmio_files.add(mmio_info.file_path)
        mmio_files = list(mmio_files)
        return f"MMIO files: {mmio_files}"
    except Exception as e:
        return f"Error collecting MMIO files: {e}"

@mcp.tool()
async def collect_mmio_func_info(func_name: str) -> str:
    """This tool collects the mmio infos and function info from the registered database given a mmio function name"""
    try:
        codebase_infos = get_global_codebase_infos()
        mmio_func_info = codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.get(func_name)
        common_func_info = codebase_infos.common_infos.functions.get(func_name)
        if not mmio_func_info or not common_func_info:
            return f"MMIO function not found: {func_name}"
        return f"Function info: {common_func_info}\nMMIO Exprs info: {mmio_func_info}"
    except Exception as e:
        return f"Error collecting MMIO function info: {e}"

# common
@mcp.tool()
async def collect_function_info(func_name: str) -> str:
    """This tool collects the function info from the registered database given a function name"""
    try:
        codebase_infos = get_global_codebase_infos()
        func_info = codebase_infos.common_infos.functions.get(func_name)
        if not func_info:
            return f"Function not found: {func_name}"
        return f"Function info: {func_info}"
    except Exception as e:
        return f"Error collecting function info: {e}"

@mcp.tool()
async def collect_struct_or_enum_info(struct_name: str) -> str:
    """This tool collects the struct or enum info from the registered database"""
    try:
        codebase_infos = get_global_codebase_infos()
        struct_info = codebase_infos.common_infos.structs.get(struct_name)
        if not struct_info:
            struct_info = codebase_infos.common_infos.enums.get(struct_name)
            if not struct_info:
                return f"Struct or enum not found: {struct_name}"
            return f"Enum info: {struct_info}"
        return f"Struct info: {struct_info}"
    except Exception as e:
        return f"Error collecting struct or enum info: {e}"

def resolve_call_stack(call_to_dict: Dict[str, List[FunctionCallInfo]], call_from_dict: Dict[str, List[FunctionCallInfo]], func_name: str, layer_cnt: int) -> tuple:
    """递归解析函数调用栈"""
    if layer_cnt <= 0:
        return [], []
    call_to_info = call_to_dict.get(func_name, [])
    call_from_info = call_from_dict.get(func_name, [])
    return call_to_info, call_from_info

@mcp.tool()
async def collect_func_call_stack(func_name: str) -> str:
    """This tool collects the function call stack given a function name"""
    try:
        codebase_infos = get_global_codebase_infos()
        # 通过layer_cnt层递归调用栈
        call_to_dict, call_from_dict = codebase_infos.common_infos.func_calltos, codebase_infos.common_infos.func_callfroms
        call_to_stack, call_from_stack = resolve_call_stack(call_to_dict, call_from_dict, func_name, 1)
        if not call_to_stack and not call_from_stack:
            return f"Function call not found: {func_name}"
        return f"Function call to info: {call_to_stack}\nFunction call from info: {call_from_stack}"
    except Exception as e:
        return f"Error collecting function call stack: {e}"

# driver
@mcp.tool()
async def collect_driver_info(driver_name: str) -> str:
    """This tool collects the driver info from the registered database given a driver name"""
    try:
        codebase_infos = get_global_codebase_infos()
        driver_info = codebase_infos.driver_infos.driverfrom_function_dict.get(driver_name)
        if not driver_info:
            return f"Driver not found: {driver_name}"
        return f"Driver info: {driver_info}"
    except Exception as e:
        return f"Error collecting driver info: {e}"

def register_db(db_path: str):
    """注册数据库路径"""
    codebase_infos_dict[db_path] = CodebaseInfos(db_path)
    print(f"Database registered and analyzed: {db_path}")

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
    GLOBAL_DB_PATH = args.db_path
    transport = args.transport
    
    # 验证数据库路径
    db_path_resolved = Path(GLOBAL_DB_PATH).resolve()
    if not db_path_resolved.exists():
        print(f"Error: Database path does not exist: {GLOBAL_DB_PATH}")
        sys.exit(1)
    
    # 初始化全局codebase_infos
    try:
        register_db(GLOBAL_DB_PATH)
    except Exception as e:
        print(f"Error initializing codebase info: {e}")
        sys.exit(1)
    
    # 启动MCP服务器
    mcp.run(transport=transport)