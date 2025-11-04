from abc import ABC, abstractmethod
from typing import Any, Dict
from pathlib import Path
import json

class CodebaseInfoBase(ABC):
    """代码库信息基类"""
    
    def __init__(self, db_path: str = ""):
        """初始化方法，支持从缓存加载"""
        self.db_path = db_path
        if db_path:
            self.init_from_cache(db_path)

    @abstractmethod
    def init_from_cache(self, db_path: str) -> bool:
        """从缓存初始化数据"""
        pass

    @abstractmethod
    def _validate_cache_data(self, data: Dict) -> bool:
        """验证缓存数据的完整性"""
        pass

    @abstractmethod
    def _load_from_dict(self, data: Dict[str, Any]) -> None:
        """从字典加载数据"""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式用于JSON序列化"""
        pass

    @abstractmethod
    def save_to_cache(self) -> bool:
        """保存数据到缓存"""
        pass

    @abstractmethod
    def collect_infos(self, db_path: str, force_refresh: bool = False) -> None:
        """收集所有信息，支持缓存机制"""
        pass

    def _run_query_and_return_json(self, query_file: str) -> Any:
        """运行query并返回结果"""
        from utils.db_query import run_query_and_return_json
        result = run_query_and_return_json(self.db_path, query_file)
        if result:
            return json.loads(result)["#select"]["tuples"]
        return None