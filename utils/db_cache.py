from pathlib import Path
import shutil
import os
from config import globs
import time
import glob
from typing import Dict


def clear_cache(db_path: str, query_infos: list = []):
    if query_infos == []:
        tmp_path = str(Path(db_path) / "lcmhal_tmp")
        # 删除整个tmp文件夹及其内容 （直接删除，不提示确认）
        if Path(tmp_path).exists():
            shutil.rmtree(tmp_path)
    else:
        for query in query_infos:
            output_path = str(Path(db_path) / "lcmhal_tmp" / str(query) + ".bqrs")
            if Path(output_path).exists():
                os.remove(output_path)


def dump_message(result: Dict[str, any]) -> Dict[str, any]:
    """
    将消息转化为可序列化的字典
    """
    ans = {}
    if "messages" in result:
        model_list =  [i.model_dump() for i in result["messages"]]
        ans["messages"] = model_list
    if "final_response" in result and result["final_response"] is not None:
        ans["final_response"] = result["final_response"].model_dump()
    return ans

def dump_message_json(result: Dict[str, any]) -> str:
    """
    将消息转化为JSON字符串
    """
    import json
    return json.dumps(dump_message(result), ensure_ascii=False, indent=2)

def dump_json_log(msg_type: str="undefined_info", result: Dict[str, any] = {}, file_path: str = ""):
    """
    直接将字典转化为json字符串并写入日志文件
    """
    if "function_name" in result:
        function_name = result["function_name"]
    else:
        function_name = ""
    import json
    # 检查文件路径是否为空
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        file_path = os.path.join(tmp_dir, f"{msg_type}_{function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=2))

def dump_message_raw_log(msg_type: str="undefined_info", result: str = "", file_path: str = "", overwrite: bool = False):
    """
    将原始字符串写入日志文件
    """
    function_name = ""
    # 检查文件路径是否为空
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        if overwrite:
            file_path = get_analyzed_json_log_path(msg_type, function_name)
            if file_path == "":
                file_path = os.path.join(tmp_dir, f"{msg_type}_{function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
        else:
            file_path = os.path.join(tmp_dir, f"{msg_type}_{function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(result)

def dump_message_json_log(msg_type: str="undefined_info", result: Dict[str, any] = {}, file_path: str = "", overwrite: bool = False):
    """
    将消息转化为JSON字符串并写入日志文件
    """
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        # 获取Function名称
        function_name = ""
        # 如果来自AIMemory，则会有FinalResponse->FunctionName
        if "final_response" in result:
            if hasattr(result["final_response"], "function_name"):
                function_name = result["final_response"].function_name
        # 如果来自其他数据结构，则会有FunctionName
        elif "function_name" in result:
            function_name = result["function_name"]
        file_path = ""
        if overwrite:
            file_path = get_analyzed_json_log_path(msg_type, function_name)
            if file_path == "":
                file_path = os.path.join(tmp_dir, f"{msg_type}_{function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
        else:
            file_path = os.path.join(tmp_dir, f"{msg_type}_{function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(dump_message_json(result))

def check_analyzed_json_log(msg_type: str="undefined_info", func_name: str = "", file_path: str = "") -> bool:
    """
    检查JSON日志文件是否存在
    """
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            return False
        file_path = os.path.join(tmp_dir, f"{msg_type}_{func_name}_*.json")
    # 使用glob检查匹配的文件是否存在
    matching_files = glob.glob(file_path)
    # 使用列表推导式创建新列表，避免在遍历同时修改列表
    matching_files = [file for file in matching_files if "_".join(file.split("_")[:-1]).endswith(f"{msg_type}_{func_name}")]
    return len(matching_files) > 0

def get_analyzed_json_log_path(msg_type: str="undefined_info", func_name: str = "", file_path: str = "") -> str:
    """
    获取分析过的JSON日志文件路径
    如果不存在则返回空字符串
    """
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            return ""
        # 匹配文件名模式({msg_type}_{func_name}_日期.json)
        file_path = os.path.join(tmp_dir, f"{msg_type}_{func_name}_*.json")
    
    # 使用glob检查匹配的文件是否存在，并按时间排序（最新的在前）
    matching_files = sorted(glob.glob(file_path), key=os.path.getmtime, reverse=True)
    # 使用列表推导式创建新列表，避免在遍历同时修改列表
    matching_files = [file for file in matching_files if "_".join(file.split("_")[:-1]).endswith(f"{msg_type}_{func_name}")]
    if len(matching_files) > 0:
        # 返回第一个匹配文件路径（现在总是最新的文件）
        return matching_files[0]
    return ""

def get_analyzed_json_log(msg_type: str="undefined_info", func_name: str = "", file_path: str = "") -> str:
    """
    获取分析过的JSON日志文件内容
    如果不存在则返回空字符串
    """
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            return ""
        # 匹配文件名模式({msg_type}_{func_name}_日期.json)
        file_path = os.path.join(tmp_dir, f"{msg_type}_{func_name}_*.json")
    
    # 使用glob检查匹配的文件是否存在，并按时间排序（最新的在前）
    matching_files = sorted(glob.glob(file_path), key=os.path.getmtime, reverse=True)
    # 使用列表推导式创建新列表，避免在遍历同时修改列表
    matching_files = [file for file in matching_files if "_".join(file.split("_")[:-1]).endswith(f"{msg_type}_{func_name}")]
    if len(matching_files) > 0:
        # 读取第一个匹配文件内容（现在总是最新的文件）
        with open(matching_files[0], "r", encoding="utf-8") as f:
            return f.read()
    return ""