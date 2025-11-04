from dataclasses import dataclass, field
from typing import List, Dict, Any
from .base import QueryInfo
from utils.db_file import read_struct_with_start_line_from_db, read_line_from_db

@dataclass
class DriverExprInfo(QueryInfo):
    """驱动表达式信息数据结构"""
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
    def from_dict(data: Dict[str, Any]) -> 'DriverExprInfo':
        """从字典创建对象"""
        return DriverExprInfo(
            name=data.get("name", ""),
            function=data.get("function", ""),
            file_path=data.get("file_path", ""),
            start_line=data.get("start_line", 0),
            expr_type=data.get("expr_type", ""),
            enclosing_type=data.get("enclosing_type", "")
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, List['DriverExprInfo']]:
        """从查询结果解析驱动表达式信息，返回字典，键为函数名"""
        expr_dict: Dict[str, List[DriverExprInfo]] = {}
        for item in result:
            func_name = item[1]
            if func_name not in expr_dict:
                expr_dict[func_name] = []
            
            expr = DriverExprInfo(
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
class DriverFunctionContainsInfo(QueryInfo):
    """驱动函数包含信息数据结构"""
    type_name: str
    file_path: str
    start_line: int
    flag: str
    type_content: str
    type_lines: Dict[int, str]

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
    def from_dict(data: Dict[str, Any]) -> 'DriverFunctionContainsInfo':
        """从字典创建对象"""
        return DriverFunctionContainsInfo(
            type_name=data.get("type_name", ""),
            file_path=data.get("file_path", ""),
            start_line=data.get("start_line", 0),
            flag=data.get("flag", ""),
            type_content=data.get("type_content", ""),
            type_lines=data.get("type_lines", {})
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, List['DriverFunctionContainsInfo']]:
        """从查询结果解析驱动函数包含信息，返回字典，键为函数名"""
        
        contains_dict: Dict[str, List[DriverFunctionContainsInfo]] = {}
        for item in result:
            func_name = item[0]
            if func_name not in contains_dict:
                contains_dict[func_name] = []
            
            type_content, type_lines = read_struct_with_start_line_from_db(db_path, item[2][1:], item[3])
            
            contains_info = DriverFunctionContainsInfo(
                type_name=item[1],
                file_path=item[2],
                start_line=item[3],
                flag=item[4],
                type_content=type_content,
                type_lines=type_lines
            )
            contains_dict[func_name].append(contains_info)
        return contains_dict

@dataclass
class DriverFunctionCallInfo(QueryInfo):
    """驱动函数调用信息数据结构"""
    name: str
    callee_name: str
    file_path: str
    start_line: int
    start_line_content: str
    call_type: str

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "callee_name": self.callee_name,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "start_line_content": self.start_line_content,
            "call_type": self.call_type
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'DriverFunctionCallInfo':
        """从字典创建对象"""
        return DriverFunctionCallInfo(
            name=data.get("name", ""),
            callee_name=data.get("callee_name", ""),
            file_path=data.get("file_path", ""),
            start_line=data.get("start_line", 0),
            start_line_content=data.get("start_line_content", ""),
            call_type=data.get("call_type", "")
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, List['DriverFunctionCallInfo']]:
        """从查询结果解析驱动函数调用信息，返回字典，键为函数名"""
        call_dict: Dict[str, List[DriverFunctionCallInfo]] = {}
        for item in result:
            func_name = item[2]
            if func_name not in call_dict:
                call_dict[func_name] = []
            
            call_info = DriverFunctionCallInfo(
                name=item[0],
                callee_name=item[1],
                file_path=item[3],
                start_line=item[4],
                start_line_content=read_line_from_db(db_path, item[3][1:], item[4]),
                call_type=item[5]
            )
            call_dict[func_name].append(call_info)
        return call_dict

@dataclass
class MmioExprInfo(QueryInfo):
    """MMIO表达式信息数据结构"""
    name: str
    function: str
    file_path: str
    start_line: int
    start_line_content: str
    expr_type: str
    enclosing_type: str

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "function": self.function,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "start_line_content": self.start_line_content,
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
            start_line_content=data.get("start_line_content", ""),
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
                start_line_content=read_line_from_db(db_path, item[2][1:], item[3]),
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
    start_line_content: str
    flag: str
    type_content: str
    type_lines: List[str]

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "type_name": self.type_name,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "start_line_content": self.start_line_content,
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
            start_line_content=data.get("start_line_content", ""),
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
                start_line_content=read_line_from_db(db_path, item[2][1:], item[3]),
                flag=item[4],
                type_content=type_content,
                type_lines=type_lines
            )
            contains_dict[func_name].append(contains_info)
        return contains_dict