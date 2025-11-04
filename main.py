import asyncio
import config.globs as globs
from tools.builder.proj_builder import build_proj_dbgen, clear_proj
from tools.builder.builder_tool import build_project
from tools.analyzer.function_classifier import analyze_functions
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from tools.replacer.code_replacer import function_replace
from tools.replacer.code_recover import function_recover
# from tools.collector.mmio import function
from utils.src_ops import src_replace

if __name__ == "__main__":
    # TODO: 从命令行输入
    # 编译脚本路径
    globs.script_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver"
    # codeql的DB路径
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 源文件路径, 可能存在src目录和db中的目录有出入, 所以需要根据db中的路径来替换
    globs.src_path = "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer"
    # 项目路径, DB中记录的项目路径
    globs.proj_path = "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
    # 初始化数据库
    build_proj_dbgen(globs.script_path, globs.db_path)
    # 预分析数据库
    register_db(globs.db_path)
    # 编译项目
    build_output = asyncio.run(build_project())
    print(f"Build project output: {build_output.model_dump_json()}")



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