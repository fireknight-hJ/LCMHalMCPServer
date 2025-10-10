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

@mcp.tool()
async def collect_mmio_func_list(db_path: str) -> str:
    """This tool collects the mmio function list from the registered database"""
    codebase_infos = codebase_infos_dict.get(db_path)
    if not codebase_infos:
        return f"Database not registered: {db_path}"
    return f"MMIO function list: {codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict}"

if __name__ == "__main__":
    # 通过输入参数指定transport方式
    import sys
    if len(sys.argv) > 1:
        transport = sys.argv[1]
    else:
        transport = "streamable-http"
    # 默认使用streamable-http， 其他可选sse或者stdio
    mcp.run(transport=transport)

