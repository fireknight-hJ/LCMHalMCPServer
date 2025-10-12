from dataclasses import dataclass, field
from utils.db_file import read_struct_with_start_line_from_db, read_line_from_db
from typing import Any, Dict, List, Tuple
from models.query_results.base import QueryInfo

# common infos collector
@dataclass
class FunctionInfo(QueryInfo):
    """函数信息数据结构"""
    name: str
    file_path: str
    location_line: int
    function_content: str
    function_content_in_lines: Dict[int, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "file_path": self.file_path,
            "location_line": self.location_line,
            "function_content": self.function_content,
            "function_content_in_lines": self.function_content_in_lines
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FunctionInfo':
        """从字典数据创建FunctionInfo对象"""
        return FunctionInfo(
            name=data["name"],
            file_path=data["file_path"],
            location_line=data["location_line"],
            function_content=data["function_content"],
            function_content_in_lines=data.get("function_content_in_lines", {})
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, 'FunctionInfo']:
        """从查询结果解析函数信息，返回字典，键为函数名"""
        functions: Dict[str, FunctionInfo] = {}
        for item in result:
            func_name, file_path, location_line = item[0], item[1], item[2]
            function_content, function_content_in_lines = read_struct_with_start_line_from_db(db_path, file_path, location_line, func_name)
            if function_content == "" :
                continue
            functions[func_name] = FunctionInfo(
                name=func_name,
                file_path=file_path,
                location_line=location_line,
                function_content=function_content, 
                function_content_in_lines=function_content_in_lines
            )
        return functions

@dataclass
class StructInfo(QueryInfo):
    """结构体信息数据结构"""
    name: str
    file_path: str
    location_line: int
    struct_content: str
    struct_content_in_lines: Dict[int, str] = field(default_factory=dict)
    members: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "file_path": self.file_path,
            "location_line": self.location_line,
            "struct_content": self.struct_content,
            "struct_content_in_lines": self.struct_content_in_lines,
            "members": self.members
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'StructInfo':
        """从字典数据创建StructInfo对象"""
        return StructInfo(
            name=data["name"],
            file_path=data["file_path"],
            location_line=data["location_line"],
            struct_content=data["struct_content"],
            struct_content_in_lines=data.get("struct_content_in_lines", {}),
            members=data.get("members", {})
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, 'StructInfo']:
        """从查询结果解析结构体信息，返回字典，键为结构体名"""
        structs: Dict[str, StructInfo] = {}
        for item in result:
            struct_name, member_name, member_type, file_path, location_line = (
                item[0], item[1], item[2], item[3], item[4]
            )
            struct_content, struct_content_in_lines = read_struct_with_start_line_from_db(db_path, file_path[1:], location_line, struct_name)
            if struct_content == "" :
                continue
            if struct_name not in structs:
                structs[struct_name] = StructInfo(
                    name=struct_name,
                    file_path=file_path,
                    location_line=location_line,
                    struct_content=struct_content,
                    struct_content_in_lines=struct_content_in_lines,
                    members={}
                )
            structs[struct_name].members[member_name] = member_type
        return structs

@dataclass
class EnumInfo(QueryInfo):
    """枚举信息数据结构"""
    name: str
    value: Any
    typedef: str
    file_path: str
    location_line: int

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "name": self.name,
            "value": self.value,
            "typedef": self.typedef,
            "file_path": self.file_path,
            "location_line": self.location_line
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'EnumInfo':
        """从字典数据创建EnumInfo对象"""
        return EnumInfo(
            name=data["name"],
            value=data["value"],
            typedef=data.get("typedef", ""),
            file_path=data.get("file_path", ""),
            location_line=data.get("location_line", 0)
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, 'EnumInfo']:
        """从查询结果解析枚举信息，返回字典，键为枚举名"""
        enums: Dict[str, EnumInfo] = {}
        for item in result:
            enum_type, enum_name, enum_value, enum_file, enum_startline = item[0], item[1], item[2], item[3], item[4]
            enums[enum_name] = EnumInfo(name=enum_name, value=enum_value, file_path=enum_file, location_line=enum_startline, typedef=enum_type)
        return enums

@dataclass
class FunctionCallInfo(QueryInfo):
    """函数调用信息数据结构"""
    caller_name: str
    callee_name: str
    call_tag: str
    file_path: str
    start_line: int
    call_type: str
    ret_type: str
    start_line_content: str

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "caller_name": self.caller_name,
            "callee_name": self.callee_name,
            "call_tag": self.call_tag,
            "file_path": self.file_path,
            "start_line": self.start_line,
            "call_type": self.call_type,
            "ret_type": self.ret_type,
            "start_line_content": self.start_line_content
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'FunctionCallInfo':
        """从字典数据创建FunctionCallInfo对象"""
        return FunctionCallInfo(
            caller_name=data["caller_name"],
            callee_name=data["callee_name"],
            call_tag=data["call_tag"],
            file_path=data["file_path"],
            start_line=data["start_line"],
            call_type=data["call_type"],
            ret_type=data["ret_type"],
            start_line_content=data["start_line_content"]
        )

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Tuple[Dict[str, List['FunctionCallInfo']], Dict[str, List['FunctionCallInfo']]]:
        """从查询结果解析函数调用信息，返回字典，键为函数名"""
        call_to_dict: Dict[str, List[FunctionCallInfo]] = {}
        call_from_dict: Dict[str, List[FunctionCallInfo]] = {}
        for item in result:
            func_name, callee_name, call_tag, file_path, start_line, call_type, ret_type = item[0], item[1], item[2], item[3], item[4], item[5], item[6]
            call_to_dict.setdefault(func_name, []).append(
                FunctionCallInfo(
                    caller_name=func_name,
                    callee_name=callee_name,
                    call_tag=call_tag,
                    file_path=file_path,
                    start_line=start_line,
                    start_line_content=read_line_from_db(db_path, file_path[1:], start_line),
                    call_type=call_type,
                    ret_type=ret_type
                )
            )
            call_from_dict.setdefault(callee_name, []).append(
                FunctionCallInfo(
                    caller_name=func_name,
                    callee_name=callee_name,
                    call_tag=call_tag,
                    file_path=file_path,
                    start_line=start_line,
                    start_line_content=read_line_from_db(db_path, file_path[1:], start_line),
                    call_type=call_type,
                    ret_type=ret_type
                )
            )
        return call_to_dict, call_from_dict