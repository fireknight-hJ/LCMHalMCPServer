from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from tools.collector.common import *
from tools.collector.driver import *
from tools.collector.mmio import *
from utils.db_file import list_files_in_db_zip
from models.query_results.common import FunctionCallInfo

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

def get_global_codebase_infos(db_path: str) -> CodebaseInfos:
    """获取全局的codebase_infos实例"""
    if not db_path:
        raise ValueError("Database path not set. Please provide db_path.")
    
    if db_path not in codebase_infos_dict:
        codebase_infos_dict[db_path] = CodebaseInfos(db_path)
    
    return codebase_infos_dict[db_path]

def register_db(db_path: str) -> bool:
    """注册数据库路径"""
    try:
        codebase_infos_dict[db_path] = CodebaseInfos(db_path)
        print(f"Database registered and analyzed: {db_path}")
        return True
    except Exception as e:
        print(f"Error registering database: {e}")
        return False

# 文件列表相关接口
def get_files_in_db_zip(db_path: str) -> List[str]:
    """获取数据库zip文件中的文件列表"""
    try:
        return list_files_in_db_zip(db_path)
    except Exception as e:
        print(f"Error listing files in src.zip: {e}")
        return []

def get_tree_in_db_zip(db_path: str) -> str:
    """获取数据库zip文件中的目录树"""
    try:
        return list_tree_in_db_zip(db_path)
    except Exception as e:
        print(f"Error listing tree in src.zip: {e}")
        return ""

# MMIO相关接口
def get_mmio_func_list(db_path: str) -> List[str]:
    """获取 CodeQL 认定的全部 MMIO 相关函数名（`info_mmio_function_collector.ql` / `MMIOFunction`），已排序。

    条件：函数体内存在 `MMIOFieldAccess`，或通过 inline/weak 调用链触及 MMIO（见 `MMIOAnalyzer.isMMIOFunction`）。
    用于 Builder / FunctionClassifier / emulate `mmio_funcs` 等与「含 MMIO 操作」相关的流程。
    """
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        return sorted(codebase_infos.mmio_infos.mmio_functions.keys())
    except Exception as e:
        print(f"Error getting MMIO function list: {e}")
        return []


def get_mmio_func_list_interesting_mmioexpr(db_path: str) -> List[str]:
    """较窄子集：`mmioinfo_mmioexpr_collector.ql`（需 `isInterestingMMIOFunction` + `MMIOTracedExpr`）。

    数量通常远小于 `get_mmio_func_list()`；仅在为旧行为或对比统计保留时使用。
    """
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        return list(codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.keys())
    except Exception as e:
        print(f"Error getting interesting-MMIO-expr function list: {e}")
        return []


def get_mmio_func_list_all(db_path: str) -> List[str]:
    """与 `get_mmio_func_list()` 相同；保留别名以便旧代码与文档引用。"""
    return get_mmio_func_list(db_path)

def get_mmio_files(db_path: str) -> List[str]:
    """获取 MMIO 相关文件列表（interesting expr 子集 + `MMIOFunction` 全集上的文件路径并集）。"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        mmio_files: Set[str] = set()
        for mmio_info in codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.values():
            if isinstance(mmio_info, list):
                for info in mmio_info:
                    mmio_files.add(info.file_path)
            else:
                mmio_files.add(mmio_info.file_path)
        for fi in codebase_infos.mmio_infos.mmio_functions.values():
            if fi is not None and getattr(fi, "file_path", None):
                mmio_files.add(fi.file_path)
        return list(mmio_files)
    except Exception as e:
        print(f"Error getting MMIO files: {e}")
        return []

def get_mmio_func_info(db_path: str, func_name: str) -> Dict[str, Any]:
    """获取 MMIO 函数详细信息。优先返回 interesting-MMIO-expr 子集中的逐条表达式；否则仅返回 `MMIOFunction` 元数据。"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        mmio_func_info = codebase_infos.mmio_infos.mmioinfo_mmioexpr_dict.get(func_name)
        common_func_info = codebase_infos.common_infos.functions.get(func_name)

        if not common_func_info:
            return {"error": f"Function not found in database: {func_name}"}

        if mmio_func_info is not None:
            return {
                "function_info": common_func_info,
                "mmio_exprs_info": mmio_func_info,
            }

        if func_name in codebase_infos.mmio_infos.mmio_functions:
            return {
                "function_info": common_func_info,
                "mmio_exprs_info": [],
                "mmio_note": (
                    "In CodeQL MMIOFunction set but no per-expr row in mmioinfo_mmioexpr_collector "
                    "(interesting-MMIO-expr subset); use function body for access detail."
                ),
            }

        return {"error": f"MMIO function not found: {func_name}"}
    except Exception as e:
        print(f"Error getting MMIO function info: {e}")
        return {"error": str(e)}

# 通用函数相关接口
def get_function_info(db_path: str, func_name: str) -> Optional[Any]:
    """获取函数信息"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        func_info = codebase_infos.common_infos.functions.get(func_name)
        return func_info
    except Exception as e:
        print(f"Error getting function info: {e}")
        return None


def get_function_source(db_path: str, func_name: str) -> Optional[str]:
    """Get the original function source code as a single string, for use in rubric checks."""
    func_info = get_function_info(db_path, func_name)
    if not func_info or not getattr(func_info, "function_content_in_lines", None):
        return None
    lines = func_info.function_content_in_lines
    idx = getattr(func_info, "location_line", 0)
    code_list = []
    while True:
        line = lines.get(str(idx)) or lines.get(idx)
        if line is None:
            break
        code_list.append(line)
        idx += 1
    return "\n".join(code_list) if code_list else None


def get_struct_or_enum_info(db_path: str, struct_name: str) -> Dict[str, Any]:
    """获取结构体或枚举信息"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        struct_info = codebase_infos.common_infos.structs.get(struct_name)
        if struct_info:
            return {"type": "struct", "info": struct_info}
        
        enum_info = codebase_infos.common_infos.enums.get(struct_name)
        if enum_info:
            return {"type": "enum", "info": enum_info}
        
        return {"error": f"Struct or enum not found: {struct_name}"}
    except Exception as e:
        print(f"Error getting struct or enum info: {e}")
        return {"error": str(e)}

def resolve_call_stack(call_to_dict: Dict[str, List[FunctionCallInfo]], 
                      call_from_dict: Dict[str, List[FunctionCallInfo]], 
                      func_name: str, layer_cnt: int) -> tuple:
    """递归解析函数调用栈"""
    if layer_cnt <= 0:
        return [], []
    call_to_info = call_to_dict.get(func_name, [])
    call_from_info = call_from_dict.get(func_name, [])
    return call_to_info, call_from_info

def get_func_call_stack(db_path: str, func_name: str, layer_cnt: int = 1) -> Dict[str, Any]:
    """获取函数调用栈"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        call_to_dict, call_from_dict = codebase_infos.common_infos.func_calltos, codebase_infos.common_infos.func_callfroms
        call_to_stack, call_from_stack = resolve_call_stack(call_to_dict, call_from_dict, func_name, layer_cnt)
        
        if not call_to_stack and not call_from_stack:
            return {"error": f"Function call not found: {func_name}"}
        
        return {
            "call_to_info": call_to_stack,
            "call_from_info": call_from_stack
        }
    except Exception as e:
        print(f"Error getting function call stack: {e}")
        return {"error": str(e)}

# 驱动相关接口
def get_driver_info(db_path: str, driver_name: str) -> Optional[Any]:
    """获取驱动信息"""
    try:
        codebase_infos = get_global_codebase_infos(db_path)
        driver_info = codebase_infos.driver_infos.driverfrom_function_dict.get(driver_name)
        return driver_info
    except Exception as e:
        print(f"Error getting driver info: {e}")
        return None

# 数据库验证接口
def validate_database(db_path: str) -> Dict[str, Any]:
    """验证数据库路径和完整性"""
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return {"valid": False, "error": f"Database path does not exist: {db_path}"}

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return {"valid": False, "error": f"Missing required src.zip in: {db_path}"}
    
    return {"valid": True, "message": f"Database is valid: {db_path}"}

if __name__ == "__main__":
    # 示例用法
    db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    
    # 注册数据库
    if register_db(db_path):
        # 获取MMIO函数列表
        mmio_funcs = get_mmio_func_list(db_path)
        print(f"MMIO functions: {mmio_funcs}")
        
        # 获取函数信息
        if mmio_funcs:
            func_info = get_function_info(db_path, mmio_funcs[0])
            print(f"Function info: {func_info}")