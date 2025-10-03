from utils.db_file import read_struct_with_start_line_from_db
from utils.db_query import run_query_and_return_json
from config.collector_infos import *
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from pathlib import Path

from .base import CodebaseInfoBase
from models.query_results.common import FunctionInfo, StructInfo, EnumInfo

@dataclass
class CommonCodebaseInfo(CodebaseInfoBase):
    """通用代码库信息总数据结构"""
    db_path: str = ""
    cache_file: str = ""
    functions: Dict[str, FunctionInfo] = field(default_factory=dict)
    structs: Dict[str, StructInfo] = field(default_factory=dict)
    enums: Dict[str, EnumInfo] = field(default_factory=dict)
    mmio_functions: Dict[str, FunctionInfo] = field(default_factory=dict)
    driver_functions: Dict[str, FunctionInfo] = field(default_factory=dict)
    buffer_functions: Dict[str, FunctionInfo] = field(default_factory=dict)

    def __init__(self, db_path: str = ""):
        """初始化方法，支持从缓存加载"""
        self.db_path = db_path
        self.functions = {}
        self.structs = {}
        self.enums = {}
        self.mmio_functions = {}
        self.driver_functions = {}
        self.buffer_functions = {}
        if db_path:
            self.init_from_cache(db_path)

    def init_from_cache(self, db_path: str) -> bool:
        """
        从缓存初始化数据
        返回是否成功从缓存加载
        """
        self.cache_dir = Path(db_path) / "lcmhal_tmp"
        self.cache_file = self.cache_dir / "common_info.json"
        
        if not self.cache_file.exists():
            print(f"[INFO] 缓存文件不存在: {self.cache_file}")
            return False
        
        try:
            with open(self.cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 验证缓存数据完整性
            if not self._validate_cache_data(data):
                print("[WARN] 缓存数据不完整或格式错误，将重新收集")
                return False
            
            # 从缓存数据恢复
            self._load_from_dict(data)
            print(f"[INFO] 成功从缓存加载数据: {self.cache_file}")
            return True
            
        except Exception as e:
            print(f"[ERROR] 加载缓存失败: {e}")
            return False

    def _validate_cache_data(self, data: Dict) -> bool:
        """验证缓存数据的完整性"""
        required_keys = ["functions", "structs", "enums"]
        return all(key in data for key in required_keys)

    def _load_from_dict(self, data: Dict[str, Any]) -> None:
        """从字典加载数据"""
        # 恢复函数信息
        for name, func_data in data.get("functions", {}).items():
            self.functions[name] = FunctionInfo(
                name=func_data["name"],
                file_path=func_data["file_path"],
                location_line=func_data["location_line"],
                function_content=func_data["function_content"]
            )
        
        # 恢复结构体信息
        for name, struct_data in data.get("structs", {}).items():
            self.structs[name] = StructInfo(
                name=struct_data["name"],
                file_path=struct_data["file_path"],
                location_line=struct_data["location_line"],
                struct_content=struct_data["struct_content"],
                members=struct_data.get("members", {})
            )
        
        # 恢复枚举信息
        for name, enum_data in data.get("enums", {}).items():
            self.enums[name] = EnumInfo(
                name=enum_data["name"],
                value=enum_data["value"]
            )

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式用于JSON序列化"""
        return {
            "functions": {name: {
                "name": func.name,
                "file_path": func.file_path,
                "location_line": func.location_line,
                "function_content": func.function_content
            } for name, func in self.functions.items()},
            "structs": {name: {
                "name": struct.name,
                "file_path": struct.file_path,
                "location_line": struct.location_line,
                "struct_content": struct.struct_content,
                "members": struct.members
            } for name, struct in self.structs.items()},
            "enums": {name: {
                "name": enum.name,
                "value": enum.value
            } for name, enum in self.enums.items()}
        }

    def save_to_cache(self) -> bool:
        """保存数据到缓存"""
        if not self.db_path:
            print("[ERROR] 未设置数据库路径，无法保存缓存")
            return False
        
        try:
            # 确保缓存目录存在
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存数据
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
            
            print(f"[INFO] 数据已保存到缓存: {self.cache_file}")
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
            ("函数信息", self._collect_functions),
            ("结构体信息", self._collect_structs),
            ("枚举信息", self._collect_enums),
        ]
        
        for module_name, collector_func in collectors:
            try:
                print(f"[INFO] 收集{module_name}...")
                collector_func()
            except Exception as e:
                print(f"[ERROR] 收集{module_name}失败: {e}")
                # 继续收集其他模块
        
        # 保存到缓存
        self.save_to_cache()
        print("[INFO] 信息收集完成")

    def _collect_functions(self) -> None:
        """收集函数信息"""
        result = self._run_query_and_return_json(function_collector_query_file)
        if result:
            self.functions = FunctionInfo.resolve_from_query_result(self.db_path, result)
            print("[INFO] 函数信息收集完成")

    def _collect_structs(self) -> None:
        """收集结构体信息"""
        result = self._run_query_and_return_json(struct_collector_query_file)
        if result:
            self.structs = StructInfo.resolve_from_query_result(self.db_path, result)
            print("[INFO] 结构体信息收集完成")

    def _collect_enums(self) -> None:
        """收集枚举信息"""
        result = self._run_query_and_return_json(enum_collector_query_file)
        if result:
            self.enums = EnumInfo.resolve_from_query_result(self.db_path, result)
            print("[INFO] 枚举信息收集完成")


# 使用示例
def create_codebase_info(db_path: str, force_refresh: bool = False) -> CommonCodebaseInfo:
    """
    创建CodebaseInfo实例的便捷函数
    """
    codebase_info = CommonCodebaseInfo()
    codebase_info.collect_infos(db_path, force_refresh)
    return codebase_info


if __name__ == "__main__":
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 示例用法
    codebase_info = create_codebase_info(db_path, force_refresh=False)
    print("[INFO] 代码信息收集完成")