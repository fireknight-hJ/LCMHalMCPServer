import asyncio
import config.globs as globs
from tools.builder.proj_builder import build_proj_dbgen
from tools.analyzer.function_classifier import function_classify
from tools.collector.mcp_server import collect_mmio_func_list, register_db, codebase_infos_dict

def analyze_functions(function_list):
    mmio_info_list = {}
    for func_name in function_list:
        try:
            classifier_res = asyncio.run(function_classify(func_name))
            mmio_info_list[func_name] = classifier_res
        except Exception as e:
            print(f"Error analyzing function {func_name}: {e}")
    return mmio_info_list

def replace_functions(mmio_info_list):
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.replace_func_name:
            print(f"Replace function {func_name} with {classify_res.replace_func_name}")

if __name__ == "__main__":
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer_Macbook"
    # 初始化数据库
    build_proj_dbgen(globs.script_path, globs.db_path)
    # 预分析数据库
    register_db(globs.db_path)
    # 处理所有MMIO函数
    mmio_info_list = {}
    function_list = codebase_infos_dict[globs.db_path].mmio_infos.mmioinfo_mmioexpr_dict.keys()
    mmio_info_list = analyze_functions(function_list)
    # 打印所有MMIO函数的分类结果
    for func_name, classify_res in mmio_info_list.items():
        print(f"Function {func_name} classify result: {classify_res.model_dump_json()}")
    # 找到所有有替换函数条目并进行替换

    for func_name, classify_res in mmio_info_list.items():
        if classify_res.replace_func_name:
            print(f"Function {func_name} has replace function {classify_res.replace_func_name}")

"""
当前workflow：

Tool-编译工具
1. 编译项目并生成DB
Tool-codeql预分析工具
1. 静态分析DB中的函数


Agent-分类Agent工作
1. 分析DB中的函数
2. 分类函数

Tool-分类结果总结工具
1. 根据结果总结待替换文件和替换函数

Agent-替换Agent工作
4. 替换函数

Agent-编译Agent工作
5. 尝试重新编译
6. 编译失败尝试修复
"""
