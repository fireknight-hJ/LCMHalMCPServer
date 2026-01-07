import asyncio
import os
import yaml
import config.globs as globs
from config.globs import load_config_from_yaml
from tools.builder.proj_builder import build_proj_dbgen, clear_proj
from agents.analyzer_agent import analyze_functions
from tools.collector.collector import get_mmio_func_list, register_db, get_function_info
from tools.replacer.code_replacer import function_replace
from tools.replacer.code_recover import function_recover
from tools.emulator.conf_generator import generate_emulator_configs
# from tools.collector.mmio import function
from utils.src_ops import src_replace


async def main():
    # 获取命令行输入的script_path，默认为默认配置中的路径
    import sys
    script_path = sys.argv[1] if len(sys.argv) > 1 else globs.default_config["script_path"]
    
    # 从配置文件加载配置
    config = load_config_from_yaml(script_path)
    
    # 设置全局变量
    globs.globs_init(config)
    
    # 初始化数据库
    build_proj_dbgen(globs.script_path, globs.db_path)
    # 预分析数据库
    register_db(globs.db_path)
    # # 编译项目
    from tools.builder.core import build_project
    build_output = build_project()
    print(f"Build project output: {build_output}")
    # 生成配置文件
    generate_emulator_configs()
    # 执行模拟器（根据用户反馈调整为使用agent workflow）
    from agents.emulator_runner_agent import run_emulator
    emulate_output = await run_emulator()
    print(f"Emulate output: {emulate_output}")

# 运行主函数
if __name__ == "__main__":
    asyncio.run(main())

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