from models.query_results.common import FunctionInfo
from models.analyze_results.function_analyze import FunctionClassifyResponse

import config.globs as globs
from utils.src_ops import src_replace, file_convert_proj2src



def get_func_content(function_info: FunctionInfo) -> str:
    """
    获取函数的原始代码
    :param function_info: 函数信息
    :return: 函数的原始代码
    """
    code_list = []
    idx = function_info.location_line
    while str(idx) in function_info.function_content_in_lines:
        code_list.append(function_info.function_content_in_lines[str(idx)])
        idx += 1
    ret = "\n".join(code_list)
    return ret

def function_replace(function_info: FunctionInfo, replacement_code: str):
    """
    替换函数的实现
    """
    src_file = file_convert_proj2src(function_info.file_path)
    ret = src_replace(src_file, get_func_content(function_info), replacement_code)
    return ret != ""
