import asyncio
import config.globs as globs
from tools.analyzer.function_classifier import function_classify
from tools.collector.mcp_server import collect_mmio_func_list, register_db, codebase_infos_dict
from utils.log import check_analyzed_json_log

if __name__ == "__main__":
    # 注册数据库
    register_db(globs.db_path)
    # 处理所有MMIO函数
    mmio_info_list = {}
    function_list = codebase_infos_dict[globs.db_path].mmio_infos.mmioinfo_mmioexpr_dict.keys()
    for func_name in function_list:
        try:
            if not check_analyzed_json_log("function_classify", func_name):
                classifier_res = asyncio.run(function_classify(func_name))
                mmio_info_list[func_name] = classifier_res
            else:
                print(f"Function {func_name} has been analyzed, skip.")
        except Exception as e:
            print(f"Error analyzing function {func_name}: {e}")
    # 打印所有MMIO函数的分类结果
    for func_name, classify_res in mmio_info_list.items():
        print(f"Function {func_name} classify result: {classify_res.model_dump_json()}")
    # 找到所有有替换函数条目并进行替换
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.replace_func_name:
            print(f"Function {func_name} has replace function {classify_res.replace_func_name}")
