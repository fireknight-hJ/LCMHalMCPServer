from utils.db_file import read_struct_with_start_line_from_db
from utils.db_query import run_query_and_return_json
from config.collector_infos import *
import subprocess
import json
import re
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from pathlib import Path
from lcmhalmcp.models.query_results.common import FunctionInfo, StructInfo, EnumInfo

@dataclass
class MmioCodebaseInfo:
    """代码库信息总数据结构"""
    db_path: str = ""
    cache_file: str = ""
    mmio_functions: Dict[str, FunctionInfo] = field(default_factory=dict)
    driver_functions: Dict[str, FunctionInfo] = field(default_factory=dict)
    buffer_functions: Dict[str, FunctionInfo] = field(default_factory=dict)

    def __init__(self, db_path: str = ""):
        """初始化方法，支持从缓存加载"""
        self.mmio_functions = {}
        self.driver_functions = {}
        self.buffer_functions = {}
        self.db_path = db_path
        self.cache_file = db_path
        if db_path:
            self.init_from_cache(db_path)

    def init_from_cache(self, db_path: str) -> bool:
        """
        从缓存初始化数据
        返回是否成功从缓存加载
        """
        cache_dir = Path(db_path) / "lcmhal_tmp"
        cache_file = cache_dir / "mmio_info.json"
        
        if not cache_file.exists():
            print(f"[INFO] 缓存文件不存在: {cache_file}")
            return False
        
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 验证缓存数据完整性
            if not self._validate_cache_data(data):
                print("[WARN] 缓存数据不完整或格式错误，将重新收集")
                return False
            
            # 从缓存数据恢复
            self._load_from_dict(data)
            print(f"[INFO] 成功从缓存加载数据: {cache_file}")
            return True
            
        except Exception as e:
            print(f"[ERROR] 加载缓存失败: {e}")
            return False

    def _validate_cache_data(self, data: Dict) -> bool:
        """验证缓存数据的完整性"""
        required_keys = ["mmio_functions", 
                        "driver_functions", "buffer_functions"]
        return all(key in data for key in required_keys)

    def _load_from_dict(self, data: Dict[str, Any]) -> None:
        """从字典加载数据"""
        for name, func_data in data.get("mmio_functions", {}).items():
            self.mmio_functions[name] = FunctionInfo(
                name=func_data["name"],
                file_path=func_data["file_path"],
                location_line=func_data["location_line"],
                function_content=func_data["function_content"]
            )
        
        for name, func_data in data.get("driver_functions", {}).items():
            self.driver_functions[name] = FunctionInfo(
                name=func_data["name"],
                file_path=func_data["file_path"],
                location_line=func_data["location_line"],
                function_content=func_data["function_content"]
            )
        
        for name, func_data in data.get("buffer_functions", {}).items():
            self.buffer_functions[name] = FunctionInfo(
                name=func_data["name"],
                file_path=func_data["file_path"],
                location_line=func_data["location_line"],
                function_content=func_data["function_content"]
            )

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式用于JSON序列化"""
        return {
            "mmio_functions": {name: {
                "name": func.name,
                "file_path": func.file_path,
                "location_line": func.location_line,
                "function_content": func.function_content
            } for name, func in self.mmio_functions.items()},
            "driver_functions": {name: {
                "name": func.name,
                "file_path": func.file_path,
                "location_line": func.location_line,
                "function_content": func.function_content
            } for name, func in self.driver_functions.items()},
            "buffer_functions": {name: {
                "name": func.name,
                "file_path": func.file_path,
                "location_line": func.location_line,
                "function_content": func.function_content
            } for name, func in self.buffer_functions.items()}
        }

    def save_to_cache(self) -> bool:
        """保存数据到缓存"""
        if not self.db_path:
            print("[ERROR] 未设置数据库路径，无法保存缓存")
            return False
        
        cache_dir = Path(self.db_path) / "lcmhal_tmp"
        cache_file = cache_dir / "mmio_info.json"
        
        try:
            # 确保缓存目录存在
            cache_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存数据
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
            
            print(f"[INFO] 数据已保存到缓存: {cache_file}")
            return True
            
        except Exception as e:
            print(f"[ERROR] 保存缓存失败: {e}")
            return False

    def collect_infos(self, db_path: str, force_refresh: bool = False) -> None:
        """
        收集所有信息，支持缓存机制
        Args:
            db_path: 数据库路径
            force_refresh: 是否强制刷新缓存
        """
        self.db_path = db_path
        
        # 如果不是强制刷新，尝试从缓存加载
        if not force_refresh and self.init_from_cache(db_path):
            print("[INFO] 使用缓存数据")
            return
        
        print("[INFO] 开始收集代码信息...")
        
        # 收集各个模块的信息
        collectors = [
            ("MMIO函数信息", self._collect_mmio_functions),
            ("驱动函数信息", self._collect_driver_functions),
            ("缓冲函数信息", self._collect_buffer_functions),
        ]
        
        for module_name, collector_func in collectors:
            try:
                print(f"[INFO] 收集{module_name}...")
                collector_func()
            except Exception as e:
                print(f"[ERROR] 收集{module_name}失败: {e.with_traceback()}")
                # 继续收集其他模块
        
        # 保存到缓存
        self.save_to_cache()
        print("[INFO] 信息收集完成")

    def _run_query_and_return_json(self, query_file: str) -> Optional[List[Any]]:
        """运行query并返回结果"""
        result = run_query_and_return_json(self.db_path, query_file)
        if result:
            return json.loads(result)["#select"]["tuples"]
        return None

    def _collect_mmio_functions(self) -> None:
        """收集MMIO函数信息"""
        result = self._run_query_and_return_json(mmio_function_query_file)
        if result:
            for item in result:
                func_name, file_path, location_line = item[0], item[1], item[2]
                function_content = read_struct_with_start_line_from_db(self.db_path, file_path[1:], location_line, func_name)
                if function_content == "" :
                    continue
                self.mmio_functions[func_name] = FunctionInfo(
                    name=func_name,
                    file_path=file_path,
                    location_line=location_line,
                    function_content=function_content
                )
            print("[INFO] MMIO函数信息收集完成")

    def _collect_driver_functions(self) -> None:
        """收集驱动函数信息"""
        result = self._run_query_and_return_json(driver_function_query_file)
        if result:
            for item in result:
                func_name, file_path, location_line = item[0], item[1], item[2]
                function_content = read_struct_with_start_line_from_db(self.db_path, file_path[1:], location_line, func_name)
                if function_content == "" :
                    continue
                self.driver_functions[func_name] = FunctionInfo(
                    name=func_name,
                    file_path=file_path,
                    location_line=location_line,
                    function_content=function_content
                )
            print("[INFO] 驱动函数信息收集完成")

    def _collect_buffer_functions(self) -> None:
        """收集缓冲函数信息"""
        result = self._run_query_and_return_json(buffer_function_query_file)
        if result:
            for item in result:
                func_name, file_path, location_line = item[0], item[1], item[2]
                function_content = read_struct_with_start_line_from_db(self.db_path, file_path[1:], location_line, func_name)
                if function_content == "" :
                    continue
                self.buffer_functions[func_name] = FunctionInfo(
                    name=func_name,
                    file_path=file_path,
                    location_line=location_line,
                    function_content=function_content
                )
            print("[INFO] 缓冲函数信息收集完成")


# 使用示例
def create_mmiocodebase_info(db_path: str, force_refresh: bool = False) -> CodebaseInfo:
    """
    创建CodebaseInfo实例的便捷函数
    """
    codebase_info = MmioCodebaseInfo()
    codebase_info.collect_infos(db_path, force_refresh)
    return codebase_info


if __name__ == "__main__":
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 示例用法
    codebase_info = create_mmiocodebase_info(db_path, force_refresh=False)
    print("[INFO] 代码信息收集完成")