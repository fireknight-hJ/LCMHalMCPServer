from dataclasses import dataclass, field
from utils import read_struct_with_start_line_from_db
from typing import Any, Dict, List

# common infos collector
@dataclass
class FunctionInfo:
    """函数信息数据结构"""
    name: str
    file_path: str
    location_line: int
    function_content: str

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, 'FunctionInfo']:
        """从查询结果解析函数信息，返回字典，键为函数名"""
        functions: Dict[str, FunctionInfo] = {}
        for item in result:
            func_name, file_path, location_line = item[0], item[1], item[2]
            function_content = read_struct_with_start_line_from_db(db_path, file_path[1:], location_line, func_name)
            if function_content == "" :
                continue
            functions[func_name] = FunctionInfo(
                name=func_name,
                file_path=file_path,
                location_line=location_line,
                function_content=function_content
            )
        return functions

@dataclass
class StructInfo:
    """结构体信息数据结构"""
    name: str
    file_path: str
    location_line: int
    struct_content: str
    members: Dict[str, str] = field(default_factory=dict)

    @staticmethod
    def resolve_from_query_result(db_path: str, result: List[Dict[str, Any]]) -> Dict[str, 'StructInfo']:
        """从查询结果解析结构体信息，返回字典，键为结构体名"""
        structs: Dict[str, StructInfo] = {}
        for item in result:
            struct_name, member_name, member_type, file_path, location_line = (
                item[0], item[1], item[2], item[3], item[4]
            )
            struct_content = read_struct_with_start_line_from_db(db_path, file_path[1:], location_line, struct_name)
            if struct_content == "" :
                continue
            structs[struct_name] = StructInfo(
                name=struct_name,
                file_path=file_path,
                location_line=location_line,
                struct_content=struct_content,
                members={}
            )
            structs[struct_name].members[member_name] = member_type

@dataclass
class EnumInfo:
    """枚举信息数据结构"""
    name: str
    value: Any

    @staticmethod
    def resolve_from_query_result(result: List[Dict[str, Any]]) -> Dict[str, 'EnumInfo']:
        """从查询结果解析枚举信息，返回字典，键为枚举名"""
        enums: Dict[str, EnumInfo] = {}
        for item in result:
            enum_name, enum_value = item[0], item[1]
            enums[enum_name] = EnumInfo(name=enum_name, value=enum_value)
        return enums