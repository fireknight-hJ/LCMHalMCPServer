from fastmcp import FastMCP, Context
from pathlib import Path
from tools.collector.common import *
from tools.collector.driver import *
from tools.collector.mmio import *

mcp = FastMCP("LCMHalMCP", version="1.0.0", port=8112)

# 存储全部三类代码信息
class CodebaseInfos:
    def __init__(self, db_path: str = ""):
        self.db_path = db_path
        if not db_path:
            return
        self.common_infos = create_commoncodebase_info(db_path, force_refresh=False)
        self.driver_infos = create_drivercodebase_info(db_path, force_refresh=False)
        self.mmio_infos = create_mmiocodebase_info(db_path, force_refresh=False)

# 存储所有db的信息
codebase_infos_dict : Dict[str, CodebaseInfos] = {}

@mcp.tool()
async def register_and_analyze_database(db_path: str) -> str:
    """This tool registers a CodeQL database, and analyze it given a path"""
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}"
    
    # 初始化代码信息
    try:
        codebase_infos_dict[db_path] = CodebaseInfos(db_path)
    except Exception as e:
        return f"Failed to initialize codebase info: {e}"
    
    return f"Database registered and analyzed: {db_path}"

# mmio
@mcp.tool()
async def collect_mmio_func_list(db_path: str) -> str:
    """This tool collects the mmio function list from the registered database"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    func_list = codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.keys()
    return f"MMIO function list: {func_list}"

@mcp.tool()
async def collect_mmio_files(db_path: str) -> str:
    """This tool collects the mmio files from the registered database"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    mmio_files = set()
    for i in codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.values():
        mmio_files.add(i.file_path)
    mmio_files = list(mmio_files)
    return f"MMIO files: {mmio_files}"

@mcp.tool()
async def collect_mmio_func_info(db_path: str, func_name: str) -> str:
    """This tool collects the mmio infos and function info from the registered database given a mmio function name"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    mmio_func_info = codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.get(func_name)
    common_func_info = codebase_infos.common_infos.functions.get(func_name)
    if not mmio_func_info or not common_func_info:
        return f"MMIO function not found: {func_name}"
    return f"Function info: {common_func_info}\nMMIO Exprs info: {mmio_func_info}"

# common
@mcp.tool()
async def collect_function_info(db_path: str, func_name: str) -> str:
    """This tool collects the function info from the registered database given a function name"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    func_info = codebase_infos.common_infos.functions.get(func_name)
    if not func_info:
        return f"Function not found: {func_name}"
    return f"Function info: {func_info}"

@mcp.tool()
async def collect_struct_or_enum_info(db_path: str, struct_name: str) -> str:
    """This tool collects the struct or enum info from the registered database"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    struct_info = codebase_infos.common_infos.structs.get(struct_name)
    if not struct_info:
        struct_info = codebase_infos.common_infos.enums.get(struct_name)
        if not struct_info:
            return f"Struct or enum not found: {struct_name}"
        return f"Enum info: {struct_info}"
    return f"Struct info: {struct_info}"

def resolve_call_stack(call_to_dict: Dict[str, List[FunctionCallInfo]], call_from_dict: Dict[str, List[FunctionCallInfo]], func_name: str, layer_cnt: int) -> List[FunctionCallInfo]:
    """递归解析函数调用栈"""
    if layer_cnt <= 0:
        return []
    call_to_info = call_to_dict.get(func_name)
    if not call_to_info:
        return []
    call_from_info = call_from_dict.get(func_name)
    if not call_from_info:
        return []
    return call_to_info, call_from_info

@mcp.tool()
async def collect_func_call_stack(db_path: str, func_name: str) -> str:
    """This tool collects the function call stack given a function name, """
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    # 通过layer_cnt层递归调用栈
    call_to_dict, call_from_dict = codebase_infos.common_infos.func_calltos, codebase_infos.common_infos.func_callfroms
    call_to_stack, call_from_stack = resolve_call_stack(call_to_dict, call_from_dict, func_name, 1)
    if not call_to_stack and not call_from_stack:
        return f"Function call not found: {func_name}"
    return f"Function call to info: {call_to_stack}\nFunction call from info: {call_from_stack}"

# driver
# async def collect_driver_info(db_path: str, driver_name: str) -> str:
#     """This tool collects the driver info from the registered database given a driver name"""
#     codebase_infos = codebase_infos_dict.get(db_path)
#     if not codebase_infos:
#         return f"Database not registered: {db_path}"
#     driver_info = codebase_infos.driver_infos.driverinfo_dict.get(driver_name)
#     if not driver_info:
#         return f"Driver not found: {driver_name}"
#     return f"Driver info: {driver_info}"


if __name__ == "__main__":
    # 通过输入参数指定transport方式
    import sys
    if len(sys.argv) > 1:
        transport = sys.argv[1]
    else:
        transport = "streamable-http"
    # 默认使用streamable-http， 其他可选sse或者stdio
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    codebase_infos_dict[db_path] = CodebaseInfos(db_path)
    mcp.run(transport=transport)

