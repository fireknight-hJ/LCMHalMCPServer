# Emulator工具的核心功能模块
# 提供直接调用的函数接口，避免通过MCP客户端启动新进程
import config.globs as globs
import os
import re
from tools.emulator.emulate_runner import run_emulator
from tools.emulator.conf_generator import extract_syms, generate_emulator_configs


def emulate_proj() -> dict:
    """运行模拟器，返回模拟器结果
    
    Returns:
        dict: 模拟结果，包含std_out、std_err、exit_code和success判断
    """
    # 每次emulate前重新生成syms.yml配置文件，因为重新build后符号表会变化
    extract_syms()
    # 每次emulate前重新生成配置文件，因为重新build后配置文件会变化（entry_point等）
    generate_emulator_configs()
    # 运行模拟器
    ret = run_emulator()
    
    # 将模拟器 stdout/stderr 持久化到 debug_output，便于排查 UC_ERR_READ_UNMAPPED 等错误
    debug_out_dir = os.path.join(globs.script_path, "emulate", "debug_output")
    os.makedirs(debug_out_dir, exist_ok=True)
    for name, data in [("stdout.txt", ret.stdout), ("stderr.txt", ret.stderr)]:
        path = os.path.join(debug_out_dir, name)
        text = data.decode("utf-8", errors="replace") if isinstance(data, bytes) else (data or "")
        with open(path, "w") as f:
            f.write(text)
    
    # 检查 lcmhal.txt 判断是否有死循环
    lcmhal_path = os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt")
    has_loop = False
    if os.path.exists(lcmhal_path):
        with open(lcmhal_path, 'r') as f:
            content = f.read()
            if 'exceptional loop' in content:
                has_loop = True
    
    # 判断是否成功：exit_code == 0 且没有死循环
    success = (ret.returncode == 0 and not has_loop)
    
    return {
        "std_out": ret.stdout,
        "std_err": ret.stderr,
        "exit_code": ret.returncode,
        "success": success,
        "has_exceptional_loop": has_loop
    }


def ensure_emulator_output_exists():
    """确保模拟器输出文件存在，如果不存在或ELF文件比输出文件新则运行模拟器生成
    """
    # 检查两个关键文件是否存在
    lcmhal_file = os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt")
    function_file = os.path.join(globs.script_path, "emulate/debug_output/function.txt")
    elf_file = os.path.join(globs.script_path, "emulate/output.elf")
    
    # 获取 ELF 文件的修改时间（如果存在）
    elf_mtime = 0
    if os.path.exists(elf_file):
        elf_mtime = os.path.getmtime(elf_file)
    
    # 检查输出文件是否存在且比 ELF 文件旧
    needs_rerun = False
    if not os.path.exists(lcmhal_file) or not os.path.exists(function_file):
        needs_rerun = True
    elif elf_mtime > 0:
        # ELF 文件比输出文件新，需要重新运行
        lcmhal_mtime = os.path.getmtime(lcmhal_file)
        if elf_mtime > lcmhal_mtime:
            needs_rerun = True
    
    if needs_rerun:
        # 如果需要重新运行，先删除旧的输出文件
        debug_output_dir = os.path.join(globs.script_path, "emulate/debug_output")
        if os.path.exists(debug_output_dir):
            for filename in ['lcmhal.txt', 'function.txt', 'debug.txt']:
                filepath = os.path.join(debug_output_dir, filename)
                if os.path.exists(filepath):
                    os.remove(filepath)
        # 运行模拟器生成新输出
        print("模拟器输出文件不存在或已过期，正在运行模拟器生成...")
        emulate_proj()
        print("模拟器运行完成，输出文件已生成")


def mmio_function_emulate_info() -> str:
    """获取所有MMIO函数的模拟器结果信息
    
    Returns:
        str: 模拟器输出的MMIO函数信息
    """
    # 确保模拟器输出文件存在
    ensure_emulator_output_exists()
    
    with open(os.path.join(globs.script_path, "emulate/debug_output/lcmhal.txt"), "r") as f:
        data = "".join(f.readlines())
    return data


def function_calls_emulate_info(max_loop_lines: int = 5, max_output_lines: int = 1000) -> str:
    """获取所有函数调用栈的模拟器结果信息，并压缩连续重复的行和多行循环
    
    Args:
        max_loop_lines: 最大检测循环行数，默认为5
        max_output_lines: 最大输出行数，默认为1000。如果超出，只保留末尾的行数
    
    Returns:
        str: 模拟器输出的函数调用栈信息（已压缩连续重复行和多行循环）
    """
    # 确保模拟器输出文件存在
    ensure_emulator_output_exists()
    
    # 定义正则表达式模式：捕获序号和核心内容
    # 模式匹配：空格 + 序号 + 空格 + 核心内容
    pattern = re.compile(r'\s+(\d+)\s+(.+)')
    
    # 读取所有行并解析
    parsed_lines = []
    with open(os.path.join(globs.script_path, "emulate/debug_output/function.txt"), "r") as f:
        for line in f:
            match = pattern.match(line)
            if match:
                seq = int(match.group(1))
                core = match.group(2)
                parsed_lines.append((seq, core))
    
    if not parsed_lines:
        return ""
    
    compressed_lines = []
    i = 0
    n = len(parsed_lines)
    
    while i < n:
        # 首先尝试检测多行循环
        loop_detected = False
        
        # 尝试不同长度的循环检测（从2到max_loop_lines）
        for loop_length in range(2, min(max_loop_lines, n - i) + 1):
            # 检查是否存在循环
            is_loop = True
            for j in range(loop_length):
                if i + loop_length + j >= n:
                    is_loop = False
                    break
                if parsed_lines[i + j][1] != parsed_lines[i + loop_length + j][1]:
                    is_loop = False
                    break
            
            if is_loop:
                # 检测到循环，计算循环次数
                loop_count = 2  # 至少重复一次
                while i + loop_count * loop_length < n:
                    all_match = True
                    for j in range(loop_length):
                        if parsed_lines[i + j][1] != parsed_lines[i + loop_count * loop_length + j][1]:
                            all_match = False
                            break
                    if all_match:
                        loop_count += 1
                    else:
                        break
                
                # 添加循环信息
                start_seq = parsed_lines[i][0]
                end_seq = parsed_lines[i + (loop_count - 1) * loop_length + loop_length - 1][0]
                compressed_lines.append(f"\t\t[LOOP] {start_seq}-{end_seq} (重复{loop_count}次)")
                for j in range(loop_length):
                    seq, core = parsed_lines[i + j]
                    compressed_lines.append(f"\t\t  {seq} {core}")
                
                # 跳过循环的所有行
                i += loop_count * loop_length
                loop_detected = True
                break
        
        if not loop_detected:
            # 没有检测到循环，使用原有的单行重复检测
            start_seq = parsed_lines[i][0]
            core = parsed_lines[i][1]
            j = i + 1
            
            # 查找连续重复的行
            while j < n and parsed_lines[j][1] == core:
                j += 1
            
            end_seq = parsed_lines[j - 1][0]
            
            if j - i == 1:
                # 只有一行，直接添加
                compressed_lines.append(f"\t\t{start_seq} {core}")
            else:
                # 多行连续重复，显示范围
                compressed_lines.append(f"\t\t{start_seq}-{end_seq} {core} (重复{j - i}次)")
            
            i = j
    
    # 控制窗口大小，超出时只保留末尾的行数
    if len(compressed_lines) > max_output_lines:
        # 只保留末尾的max_output_lines行
        compressed_lines = compressed_lines[-max_output_lines:]
        # 在开头添加提示信息
        compressed_lines.insert(0, f"\t\t[TRUNCATED] Output exceeded {max_output_lines} lines. Showing last {max_output_lines} lines only.")
    
    return "\n".join(compressed_lines)
