from dataclasses import dataclass, field
from typing import List, Dict, Any
from .base import QueryInfo
from utils.db_file import read_struct_with_start_line_from_db

@dataclass
class MmioExprInfo(QueryInfo):
    """MMIO表达式信息数据结构"""
    name: str
    function: str
    file_path: str
    start_line: int
    expr_type: str
    enclosing_type: str

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "function": self.function,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "expr_type": self.expr_type,
            "enclosing_type": self.enclosing_type
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'MmioExprInfo':
        """从字典创建对象"""
        return MmioExprInfo(
            name=data.get("name", ""),
            function=data.get("function", ""),
            file_path=data.get("file_path", ""),
            start_line=data.get("start_line", 0),
            expr_type=data.get("expr_type", ""),
            enclosing_type=data.get("enclosing_type", "")
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, List['MmioExprInfo']]:
        """从查询结果解析MMIO表达式信息，返回字典，键为函数名"""
        expr_dict: Dict[str, List[MmioExprInfo]] = {}
        for item in result:
            func_name = item[1]
            if func_name not in expr_dict:
                expr_dict[func_name] = []
            
            expr = MmioExprInfo(
                name=item[0],
                function=func_name,
                file_path=item[2],
                start_line=item[3],
                expr_type=item[4],
                enclosing_type=item[5]
            )
            expr_dict[func_name].append(expr)
        return expr_dict

@dataclass
class MmioFunctionContainsInfo(QueryInfo):
    """MMIO函数包含信息数据结构"""
    type_name: str
    file_path: str
    start_line: int
    flag: str
    type_content: str
    type_lines: List[str]

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "type_name": self.type_name,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "flag": self.flag,
            "type_content": self.type_content,
            "type_lines": self.type_lines
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'MmioFunctionContainsInfo':
        """从字典创建对象"""
        return MmioFunctionContainsInfo(
            type_name=data.get("type_name", ""),
            file_path=data.get("file_path", ""),
            start_line=data.get("start_line", 0),
            flag=data.get("flag", ""),
            type_content=data.get("type_content", ""),
            type_lines=data.get("type_lines", [])
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, List['MmioFunctionContainsInfo']]:
        """从查询结果解析MMIO函数包含信息，返回字典，键为函数名"""
        
        
        contains_dict: Dict[str, List[MmioFunctionContainsInfo]] = {}
        for item in result:
            func_name = item[0]
            if func_name not in contains_dict:
                contains_dict[func_name] = []
            
            type_content, type_lines = read_struct_with_start_line_from_db(db_path, item[2][1:], item[3])
            
            contains_info = MmioFunctionContainsInfo(
                type_name=item[1],
                file_path=item[2],
                start_line=item[3],
                flag=item[4],
                type_content=type_content,
                type_lines=type_lines
            )
            contains_dict[func_name].append(contains_info)
        return contains_dict