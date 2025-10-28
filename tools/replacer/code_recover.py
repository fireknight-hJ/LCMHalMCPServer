import config.globs as globs
from utils.db_file import read_file_from_db_zip


def recover_code_file(code_path: str, proj_path: tuple[str, str] = None) -> bool:
    """
    搜索对应的源文件路径，根据codeql的DB中的对应文件恢复原始代码
    :param code_path: 代码文件路径
    :param proj_path: 项目目录路径 (可能存在项目目录被移动到其他位置), 元组中的第一个元素为项目DB存储的路径, 第二个元素为项目实际路径
    :return: 恢复后的代码字符串
    """
    # 搜索对应的源文件路径
    db_path = globs.db_path
    file_content, ok = read_file_from_db_zip(db_path, code_path)
    # 替换项目DB存储路径为项目实际路径
    code_file_path = code_path
    if proj_path is not None and len(proj_path) == 2:
        code_file_path = code_path.replace(proj_path[0], proj_path[1])
    else:
        code_file_path = code_path
    if not ok or file_content is None or len(file_content) == 0:
        return False
    # 恢复原始代码
    print(file_content)
    with open(code_file_path, 'wb') as f:
        f.write(file_content.encode('utf-8'))
    return True

def batch_recover_code_files(code_paths: list[str], proj_path: tuple[str, str] = None) -> bool:
    """
    批量恢复代码文件
    :param code_paths: 代码文件路径列表
    :param proj_path: 项目目录路径 (可能存在项目目录被移动到其他位置), 元组中的第一个元素为项目DB存储的路径, 第二个元素为项目实际路径
    :return: 是否所有文件都恢复成功
    """
    for code_path in code_paths:
        if not recover_code_file(code_path, proj_path):
            return False
    return True

if __name__ == "__main__":
    file_paths = [
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/system_stm32f7xx.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/ethernetif.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/stm32f7xx_hal_timebase_tim.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/main.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/app_ethernet.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/s5k5cag_RGB888.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/stm32f769i_camera.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Src/stm32f7xx_it.c",
        "/home/haojie/posixGen_Demos/LwIP_StreamingServer/Utilities/Log/lcd_log.c"
    ]
    globs.db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer"
    for file_path in file_paths:
        if recover_code_file(file_path,
            ("/home/haojie/posixGen_Demos/LwIP_StreamingServer",
             "/Users/jie/Documents/posixGen_Demos-main/LwIP_StreamingServer")
        ):
            print(f"Recover {file_path} done.")
        else:
            print(f"Recover {file_path} failed.")
    

    

    