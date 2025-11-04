from abc import ABC, abstractmethod
from typing import Any, Dict, List

class QueryInfo(ABC):
    """查询信息基类"""
    
    @staticmethod
    @abstractmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, Any]:
        """从查询结果解析信息，返回字典，键为信息名称"""
        pass