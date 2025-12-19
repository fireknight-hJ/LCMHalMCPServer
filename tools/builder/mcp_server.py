from fastmcp import FastMCP
import json
import config.globs as globs
import asyncio
from models.build_results.build_output import BuildOutput
from models.analyze_results.function_analyze import ReplacementUpdate
from tools.builder.proj_builder import build_proj, clear_proj
from tools.collector.collector import get_mmio_func_list, get_function_info
from tools.analyzer.analyzer import function_classify, analyze_functions
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace
from utils.db_cache import dump_message_json_log, dump_json_log, check_analyzed_json_log, get_analyzed_json_log

mcp = FastMCP("LCMHalMCP", version="1.0.0")

mmio_info_list = {}
mmio_infos_by_file = {}
replacement_updates = {}
replacement_updates_by_file = {}

def replacement_update_log(replacement_update: ReplacementUpdate):
    # log ai memory
    if globs.ai_log_enable:
        dump_json_log("replacement_update", replacement_update.model_dump())

def replace_funcs():
    for func_name, classify_res in mmio_info_list.items():
        if func_name in replacement_updates:
            replace_res = function_replace(get_function_info(globs.db_path, func_name), replacement_updates[func_name].replacement_code)
        elif classify_res.has_replacement:
            # src_replace(f"{globs.src_path}/{classify_res.file_name}", classify_res.replace_code)
            replace_res = function_replace(get_function_info(globs.db_path, func_name), classify_res.function_replacement)
            # 注释掉print语句，避免干扰JSON-RPC通信
            # print(f"Function {func_name} has replacement, replace result: {replace_res}")

def recover_funcs():
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            recover_res = function_recover(get_function_info(globs.db_path, func_name))
            # 注释掉print语句，避免干扰JSON-RPC通信
            # print(f"Function {func_name} has recovery, recover result: {recover_res}")

@mcp.tool()
async def build_project() -> dict:
    """build project, return build result, including exitcode and stderr output"""
    # 替换文件
    replace_funcs()
    # 编译项目
    clear_proj(globs.script_path)
    build_info = build_proj(globs.script_path)
    # 项目复原
    recover_funcs()
    # 结果输出 - 修复：直接返回BuildOutput对象，不要使用json.dumps()
    return {
        "std_err": build_info.std_err,
        "exit_code": build_info.exit_code
    }

@mcp.tool()
async def get_replace_func_details_by_file(file_path: str) -> dict:
    """get replacement functions info of the corresponding file, please make sure the function to be analyzed
    file_path: the full path of the file in the codebase
    replace_func_infos: list of Functions replacement info 
    replacement_updates: list of Functions that have been updated before due to build failure"""
    # 从mmio_infos_by_file中获取对应文件的MMIO函数分类结果
    # 如果可以直接匹配完整文件路径
    mmio_infos = mmio_infos_by_file.get(file_path, [])
    if mmio_infos != []:
        return {
            "file_path": file_path,
            "replaced_function_infos": [info.model_dump() for info in mmio_infos],
            "replacement_updates": [update.model_dump() for update in replacement_updates_by_file.get(file_path, [])]   
        }
    # 模糊匹配c文件名称
    file_path = file_path.split("/")[-1]
    file_paths = []
    for file_name in mmio_infos_by_file.keys():
        if file_name.endswith(file_path):
            file_paths.append(file_name)
    if file_paths == []:
        file_not_found = {"error": f"File {file_path} not found in Replacement MMIO function list, maybe no function replacement in this file?"}
        return file_not_found
    elif len(file_paths) > 1:
        file_path_multimatched = {
            "warnning": f"File {file_path} found in multiple files, please specify the full path, then re-run this tool with the full path.",
            "file_paths": file_paths,
        }
        return file_path_multimatched
    full_path = file_paths[0]
    mmio_infos = mmio_infos_by_file.get(full_path, [])
    replacement_update = replacement_updates_by_file.get(full_path, [])
    replacement_update_func_names = set([update.function_name for update in replacement_update])
    return {
        "file_path": full_path,
        "replaced_function_infos": [info.model_dump() for info in mmio_infos if info.function_name not in replacement_update_func_names],
        "replacement_updates": [update.model_dump() for update in replacement_update]   
    }

@mcp.tool()
async def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """get all replacement functions info"""
    if func_name not in mmio_info_list:
        return {"error": f"Function {func_name} not found in MMIO function list."}
    # 更新替换代码
    replacement_updates[func_name] = ReplacementUpdate(function_name=func_name, replacement_code=replace_code, reason=reason)
    # 存储分析结果
    replacement_update_log(replacement_updates[func_name])
    # 修复：直接返回字典对象，不要使用json.dumps()
    return {
        "function_name": func_name,
        "status": "success"
    }

def init_mcp():
    # 处理所有MMIO函数
    function_list = get_mmio_func_list(globs.db_path)
    # function_list = codebase_infos_dict[globs.db_path].mmio_infos.mmioinfo_mmioexpr_dict.keys()
    global mmio_info_list, replacement_updates
    mmio_info_list = analyze_functions(function_list)
    # 打印所有MMIO函数的分类结果
    # for func_name, classify_res in mmio_info_list.items():
    #     print(f"Function {func_name} classify result: {classify_res.model_dump_json()}")
    # 处理所有替换更新日志
    for func_name, classify_res in mmio_info_list.items():
        if check_analyzed_json_log("replacement_update", func_name):
            json_data = get_analyzed_json_log("replacement_update", func_name)
            if json_data:
                data_dict = json.loads(json_data)
                replacement_updates[func_name] = ReplacementUpdate(**data_dict)
    # 分文件收集信息
    for func_name, classify_res in mmio_info_list.items():
        function_info = get_function_info(globs.db_path, func_name)
        mmio_infos_by_file.setdefault(function_info.file_path, [])
        if classify_res.has_replacement:
            # classify_res.model_dump()
            mmio_infos_by_file.setdefault(function_info.file_path, []).append(classify_res)
        if func_name in replacement_updates:
            replacement_updates_by_file.setdefault(function_info.file_path, []).append(replacement_updates[func_name])
        # src_replace(f"{globs.src_path}/{classify_res.file_name}", classify_res.replace_code)


if __name__ == "__main__":
    # 导入argparse模块（如果尚未导入）
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='LCMHal MCP Server')
    # 添加--script-dir选项参数，设置help信息
    parser.add_argument('--script-dir', dest='script_path', help='Path to the compilation script directory', required=True)
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 从命令行参数设置script_path
    globs.script_path = args.script_path
    # 从配置文件加载配置
    config = globs.load_config_from_yaml(globs.script_path)
    
    # 设置全局变量
    globs.globs_init(config)
    # 初始化服务
    init_mcp()

    # 启动mcp服务器
    mcp.run(transport="stdio")