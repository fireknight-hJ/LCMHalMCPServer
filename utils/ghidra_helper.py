#!/usr/bin/env python3

import subprocess
import tempfile
import os

def analyze_with_ghidra_headless(binary_path, pc_address):
    """
    使用Ghidra headless模式分析程序
    """
    # Ghidra安装路径（需要根据你的安装位置修改）
    GHIDRA_PATH = "/path/to/ghidra"
    GHIDRA_SCRIPT = """
import sys
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

def decompile_at_address(program, address_str):
    decompiler = DecompInterface()
    decompiler.openProgram(program)
    
    address = program.getAddressFactory().getAddress(address_str)
    function_manager = program.getFunctionManager()
    function = function_manager.getFunctionContaining(address)
    
    if function is None:
        print("No function found at address: " + address_str)
        return None
    
    results = decompiler.decompileFunction(function, 60, ConsoleTaskMonitor())
    if results.isCompleted():
        decompiled = results.getDecompiledFunction()
        return decompiled.getC() if decompiled else None
    return None

# 主执行逻辑
current_program = getCurrentProgram()
if current_program:
    code = decompile_at_address(current_program, "{}")
    if code:
        print("DECOMPILED_CODE_START")
        print(code)
        print("DECOMPILED_CODE_END")
""".format(pc_address)

    # 创建临时脚本文件
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(GHIDRA_SCRIPT)
        script_path = f.name

    try:
        # 构建Ghidra命令
        cmd = [
            os.path.join(GHIDRA_PATH, "support/analyzeHeadless"),
            tempfile.gettempdir(),  # 临时项目目录
            "temp_project",         # 项目名称
            "-import", binary_path, # 要分析的可执行文件
            "-postScript", script_path,
            "-deleteProject"        # 分析完成后删除项目
        ]
        
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # 提取反编译代码
        output = result.stdout
        if "DECOMPILED_CODE_START" in output:
            start_idx = output.find("DECOMPILED_CODE_START") + len("DECOMPILED_CODE_START")
            end_idx = output.find("DECOMPILED_CODE_END")
            decompiled_code = output[start_idx:end_idx].strip()
            return decompiled_code
        
        return None
        
    finally:
        # 清理临时文件
        os.unlink(script_path)

# 使用示例
if __name__ == "__main__":
    binary_file = "/path/to/your/binary"  # 替换为你的可执行文件路径
    pc_addr = "00100800"                  # 替换为你要查找的PC地址
    
    code = analyze_with_ghidra_headless(binary_file, pc_addr)
    if code:
        print("反编译结果:")
        print(code)
    else:
        print("未找到反编译代码")