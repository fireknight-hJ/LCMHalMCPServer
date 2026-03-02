# Builder工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
from tools.builder.proj_builder import build_proj, clear_proj
from tools.collector.collector import get_function_info, get_function_source
from tools.replacer.code_recover import function_recover
from tools.replacer.code_replacer import function_replace
from core.data_manager import data_manager
from utils.replacement_rubric import check_replacement_rubric


def _is_core_function(func_name: str, mmio_info_list: dict) -> bool:
    """Return True if the function is classified as CORE (OS/NVIC/scheduler-critical); CORE must never be replaced."""
    if func_name not in mmio_info_list:
        return False
    classify_res = mmio_info_list[func_name]
    return getattr(classify_res, "function_type", None) == "CORE"


def replace_funcs():
    """替换需要替换的函数"""
    mmio_info_list = data_manager.get_mmio_info_list()
    replacement_updates = data_manager.get_replacement_updates()
    
    # 收集所有要替换的函数列表（CORE 类函数坚决不替换，即使存在 replacement_update）
    all_funcs_to_replace = []
    
    # 首先处理所有在replacement_updates中的函数，但排除 CORE 类
    for func_name, replacement_update in replacement_updates.items():
        if not _is_core_function(func_name, mmio_info_list):
            all_funcs_to_replace.append(func_name)
    
    # 然后处理mmio_info_list中不在replacement_updates中的函数（CORE 的 has_replacement 为 false，自然不会进入）
    for func_name, classify_res in mmio_info_list.items():
        if func_name not in replacement_updates and classify_res.has_replacement:
            all_funcs_to_replace.append(func_name)
    
    # 替换前打印所有要替换的函数
    print(f"\n{'='*60}")
    print(f"[REPLACE] Functions to replace (total: {len(all_funcs_to_replace)}):")
    for i, func_name in enumerate(all_funcs_to_replace, 1):
        print(f"  {i}. {func_name}")
    print(f"{'='*60}\n")
    
    # 执行替换（跳过 CORE 类函数，保留原实现）
    replaced_count = 0
    for func_name, replacement_update in replacement_updates.items():
        if _is_core_function(func_name, mmio_info_list):
            print(f"[REPLACE] Skipping CORE function (no replacement): {func_name}")
            continue
        func_info = get_function_info(globs.db_path, func_name)
        if func_info:
            replace_res = function_replace(func_info, replacement_update.replacement_code)
            if not replace_res:
                print(f"Warning: Failed to replace function {func_name}")
            else:
                replaced_count += 1
        else:
            print(f"Warning: Function {func_name} not found in database")
    
    # 然后处理mmio_info_list中不在replacement_updates中的函数
    for func_name, classify_res in mmio_info_list.items():
        if func_name not in replacement_updates and classify_res.has_replacement:
            func_info = get_function_info(globs.db_path, func_name)
            if func_info:
                replacement_code = classify_res.function_replacement
                replace_res = function_replace(func_info, replacement_code)
                if not replace_res:
                    print(f"Warning: Failed to replace function {func_name}")
                else:
                    replaced_count += 1
            else:
                print(f"Warning: Function {func_name} not found in database")
    
    # 替换后打印所有成功替换的函数
    print(f"\n{'='*60}")
    print(f"[REPLACE] Successfully replaced functions: {replaced_count}/{len(all_funcs_to_replace)}")
    print(f"{'='*60}\n")


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
    # 首先恢复原始文件，确保源文件是干净的原始状态
    recover_funcs()
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
        # 获取 emulate 目录下的 ELF 文件路径（build.sh 生成的）
        elf_path = os.path.join(globs.script_path, "emulate", "output.elf")
        
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
            else:
                print("ELF to BIN conversion failed")
            
            # 无论 ELF 到 BIN 转换是否成功，都更新 syms.yml
            # 因为 syms.yml 的更新依赖于 ELF 文件，而不是 BIN 文件
            try:
                from tools.emulator.conf_generator import extract_syms
                extract_syms()
                print("syms.yml updated successfully after build")
            except Exception as e:
                print(f"Warning: Failed to update syms.yml after build: {e}")
        else:
            print(f"Warning: ELF file not found at {elf_path}")
    except Exception as e:
        print(f"Error processing output files after build: {e}")
        import traceback
        traceback.print_exc()
    
    # 结果输出，添加 stdout/stderr 长度限制，避免 Builder 对话上下文过长导致 API 400
    stdout_limit = 10000
    stderr_limit = 8000
    std_out = build_info.std_out
    std_err = build_info.std_err

    if std_out and len(std_out) > stdout_limit:
        std_out = std_out[:stdout_limit] + f"\n[TRUNCATED] stdout exceeded {stdout_limit} chars. Showing first {stdout_limit} only."
    if std_err and len(std_err) > stderr_limit:
        std_err = std_err[:stderr_limit] + f"\n[TRUNCATED] stderr exceeded {stderr_limit} chars. Use FixFunctionBuildErrors with the specific error lines you need to fix."

    # 编译完成后dump全量信息
    data_manager.dump_full_info()

    return {
        "std_err": std_err,
        "std_out": std_out,
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


def _compile_verify_single_replacement(func_name: str, replace_code: str) -> dict | None:
    """对单个函数的替换做一次“临时落盘 + 全项目编译”验证。
    
    成功时返回 None；失败时返回形如 update_function_replacement 的错误 dict：
      {"ok": False, "reason": "...", "build_stderr": "..."}（build_stderr 仅在编译失败时存在）
    """
    # db_path 为空时直接跳过编译验证（保持原有行为）
    if not globs.db_path:
        return None
    
    func_info = get_function_info(globs.db_path, func_name)
    if not func_info:
        # 找不到函数信息时也不强制失败，而是跳过验证，让上层继续正常落盘
        return None
    
    # 1) 在源文件中临时应用本次替换
    applied = function_replace(func_info, replace_code)
    if not applied:
        return {
            "ok": False,
            "reason": f"Failed to apply replacement into source file for {func_name} during compile verification."
        }
    
    # 2) 运行一次项目构建（使用现有 build.sh/clear.sh 工具链）
    #    这里不修改 replacement_updates，只在工作树里替换这一处代码做验证
    try:
        clear_proj(globs.script_path)
        build_output = build_proj(globs.script_path)
    finally:
        # 3) 无论成败都恢复该文件原始代码，避免污染后续流程
        function_recover(func_info)
    
    if build_output.exit_code != 0:
        # 编译失败，携带 stderr 返回给上层 Agent，用于驱动重新生成函数体
        return {
            "ok": False,
            "reason": "Compile verification failed for replacement.",
            "build_stderr": build_output.std_err,
        }
    
    return None


def verify_replacement(func_name: str, replace_code: str) -> dict:
    """仅验证替换代码（Rubric + 可选编译），不落盘。供 FunctionClassifier 等在图内调用。

    Returns:
        {"pass": True} 或 {"pass": False, "reason": str, "build_stderr": str | None}
    """
    original_code = get_function_source(globs.db_path, func_name) if getattr(globs, "db_path", None) else None
    check_result = check_replacement_rubric(func_name, replace_code, original_code=original_code)
    if not check_result["pass"]:
        return {"pass": False, "reason": check_result["reason"], "build_stderr": None}

    if getattr(globs, "enable_compile_verify", False):
        err = _compile_verify_single_replacement(func_name, replace_code)
        if err is not None:
            return {
                "pass": False,
                "reason": err.get("reason", "Compile verification failed."),
                "build_stderr": err.get("build_stderr"),
            }
    return {"pass": True}


def update_function_replacement(func_name: str, replace_code: str, reason: str) -> dict:
    """更新函数替换代码；落盘前先做 rubric 校验，不通过则返回 ok: false 与 reason，不写入。
    
    Args:
        func_name: 函数名称
        replace_code: 替换代码
        reason: 替换原因
        
    Returns:
        dict: 更新结果。rubric 不通过时返回 {"ok": False, "reason": "..."}；成功时返回 {"ok": True, "function_name": ..., "status": "success"}
    """
    original_code = get_function_source(globs.db_path, func_name) if globs.db_path else None
    check_result = check_replacement_rubric(func_name, replace_code, original_code=original_code)
    if not check_result["pass"]:
        return {"ok": False, "reason": check_result["reason"]}
    
    # 可选：在当前项目环境下对单个函数替换做一次全项目编译验证
    # 目的：尽量在保存 ReplacementUpdate 之前就发现明显的语法/编译错误
    if getattr(globs, "enable_compile_verify", False):
        verify_result = _compile_verify_single_replacement(func_name, replace_code)
        if verify_result is not None:
            return verify_result
    
    # 通过 Rubric（以及可选的编译验证）后，才真正落盘更新
    data_manager.update_function_replacement(func_name, replace_code, reason)
    return {
        "ok": True,
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


def get_replace_func_details_by_function(func_name: str) -> dict:
    """根据函数名获取函数的分析和替换信息（按函数查询版本，更常用）

    Args:
        func_name: 函数名称

    Returns:
        dict: 包含函数分析信息和替换信息的字典
            - mmio_info: 函数的MMIO分析信息（如果有）
            - replacement_update: 函数的替换更新信息（如果有）
    """
    return data_manager.get_function_analysis_and_replacement(func_name)


def get_function_analysis_and_replacement(func_name: str) -> dict:
    """根据函数名获取函数的分析和替换信息（按函数查询版本）

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
    return data_manager.get_function_analysis_and_replacement_formatted_by_function(func_name)


def get_function_analysis_and_replacement_formatted_by_function(func_name: str) -> str:
    """根据函数名获取格式化的函数分析和替换信息（按函数查询版本）

    Args:
        func_name: 函数名称

    Returns:
        str: 格式化的函数分析和替换信息
    """
    return data_manager.get_function_analysis_and_replacement_formatted(func_name)


def get_replace_func_details_by_file(file_path: str) -> dict:
    """根据文件路径获取替换函数详情（包含替换历史信息，重要改进）

    Args:
        file_path: 文件的完整路径

    Returns:
        dict: 替换函数的详细信息
    """
    return data_manager.get_replace_func_details_by_file(file_path)


def build_with_raw() -> dict:
    """不修改任何函数替换，直接编译项目
    
    Returns:
        dict: 构建结果，包含std_err、std_out和exit_code
    """
    # 清理项目
    clear_proj(globs.script_path)
    # 编译项目
    build_info = build_proj(globs.script_path)
    
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
            else:
                print("ELF to BIN conversion failed")
            
            # 无论 ELF 到 BIN 转换是否成功，都更新 syms.yml
            # 因为 syms.yml 的更新依赖于 ELF 文件，而不是 BIN 文件
            try:
                from tools.emulator.conf_generator import extract_syms
                extract_syms()
                print("syms.yml updated successfully after build")
            except Exception as e:
                print(f"Warning: Failed to update syms.yml after build: {e}")
        else:
            print(f"Warning: ELF file not found at {elf_path}")
    except Exception as e:
        print(f"Error processing output files after build: {e}")
        import traceback
        traceback.print_exc()
    
    # 结果输出
    # 编译完成后dump全量信息
    data_manager.dump_full_info()
    
    return {
        "std_err": build_info.std_err,
        "std_out": build_info.std_out,
        "exit_code": build_info.exit_code
    }
