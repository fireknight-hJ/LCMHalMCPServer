from pathlib import Path
import shutil
import os

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