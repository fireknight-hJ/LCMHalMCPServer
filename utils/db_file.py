# 读取 codeql db 里面的src.zip中的文件内容

import zipfile
from pathlib import Path
from typing import Tuple, Dict, Any, List

MAX_STRUCT_SIZE = 0x100000  # 根据需要设置最大结构体大小

def list_files_in_db_zip(db_path: str) -> list:
    """Lists all files in the src.zip inside a CodeQL database directory."""
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}"

    try:
        with zipfile.ZipFile(source_zip, 'r') as zip_ref:
            return zip_ref.namelist()
    except Exception as e:
        return f"Error reading src.zip: {e}"

def read_file_from_db_zip(db_path: str, file_path: str) -> Tuple[str, bool]:
    """Reads a specific file from the src.zip inside a CodeQL database directory."""
    if file_path.startswith("/"):
        file_path = file_path[1:]
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}", False

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}", False

    try:
        with zipfile.ZipFile(source_zip, 'r') as zip_ref:
            with zip_ref.open(file_path) as file:
                return file.read().decode('utf-8'), True
    except KeyError:
        return f"File {file_path} not found in src.zip", False
    except Exception as e:
        return f"Error reading file {file_path} from src.zip: {e}", False

def read_line_from_db(db_path: str, file_path: str, line: int) -> str:
    """Reads a specific line from a file in the src.zip inside a CodeQL database directory."""
    content = read_file_from_db_zip(db_path, file_path)
    lines, success = content
    lines = lines.splitlines()
    if not success:
        return f"Error reading file {file_path} from src.zip: {lines}"
    if line < 1 or line > len(lines):
        return f"Invalid line number {line} for file {file_path}"
    return lines[line-1]

def read_struct_with_start_line_from_db(db_path: str, file_path: str, start_line: int, struct_or_func_name: str = None) -> Tuple[str, Dict[int, str]]:
    """Reads a struct or function definition from the start line of a file in the src.zip inside a CodeQL database directory."""
    content, success = read_file_from_db_zip(db_path, file_path)
    if not success:
        return f"Error reading file {file_path} from src.zip: {content}", {}
    lines = content.splitlines()
    struct_content, struct_content_in_lines = read_struct_or_func_from_lines(lines, start_line)
    # 如果指定了struct_or_func_name，则检查其是否在struct_content中
    if struct_or_func_name != None and struct_or_func_name not in struct_content:
        return "", {}
    return struct_content, struct_content_in_lines


def read_struct_or_func_from_lines(lines: list, start_line: int) -> Tuple[str, Dict[int, str]]:
    """Reads a struct or function definition from the start line of a file in the src.zip inside a CodeQL database directory."""
    current_comment = ""
    in_comment_block = False
    if start_line < 1 or start_line > len(lines):
        print("Invalid start-line number, may be different definition.")
        return "", {}
    # 跳转到结构体定义的起始行并存储最近的注释
    for i in range(1, start_line):
        line = lines[i-1].strip()
        # 检查是否在注释中
        if "/*" in line:
            if in_comment_block == False:
                current_comment = ""
            in_comment_block = True # 开始收集当前注释

        if in_comment_block:
            current_comment += line + "\n"  # 持续收集注释
            if "*/" in line:
                in_comment_block = False  # 结束当前注释
                # 此时，current_comment 包含了最新的注释内容
    
    # 读取结构体定义
    brace_count = 0  # 大括号计数器
    # pre_brace_count = 0 # 小括号计数器
    content_length = 0
    line_cnt = 0
    in_content = False  # 指示
    struct_content = ""
    struct_content_in_lines = {}
    
    for line in lines[start_line-1:]:
        # # 解决pre_brace_count的问题
        # if in_content == False:
        #     pre_brace_count += line.count('(')
        #     pre_brace_count -= line.count(')')
        #     if pre_brace_count == 0:
        #         in_content = True
        
        # 寻找大括号
        brace_count += line.count('{')
        brace_count -= line.count('}')

        if brace_count > 0:
            in_content = True
        
        # 检查是否超过了全局数组的大小
        if content_length + len(line) < MAX_STRUCT_SIZE:
            struct_content += line + "\n"
            struct_content_in_lines[line_cnt+start_line] = line
            content_length += len(line)
        else:
            print("Struct definition exceeds max size.")
            break

        if brace_count == 0 and in_content == True:
            if line_cnt <= 2:
                line_cnt += 1
                continue
            break
        
        # 小于0绝对是异常情况
        if brace_count < 0:
            line_cnt = 1
            break
        line_cnt += 1
    # 检查是line_cnt是否为1，若为1则说明结构体定义不存在，抛出异常
    if line_cnt <= 2:
        return "", {}
    # 合并最近的注释和结构体定义
    return current_comment + struct_content, struct_content_in_lines

def get_zip_tree_structure(zip_path, indent='    ', max_level=None):
    """
    生成ZIP文件的树状目录结构字符串
    
    参数:
        zip_path: ZIP文件的路径
        indent: 每一级目录的缩进字符串
        max_level: 最大显示层级，None表示显示所有层级
    
    返回:
        tree_str: 树状结构字符串
    """
    tree_lines = []  # 存储每一行的字符串
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            # 获取ZIP内所有文件和目录的路径列表[2,3](@ref)
            namelist = zf.namelist()
            
            if not namelist:
                return f"{zip_path}/\n(空压缩文件)"
            
            # 使用字典构建前缀树来表示目录结构[1](@ref)
            tree = {}
            
            for name in namelist:
                # 分割路径为组成部分
                parts = name.rstrip('/').split('/')
                if not parts or not parts[0]:
                    continue
                    
                current = tree
                # 逐级构建树结构
                for i, part in enumerate(parts):
                    is_last_component = (i == len(parts) - 1)
                    if part not in current:
                        # 标记是否为文件（路径的最后一部分且不以'/'结尾）
                        current[part] = {
                            'is_file': is_last_component and not name.endswith('/'), 
                            'children': {}
                        }
                    current = current[part]['children']
            
            def build_tree_node(node, prefix='', level=0):
                """递归构建树节点字符串"""
                if max_level is not None and level > max_level:
                    return []
                    
                node_lines = []
                keys = list(node.keys())
                
                for i, key in enumerate(keys):
                    is_last = (i == len(keys) - 1)
                    is_file = node[key]['is_file']
                    
                    # 当前节点的连接符
                    connector = '└── ' if is_last else '├── '
                    line = f"{prefix}{connector}{key}{'' if is_file else '/'}"
                    node_lines.append(line)
                    
                    # 为下一级节点计算新的前缀
                    new_prefix = prefix + ('    ' if is_last else '│   ')
                    
                    # 递归构建子节点
                    child_lines = build_tree_node(node[key]['children'], new_prefix, level + 1)
                    node_lines.extend(child_lines)
                
                return node_lines
            
            # 构建完整的树结构
            tree_lines.append(f"{zip_path}/")
            tree_lines.extend(build_tree_node(tree))
            
    except zipfile.BadZipFile:
        return f"错误: {zip_path} 不是一个有效的ZIP文件"
    except FileNotFoundError:
        return f"错误: 找不到文件 {zip_path}"
    except Exception as e:
        return f"错误: 处理ZIP文件时发生异常 - {str(e)}"
    
    return '\n'.join(tree_lines)

def tree_file_from_db_zip(db_path):
    """
    从数据库zip文件中提取树状目录结构字符串
    
    参数:
        db_path: 数据库zip文件的路径
    
    返回:
        tree_str: 树状结构字符串
    """
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}"

    return get_zip_tree_structure(source_zip)

if __name__ == "__main__":
    # Example usage
    db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    file_path = "home/haojie/posixGen_Demos/LwIP_StreamingServer/Drivers/STM32F7xx_HAL_Driver/Src/stm32f7xx_hal_eth.c"
    # func_name = "HAL_ETH_RegisterCallback"
    func_name = "ETH_HandleTypeDef"
    start_line = 507
    # 列出 zip 里面的文件
    files = list_files_in_db_zip(db_path)
    # print(files)
    # 尝试查找 zip 里面的文件
    content = read_file_from_db_zip(db_path, file_path)
    # print(content)
    # 读取结构体定义
    struct_content = read_struct_with_start_line_from_db(db_path, file_path, start_line, func_name)
    print(struct_content)
    # 从 zip 里面提取树状目录结构
    tree = tree_file_from_db_zip(db_path)
    print(tree)