import config.globs as globs
from utils.db_file import read_file_from_db_zip


def recover_code_file(code_path: str) -> bool:
    """
    搜索对应的源文件路径，根据codeql的DB中的对应文件恢复原始代码
    :param code_path: 代码文件路径
    :return: 恢复后的代码字符串
    """
    # 搜索对应的源文件路径
    db_path = globs.db_path
    file_content, ok = read_file_from_db_zip(db_path, code_path)
    if not ok or file_content is None or len(file_content) == 0:
        return False
    # 恢复原始代码
    print(file_content)
    with open(code_path, 'wb') as f:
        f.write(file_content.encode('utf-8'))
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
    for file_path in file_paths:
        recover_code_file(file_path)
        print(f"Recover {file_path} done.")
    

    

    