import config.globs as globs

weak_funcdef = """
int __attribute__((noinline, used, __weak__))HAL_BE_return_0(){
    return 0;
}

int __attribute__((noinline, used, __weak__))HAL_BE_return_1(){
    return 1;
}

int __attribute__((noinline, used, __weak__))HAL_BE_Out(int len){
    return len;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_In(void* buf, int len){
    return len;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_ENET_ReadFrame(void* buf, int length){
    return 1;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Write(void* buf, int block_size, int block_num){
    return block_num;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Read(void* buf, int block_size, int block_num){
    return block_num;
}
"""

def src_replace(file_path: str, old_code: str, replace_code: str) -> str:
    """
    替换源文件中的函数实现
    file_path: 源文件路径
    old_code: 要替换的代码
    replace_code: 替换后的代码
    """
    content = ""
    try:
        # 首先尝试UTF-8编码
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        # 如果UTF-8失败，尝试Windows-1252编码（常见的包含特殊字符的编码）
        try:
            with open(file_path, "r", encoding="windows-1252") as f:
                content = f.read()
        except:
            # 最后尝试使用错误处理模式
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
    
    if old_code not in content or old_code == "":
        if old_code == "":
            return ""
        
        import difflib
        import re
        import os
        import time
        
        # 生成diff文件名
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        try:
            func_name = old_code.split('(')[0].split()[-1]
            diff_filename = f"diff_{func_name}_{timestamp}.txt"
        except Exception:
            diff_filename = f"diff_{timestamp}.txt"
        
        # 创建日志目录（如果不存在）
        log_dir = "lcmhal_failcheck_logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        diff_filepath = os.path.join(log_dir, diff_filename)
        
        # 写入diff文件
        with open(diff_filepath, 'w', encoding='utf-8') as diff_file:
            diff_file.write(f"Error: old_code not found in {file_path}\n\n")
            
            # 尝试从old_code中提取函数名
            try:
                func_name = old_code.split('(')[0].split()[-1]
                diff_file.write(f"Looking for function: {func_name}\n\n")
                
                # 在content中查找函数名
                if func_name in content:
                    # 找到函数名附近的内容
                    pos = content.find(func_name)
                    # 向前找函数开始
                    start = max(0, content.rfind('\n', 0, pos))
                    # 向后找函数结束（通过大括号匹配）
                    open_braces = 0
                    end = start
                    found = False
                    
                    for i in range(pos, len(content)):
                        if content[i] == '{':
                            open_braces += 1
                        elif content[i] == '}':
                            open_braces -= 1
                            if open_braces == 0:
                                end = i + 1
                                found = True
                                break
                    
                    if found:
                        # 提取实际的函数代码
                        actual_code = content[start:end].strip()
                        diff_file.write("=== Found similar function in file ===\n")
                        diff_file.write(actual_code)
                        diff_file.write("\n\n")
                        
                        # 生成diff
                        diff_file.write("=== Diff between old_code and actual code ===\n")
                        old_lines = old_code.splitlines()
                        actual_lines = actual_code.splitlines()
                        
                        # 使用unified_diff生成差异
                        diff = difflib.unified_diff(
                            old_lines,
                            actual_lines,
                            fromfile='old_code',
                            tofile='actual_code',
                            lineterm=''
                        )
                        
                        # 写入diff
                        diff_str = '\n'.join(diff)
                        if diff_str:
                            diff_file.write(diff_str)
                        else:
                            diff_file.write("No visible diff, check whitespace and line endings")
                    else:
                        diff_file.write(f"Could not find complete function definition for {func_name}\n")
                else:
                    diff_file.write(f"Function name {func_name} not found in content\n")
            except Exception as e:
                diff_file.write(f"Error extracting function name: {e}\n")
            
            # 如果找不到函数名，比较整个old_code和content的前几个字符
            diff_file.write("\n=== First 200 chars comparison ===\n")
            old_prefix = old_code[:200]
            content_prefix = content[:200]
            
            old_lines = old_prefix.splitlines()
            content_lines = content_prefix.splitlines()
            
            diff = difflib.unified_diff(
                old_lines,
                content_lines,
                fromfile='old_code_prefix',
                tofile='content_prefix',
                lineterm=''
            )
            
            diff_str = '\n'.join(diff)
            if diff_str:
                diff_file.write(diff_str)
            else:
                diff_file.write("No diff in first 200 chars")
        
        # 只打印错误提示和diff文件位置
        print(f"Error: old_code not found in {file_path}")
        print(f"Diff information saved to: {diff_filepath}")
        
        return ""
    # 检查是否已经包含了弱函数定义，没有则添加（防止编译错误）
    if weak_funcdef not in content:
        content = weak_funcdef + content
    content = content.replace(old_code, replace_code)
    # print(f"Modifying src file {file_path}")
    
    # 写回文件时使用UTF-8编码
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return content

def src_insert(file_path: str, insert_code: str, start_line: int = -1) -> str:
    """
    在源文件中插入代码
    file_path: 源文件路径
    insert_code: 要插入的代码
    start_line: 插入的起始行号，-1表示在文件末尾插入
    """
    content = ""
    try:
        # 首先尝试UTF-8编码
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.readlines()
    except UnicodeDecodeError:
        # 如果UTF-8失败，尝试Windows-1252编码
        try:
            with open(file_path, "r", encoding="windows-1252") as f:
                content = f.readlines()
        except:
            # 最后尝试使用错误处理模式
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.readlines()
    
    if start_line == -1:
        content.append(insert_code)
    else:
        content.insert(start_line, insert_code)
    
    # 写回文件时使用UTF-8编码
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    return content
    
def file_convert_proj2src(file_path: str) -> str:
    """
    将项目路径转换为源文件路径
    file_path: 项目路径
    (解决DB中路径与实际源文件路径不同的问题，通过globs.proj_path和globs.src_path转换)
    """
    if globs.proj_path != globs.src_path:
        # 项目路径和源文件路径不同时，需要转换
        file_path = file_path.replace(globs.proj_path, globs.src_path.replace(" ", "\\ "))
        return file_path
    else:
        return file_path