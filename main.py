import asyncio
import config.globs as globs
from tools.analyzer.function_classifier import function_classify
from tools.collector.mcp_server import collect_mmio_func_list, register_db, codebase_infos_dict
from utils.log import check_analyzed_json_log

if __name__ == "__main__":
    register_db(globs.db_path)
    function_list = codebase_infos_dict[globs.db_path].mmio_infos.mmioinfo_mmioexpr_dict.keys()
    for func_name in function_list:
        try:
            if not check_analyzed_json_log("function_classify", func_name):
                asyncio.run(function_classify(func_name))
            else:
                print(f"Function {func_name} has been analyzed, skip.")
        except Exception as e:
            print(f"Error analyzing function {func_name}: {e}")
