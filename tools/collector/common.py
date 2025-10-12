from utils.db_file import read_struct_with_start_line_from_db
from utils.db_query import run_query_and_return_json
from config.collector_infos import *
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from pathlib import Path

from .base import CodebaseInfoBase
from models.query_results.common import FunctionInfo, StructInfo, EnumInfo, FunctionCallInfo

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
    func_calltos: Dict[str, List[FunctionCallInfo]] = field(default_factory=dict)
    func_callfroms: Dict[str, List[FunctionCallInfo]] = field(default_factory=dict)

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
            self.functions[name] = FunctionInfo.from_dict(func_data)
        
        # 恢复结构体信息
        for name, struct_data in data.get("structs", {}).items():
            self.structs[name] = StructInfo.from_dict(struct_data)
        
        # 恢复枚举信息
        for name, enum_data in data.get("enums", {}).items():
            self.enums[name] = EnumInfo.from_dict(enum_data)
        
        # 恢复函数调用信息（如果存在）
        if "func_calltos" in data:
            self.func_calltos = {}
            for caller, calls_data in data["func_calltos"].items():
                self.func_calltos[caller] = [
                    FunctionCallInfo.from_dict(call_data) for call_data in calls_data
                ]
        
        if "func_callfroms" in data:
            self.func_callfroms = {}
            for callee, calls_data in data["func_callfroms"].items():
                self.func_callfroms[callee] = [
                    FunctionCallInfo.from_dict(call_data) for call_data in calls_data
                ]
        
        # 恢复其他模块信息（如果存在）
        if "mmio_functions" in data:
            self.mmio_functions = {}
            for name, func_data in data["mmio_functions"].items():
                self.mmio_functions[name] = FunctionInfo.from_dict(func_data)
        
        if "driver_functions" in data:
            self.driver_functions = {}
            for name, func_data in data["driver_functions"].items():
                self.driver_functions[name] = FunctionInfo.from_dict(func_data)
        
        if "buffer_functions" in data:
            self.buffer_functions = {}
            for name, func_data in data["buffer_functions"].items():
                self.buffer_functions[name] = FunctionInfo.from_dict(func_data)

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式用于JSON序列化"""
        result = {
            "functions": {name: func.to_dict() for name, func in self.functions.items()},
            "structs": {name: struct.to_dict() for name, struct in self.structs.items()},
            "enums": {name: enum.to_dict() for name, enum in self.enums.items()}
        }
        
        # 添加函数调用信息（如果存在）
        if hasattr(self, 'func_calltos') and self.func_calltos:
            result["func_calltos"] = {
                caller: [call.to_dict() for call in calls] 
                for caller, calls in self.func_calltos.items()
            }
        
        if hasattr(self, 'func_callfroms') and self.func_callfroms:
            result["func_callfroms"] = {
                callee: [call.to_dict() for call in calls] 
                for callee, calls in self.func_callfroms.items()
            }
        
        # 添加其他模块信息（如果存在）
        if hasattr(self, 'mmio_functions') and self.mmio_functions:
            result["mmio_functions"] = {name: func.to_dict() for name, func in self.mmio_functions.items()}
        
        if hasattr(self, 'driver_functions') and self.driver_functions:
            result["driver_functions"] = {name: func.to_dict() for name, func in self.driver_functions.items()}
        
        if hasattr(self, 'buffer_functions') and self.buffer_functions:
            result["buffer_functions"] = {name: func.to_dict() for name, func in self.buffer_functions.items()}
        
        return result

    def save_to_cache(self) -> bool:
        """保存数据到缓存"""
        if not self.db_path:
            print("[ERROR] 未设置数据库路径，无法保存缓存")
            return False
        
        cache_dir = Path(self.db_path) / "lcmhal_tmp"
        self.cache_file = cache_dir / "common_info.json"

        try:
            # 确保缓存目录存在
            cache_dir.mkdir(parents=True, exist_ok=True)
            
            # 保存数据
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
            
            print(f"[INFO] 数据已保存到缓存: {self.cache_file}")
            return True
            
        except Exception as e:
            # 打印详细错误信息 栈轨迹
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
            ("函数调用信息", self._collect_function_calls),
        ]
        
        for module_name, collector_func in collectors:
            print(f"[INFO] 收集{module_name}...")
            collector_func()
            # try:
            #     print(f"[INFO] 收集{module_name}...")
            #     collector_func()
            # except Exception as e:
            #     print(f"[ERROR] 收集{module_name}失败: {e}")
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

    def _collect_function_calls(self) -> None:
        """收集函数调用信息"""
        result = self._run_query_and_return_json(function_call_collector_query_file)
        if result:
            self.func_calltos, self.func_callfroms = FunctionCallInfo.resolve_from_query_result(self.db_path, result)
            print("[INFO] 函数调用信息收集完成")

def create_commoncodebase_info(db_path: str, force_refresh: bool = False) -> CommonCodebaseInfo:
    """
    创建CommonCodebaseInfo实例的便捷函数
    """
    common_info = CommonCodebaseInfo()
    common_info.collect_infos(db_path, force_refresh)
    return common_info

if __name__ == "__main__":
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 示例用法
    codebase_info = create_commoncodebase_info(db_path, force_refresh=True)
    print("[INFO] 代码信息收集完成")