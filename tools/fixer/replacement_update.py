from models.analyze_results.function_analyze import FixedFunctionInfo
from models.analyze_results.function_analyze import ReplacementUpdate
import config.globs as globs
from utils.db_cache import dump_message_json_log, dump_json_log, check_analyzed_json_log, get_analyzed_json_log
from langchain_core.tools import tool

def replacement_update_log(replacement_update: ReplacementUpdate):
    # log ai memory
    if globs.ai_log_enable:
        dump_json_log("replacement_update", replacement_update.model_dump())


@tool(
    "ReplacementUpdater",
    description="Tool `ReplacementUpdater`, update the replacement code for a specific function in the driver source code"
)
async def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    # 目前只需要存储分析结果
    replacement_update_log(ReplacementUpdate(function_name=func_name, replacement_code=replace_code, reason=reason))
    # 修复：直接返回字典对象，不要使用json.dumps()
    return {
        "function_name": func_name,
        "status": "success"
    }