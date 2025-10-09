from utils.db_file import read_struct_with_start_line_from_db
from utils.db_query import run_query_and_return_json
from config.collector_infos import *
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from pathlib import Path

from .base import CodebaseInfoBase
from models.query_results.driver import (
    DriverExprInfo, DriverFunctionContainsInfo, DriverFunctionCallInfo
)

@dataclass
class DriverCodebaseInfo(CodebaseInfoBase):
    """驱动代码库信息总数据结构"""
    db_path: str = ""
    cache_file: str = ""
    driverfrom_expr_dict: Dict[str, List[DriverExprInfo]] = field(default_factory=dict)
    driverfrom_function_dict: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    driverfrom_function_contains_dict: Dict[str, List[DriverFunctionContainsInfo]] = field(default_factory=dict)
    driverto_functioncall_dict: Dict[str, List[DriverFunctionCallInfo]] = field(default_factory=dict)

    def __init__(self, db_path: str = ""):
        """初始化方法，支持从缓存加载"""
        self.db_path = db_path
        self.driverfrom_expr_dict = {}
        self.driverfrom_function_dict = {}
        self.driverfrom_function_contains_dict = {}
        self.driverto_functioncall_dict = {}
        if db_path:
            self.init_from_cache(db_path)

    def init_from_cache(self, db_path: str) -> bool:
        """
        从缓存初始化数据
        返回是否成功从缓存加载
        """
        cache_dir = Path(db_path) / "lcmhal_tmp"
        cache_file = cache_dir / "driver_info.json"
        
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
        required_keys = ["driverfrom_expr_dict", "driverfrom_function_dict", 
                        "driverfrom_function_contains_dict", "driverto_functioncall_dict"]
        return all(key in data for key in required_keys)

    def _load_from_dict(self, data: Dict[str, Any]) -> None:
        """从字典加载数据"""
        # 恢复驱动表达式信息
        for func_name, expr_list in data.get("driverfrom_expr_dict", {}).items():
            self.driverfrom_expr_dict[func_name] = []
            for expr_data in expr_list:
                self.driverfrom_expr_dict[func_name].append(DriverExprInfo(
                    name=expr_data["name"],
                    function=expr_data["function"],
                    file_path=expr_data["file_path"],
                    start_line=expr_data["start_line"],
                    expr_type=expr_data["expr_type"],
                    enclosing_type=expr_data["enclosing_type"]
                ))
        
        # 恢复驱动函数信息
        self.driverfrom_function_dict = data.get("driverfrom_function_dict", {})
        
        # 恢复驱动函数包含信息
        for func_name, contains_list in data.get("driverfrom_function_contains_dict", {}).items():
            self.driverfrom_function_contains_dict[func_name] = []
            for contains_data in contains_list:
                self.driverfrom_function_contains_dict[func_name].append(DriverFunctionContainsInfo(
                    type_name=contains_data["type_name"],
                    file_path=contains_data["file_path"],
                    start_line=contains_data["start_line"],
                    flag=contains_data["flag"],
                    type_content=contains_data["type_content"],
                    type_lines=contains_data["type_lines"]
                ))
        
        # 恢复驱动函数调用信息
        for func_name, call_list in data.get("driverto_functioncall_dict", {}).items():
            self.driverto_functioncall_dict[func_name] = []
            for call_data in call_list:
                self.driverto_functioncall_dict[func_name].append(DriverFunctionCallInfo(
                    name=call_data["name"],
                    callee_name=call_data["callee_name"],
                    file_path=call_data["file_path"],
                    start_line=call_data["start_line"],
                    call_type=call_data["call_type"]
                ))

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式用于JSON序列化"""
        return {
            "driverfrom_expr_dict": {
                func_name: [{
                    "name": expr.name,
                    "function": expr.function,
                    "file_path": expr.file_path,
                    "start_line": expr.start_line,
                    "expr_type": expr.expr_type,
                    "enclosing_type": expr.enclosing_type
                } for expr in expr_list]
                for func_name, expr_list in self.driverfrom_expr_dict.items()
            },
            "driverfrom_function_dict": self.driverfrom_function_dict,
            "driverfrom_function_contains_dict": {
                func_name: [{
                    "type_name": contains.type_name,
                    "file_path": contains.file_path,
                    "start_line": contains.start_line,
                    "flag": contains.flag,
                    "type_content": contains.type_content,
                    "type_lines": contains.type_lines
                } for contains in contains_list]
                for func_name, contains_list in self.driverfrom_function_contains_dict.items()
            },
            "driverto_functioncall_dict": {
                func_name: [{
                    "name": call.name,
                    "callee_name": call.callee_name,
                    "file_path": call.file_path,
                    "start_line": call.start_line,
                    "call_type": call.call_type
                } for call in call_list]
                for func_name, call_list in self.driverto_functioncall_dict.items()
            }
        }

    def save_to_cache(self) -> bool:
        """保存数据到缓存"""
        if not self.db_path:
            print("未设置数据库路径，无法保存缓存")
            return False
        
        cache_dir = Path(self.db_path) / "lcmhal_tmp"
        cache_file = cache_dir / "driver_info.json"
        
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
        
        print("[INFO] 开始收集驱动代码信息...")
        
        # 收集各个模块的信息
        collectors = [
            ("驱动表达式信息", self._collect_driverfrom_expr),
            ("驱动函数信息", self._collect_driverfrom_function),
            ("驱动函数包含信息", self._collect_driverfrom_function_contains),
            ("驱动函数调用信息", self._collect_driverto_functioncall),
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
        print("[INFO] 驱动信息收集完成")

    def _collect_driverfrom_expr(self) -> None:
        """收集驱动表达式信息"""
        result = self._run_query_and_return_json(driverfrom_expr_query_file)
        if result:
            expr_dict = DriverExprInfo.resolve_from_query_result(self.db_path, result)
            self.driverfrom_expr_dict.update(expr_dict)
            print("[INFO] 驱动表达式信息收集完成")

    def _collect_driverfrom_function(self) -> None:
        """收集驱动函数信息"""
        # 需要先收集函数信息
        from .common import create_codebase_info
        common_info = create_codebase_info(self.db_path, force_refresh=False)
        
        result = self._run_query_and_return_json(driverfrom_function_query_file)
        if result:
            for item in result:
                func_name = item[0]
                if func_name in common_info.functions:
                    self.driverfrom_function_dict[func_name] = {
                        "file_path": common_info.functions[func_name].file_path,
                        "location_line": common_info.functions[func_name].location_line
                    }
            print("[INFO] 驱动函数信息收集完成")

    def _collect_driverfrom_function_contains(self) -> None:
        """收集驱动函数包含信息"""
        result = self._run_query_and_return_json(driverfrom_function_contains_query_file)
        if result:
            contains_dict = DriverFunctionContainsInfo.resolve_from_query_result(self.db_path, result)
            self.driverfrom_function_contains_dict.update(contains_dict)
            print("[INFO] 驱动函数包含信息收集完成")

    def _collect_driverto_functioncall(self) -> None:
        """收集驱动函数调用信息"""
        result = self._run_query_and_return_json(driverto_functioncall_query_file)
        if result:
            call_dict = DriverFunctionCallInfo.resolve_from_query_result(self.db_path, result)
            self.driverto_functioncall_dict.update(call_dict)
            print("[INFO] 驱动函数调用信息收集完成")


# 使用示例
def create_drivercodebase_info(db_path: str, force_refresh: bool = False) -> DriverCodebaseInfo:
    """
    创建DriverCodebaseInfo实例的便捷函数
    """
    driver_info = DriverCodebaseInfo()
    driver_info.collect_infos(db_path, force_refresh)
    return driver_info


if __name__ == "__main__":
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    # 示例用法
    driver_info = create_drivercodebase_info(db_path, force_refresh=True)
    print("[INFO] 驱动代码信息收集完成")