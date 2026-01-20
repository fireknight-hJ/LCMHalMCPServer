# Builder工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
from tools.builder.proj_builder import build_proj, clear_proj
from tools.collector.collector import get_function_info
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace
from core.data_manager import data_manager


def replace_funcs():
    """替换需要替换的函数"""
    mmio_info_list = data_manager.get_mmio_info_list()
    replacement_updates = data_manager.get_replacement_updates()
    
    # 首先处理所有在replacement_updates中的函数，确保它们都被替换
    for func_name, replacement_update in replacement_updates.items():
        func_info = get_function_info(globs.db_path, func_name)
        if func_info:
            replace_res = function_replace(func_info, replacement_update.replacement_code)
            if not replace_res:
                print(f"Warning: Failed to replace function {func_name}")
        else:
            print(f"Warning: Function {func_name} not found in database")
    
    # 然后处理mmio_info_list中不在replacement_updates中的函数
    for func_name, classify_res in mmio_info_list.items():
        if func_name not in replacement_updates and classify_res.has_replacement:
            func_info = get_function_info(globs.db_path, func_name)
            if func_info:
                replace_res = function_replace(func_info, classify_res.function_replacement)
                if not replace_res:
                    print(f"Warning: Failed to replace function {func_name}")
            else:
                print(f"Warning: Function {func_name} not found in database")


def recover_funcs():
    """恢复被替换的函数"""
    mmio_info_list = data_manager.get_mmio_info_list()
    replacement_updates = data_manager.get_replacement_updates()
    
    # 收集所有需要复原的文件路径，确保每个文件只被复原一次
    files_to_recover = set()
    
    # 从mmio_info_list中收集文件路径
    for func_name, classify_res in mmio_info_list.items():
        if classify_res.has_replacement:
            func_info = get_function_info(globs.db_path, func_name)
            if func_info:
                files_to_recover.add(func_info.file_path)
    
    # 从replacement_updates中收集文件路径
    for func_name in replacement_updates.keys():
        func_info = get_function_info(globs.db_path, func_name)
        if func_info:
            files_to_recover.add(func_info.file_path)
    
    # 复原所有收集到的文件
    for file_path in files_to_recover:
        from tools.replacer.code_recover import recover_code_file
        recover_res = recover_code_file(file_path)


def elf_to_bin(elf_path: str, bin_path: str) -> bool:
    """将ELF文件转换为BIN文件
    
    Args:
        elf_path: ELF文件路径
        bin_path: BIN文件输出路径
        
    Returns:
        bool: 转换是否成功
    """
    import subprocess
    import os
    
    try:
        # 检查ELF文件是否存在
        if not os.path.exists(elf_path):
            print(f"Error: ELF file not found at {elf_path}")
            return False
        
        # 检查输出目录是否存在，如果不存在则创建
        bin_dir = os.path.dirname(bin_path)
        if bin_dir and not os.path.exists(bin_dir):
            os.makedirs(bin_dir, exist_ok=True)
            print(f"Created directory: {bin_dir}")
        
        # 检查arm-none-eabi-objcopy工具是否可用
        try:
            subprocess.run(
                ["arm-none-eabi-objcopy", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print("Error: arm-none-eabi-objcopy not found in PATH")
            return False
        
        # 使用arm-none-eabi-objcopy工具将ELF转换为BIN
        print(f"Converting {elf_path} to {bin_path}...")
        result = subprocess.run(
            ["arm-none-eabi-objcopy", "-O", "binary", elf_path, bin_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            # 验证输出文件是否创建成功
            if os.path.exists(bin_path):
                print(f"Successfully converted {elf_path} to {bin_path}")
                print(f"Output file size: {os.path.getsize(bin_path)} bytes")
                return True
            else:
                print(f"Error: Conversion succeeded but output file {bin_path} not found")
                return False
        else:
            print(f"Failed to convert {elf_path} to {bin_path}")
            print(f"Return code: {result.returncode}")
            if result.stdout:
                print(f"Stdout: {result.stdout}")
            if result.stderr:
                print(f"Stderr: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error converting {elf_path} to {bin_path}: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def build_project() -> dict:
    """构建项目
    
    Returns:
        dict: 构建结果，包含std_err和exit_code
    """
    # 替换文件
    replace_funcs()
    # 编译项目
    clear_proj(globs.script_path)
    build_info = build_proj(globs.script_path)
    # 项目复原
    recover_funcs()
    
    # 构建完成后处理输出文件
    try:
        import os
        # 获取脚本目录下的ELF文件路径（build.sh生成的）
        elf_path = os.path.join(globs.script_path, "output.elf")
        
        if os.path.exists(elf_path):
            print(f"ELF file found at: {elf_path}")
            
            # 构建完成后先将ELF转换为BIN文件
            bin_path = os.path.join(globs.script_path, "emulate", "output.bin")
            print(f"Attempting to convert ELF to BIN: {bin_path}")
            
            # 检查是否已经存在旧的BIN文件，如果存在则删除
            if os.path.exists(bin_path):
                print(f"Removing old BIN file: {bin_path}")
                os.remove(bin_path)
            
            # 转换ELF文件为BIN文件
            if elf_to_bin(elf_path, bin_path):
                print("ELF to BIN conversion successful")
                
                # 然后再更新syms.yml，确保符号表信息是最新的
                try:
                    from tools.emulator.conf_generator import extract_syms
                    extract_syms()
                    print("syms.yml updated successfully after build")
                except Exception as e:
                    print(f"Warning: Failed to update syms.yml after build: {e}")
            else:
                print("ELF to BIN conversion failed")
        else:
            print(f"Warning: ELF file not found at {elf_path}")
    except Exception as e:
        print(f"Error processing output files after build: {e}")
        import traceback
        traceback.print_exc()
    
    # 结果输出
    return {
        "std_err": build_info.std_err,
        "std_out": build_info.std_out,
        "exit_code": build_info.exit_code
    }


def get_replace_func_details_by_file(file_path: str) -> dict:
    """根据文件路径获取替换函数详情
    
    Args:
        file_path: 文件的完整路径
        
    Returns:
        dict: 替换函数的详细信息
    """
    return data_manager.get_replace_func_details_by_file(file_path)


def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """更新函数替换代码
    
    Args:
        func_name: 函数名称
        replace_code: 替换代码
        reason: 替换原因
        
    Returns:
        dict: 更新结果
    """
    if not data_manager.update_function_replacement(func_name, replace_code, reason):
        return {"error": f"Function {func_name} not found in MMIO function list."}
    
    return {
        "function_name": func_name,
        "status": "success"
    }


async def init_builder():
    """初始化builder工具
    
    加载MMIO函数信息
    """
    # 加载MMIO函数信息
    await data_manager.load_mmio_functions()


def get_function_analysis_and_replacement(func_name: str) -> dict:
    """根据函数名获取函数的分析和替换信息
    
    Args:
        func_name: 函数名称
        
    Returns:
        dict: 包含函数分析信息和替换信息的字典
            - mmio_info: 函数的MMIO分析信息
            - replacement_update: 函数的替换更新信息（如果有）
    """
    return data_manager.get_function_analysis_and_replacement(func_name)


def get_function_analysis_and_replacement_formatted(func_name: str) -> str:
    """根据函数名获取格式化的函数分析和替换信息（文本格式，便于大模型理解）
    
    Args:
        func_name: 函数名称
        
    Returns:
        str: 格式化的函数分析和替换信息
    """
    return data_manager.get_function_analysis_and_replacement_formatted(func_name)
