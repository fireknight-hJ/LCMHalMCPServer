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

def read_file_from_db_zip(db_path: str, file_path: str) -> str:
    """Reads a specific file from the src.zip inside a CodeQL database directory."""
    if file_path.startswith("/"):
        file_path = file_path[1:]
    db_path_resolved = Path(db_path).resolve()
    if not db_path_resolved.exists():
        return f"Database path does not exist: {db_path}"

    source_zip = db_path_resolved / "src.zip"
    if not source_zip.exists():
        return f"Missing required src.zip in: {db_path}"

    try:
        with zipfile.ZipFile(source_zip, 'r') as zip_ref:
            with zip_ref.open(file_path) as file:
                return file.read().decode('utf-8')
    except KeyError:
        return f"File {file_path} not found in src.zip"
    except Exception as e:
        return f"Error reading file {file_path} from src.zip: {e}"

def read_line_from_db(db_path: str, file_path: str, line: int) -> str:
    """Reads a specific line from a file in the src.zip inside a CodeQL database directory."""
    content = read_file_from_db_zip(db_path, file_path)
    lines = content.splitlines()
    if line < 1 or line > len(lines):
        return f"Invalid line number {line} for file {file_path}"
    return lines[line-1]

def read_struct_with_start_line_from_db(db_path: str, file_path: str, start_line: int, struct_or_func_name: str = None) -> Tuple[str, Dict[int, str]]:
    """Reads a struct or function definition from the start line of a file in the src.zip inside a CodeQL database directory."""
    content = read_file_from_db_zip(db_path, file_path)
    lines = content.splitlines()
    struct_content = read_struct_or_func_from_lines(lines, start_line)
    # 如果指定了struct_or_func_name，则检查其是否在struct_content中
    if struct_or_func_name != None and struct_or_func_name not in struct_content:
        return ""
    return struct_content


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