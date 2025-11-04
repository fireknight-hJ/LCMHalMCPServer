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

"""

def src_replace(file_path: str, old_code: str, replace_code: str) -> str:
    """
    替换源文件中的函数实现
    file_path: 源文件路径
    old_code: 要替换的代码
    replace_code: 替换后的代码
    """
    content = ""
    with open(file_path, "r") as f:
        content = f.read()
        if old_code not in content or old_code == "":
            # print(f"Error: {old_code} not found in {file_path}")
            return ""
        # 检查是否已经包含了弱函数定义，没有则添加（防止编译错误）
        if weak_funcdef not in content:
            content = weak_funcdef + content
        content = content.replace(old_code, replace_code)
        # print(f"Modifying src file {file_path}")
    with open(file_path, "w") as f:
        f.write(content)
    return content

def src_insert(file_path: str, insert_code: str, start_line: int = -1) -> str:
    """
    在源文件中插入代码
    file_path: 源文件路径
    insert_code: 要插入的代码
    start_line: 插入的起始行号，-1表示在文件末尾插入
    """
    with open(file_path, "r") as f:
        content = f.readlines()
        if start_line == -1:
            content.append(insert_code)
        else:
            content.insert(start_line, insert_code)
        with open(file_path, "w") as f:
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