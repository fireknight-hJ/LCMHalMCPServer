from typing import Dict
import logging
import os
import time
import glob

import config.globs as globs

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



# 定义日志函数，加入各种level
def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)

def log_debug(message: str):
    logger.debug(message)

def log_warning(message: str):
    logger.warning(message)

def dump_message(result: Dict[str, any]) -> Dict[str, any]:
    """
    将消息转化为可序列化的字典
    """
    ans = {}
    if "messages" in result:
        model_list =  [i.model_dump() for i in result["messages"]]
        ans["messages"] = model_list
    if "final_response" in result:
        ans["final_response"] = result["final_response"].model_dump()
    return ans

def dump_message_json(result: Dict[str, any]) -> str:
    """
    将消息转化为JSON字符串
    """
    import json
    return json.dumps(dump_message(result), ensure_ascii=False, indent=2)


def dump_message_json_log(msg_type: str="undefined_info", result: Dict[str, any] = {}, file_path: str = ""):
    """
    将消息转化为JSON字符串并写入日志文件
    """
    if file_path == "":
        # 当前项目执行路径
        tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        file_path = os.path.join(tmp_dir, f"{msg_type}_{result['final_response'].function_name}_{time.strftime('%Y%m%d%H%M%S', time.localtime())}.json")
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
    return len(matching_files) > 0