from fastmcp import FastMCP
import config.globs as globs
import asyncio
from models.build_results.build_output import BuildOutput
from tools.builder.proj_builder import build_proj
from tools.collector.collector import get_mmio_func_list, get_function_info
from tools.analyzer.function_classifier import function_classify, analyze_functions
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace

mcp = FastMCP("LCMHalMCP", version="1.0.0", port=8113)

mmio_info_list = {}
mmio_infos_by_file = {}

def replace_funcs():
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            # src_replace(f"{globs.src_path}/{classify_res.file_name}", classify_res.replace_code)
            replace_res = function_replace(get_function_info(globs.db_path, func_name), classify_res)
            print(f"Function {func_name} has replacement, replace result: {replace_res}")

def recover_funcs():
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            recover_res = function_recover(get_function_info(globs.db_path, func_name))
            print(f"Function {func_name} has recovery, recover result: {recover_res}")

@mcp.tool()
async def build_project() -> BuildOutput:
    """build project, return build result, including exitcode and stderr output"""
    # 替换文件
    replace_funcs()
    # 编译项目
    build_info = build_proj(globs.script_path)
    # 项目复原
    recover_funcs()
    # 结果输出
    return f"return_code:{build_info.exit_code}\nstd_err:{build_info.std_err}"

@mcp.tool()
async def get_replace_func_details_by_file(file_path: str):
    """get replacement functions info of the corresponding file"""
    # 从mmio_infos_by_file中获取对应文件的MMIO函数分类结果
    mmio_infos = mmio_infos_by_file.get(file_path, [])
    # 修复：返回JSON格式的数据而不是字符串
    return f"""
        "file_path": {file_path},
        "mmio_functions": {[classify_res.model_dump_json() for classify_res in mmio_infos]}
    """

@mcp.tool()
async def update_function_replacement(func_name: str, replace_code: str):
    """get all replacement functions info"""
    if func_name not in mmio_info_list:
        return {"error": f"Function {func_name} not found in MMIO function list."}
    # 更新替换代码
    mmio_info_list[func_name].replace_code = replace_code
    # 修复：返回JSON格式的数据而不是字符串
    return f"""
        "function_name": {func_name},
        "status": "success"
    """

def init_mcp():
    # 处理所有MMIO函数
    function_list = get_mmio_func_list(globs.db_path)
    # function_list = codebase_infos_dict[globs.db_path].mmio_infos.mmioinfo_mmioexpr_dict.keys()
    mmio_info_list = analyze_functions(function_list)
    # 打印所有MMIO函数的分类结果
    for func_name, classify_res in mmio_info_list.items():
        print(f"Function {func_name} classify result: {classify_res.model_dump_json()}")
    # 分文件收集信息
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            function_info = get_function_info(globs.db_path, func_name)
            mmio_infos_by_file.setdefault(function_info.file_path, []).append(classify_res)

if __name__ == "__main__":
    # TODO: config from cmdline
    
    # 编译脚本路径
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    # 文件系统路径
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    # 项目路径, DB中记录的项目路径
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
    # 初始化服务
    init_mcp()

    # 启动mcp服务器
    mcp.run(transport="stdio")