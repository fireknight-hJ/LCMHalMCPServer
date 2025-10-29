import os
import subprocess
import shutil  # 添加shutil模块用于删除目录
from models.build_results.build_output import BuildOutput

# TODO: 项目编译（暂定运行指令人工指定）

def build_result_to_info(build_result: subprocess.CompletedProcess) -> BuildOutput:
    """Convert subprocess.CompletedProcess to BuildOutput"""
    return BuildOutput(
        std_err=build_result.stderr,
        std_out=build_result.stdout,
        exit_code=build_result.returncode,
    )

# @mcp
def build_proj(conf_path: str):
    """build project, return build result"""
    # 执行conf_path下的build.sh脚本
    build_result = subprocess.run(["bash", "build.sh"], cwd=conf_path, capture_output=True, text=True)
    # 转换为BuildOutput
    build_output = build_result_to_info(build_result)
    return build_output

def clear_proj(conf_path: str):
    """clear project, return clear result"""
    # 执行conf_path下的clear.sh脚本
    clear_result = subprocess.run(["bash", "clear.sh"], cwd=conf_path, capture_output=True, text=True)
    print(clear_result.stdout)
    print(clear_result.stderr)
    print(clear_result.returncode)
    return clear_result

def build_proj_dbgen(conf_path: str, out_path: str):
    """build project and generate db, return build result
    param1: conf_path: 项目配置路径
    param2: out_path: 数据库输出路径

    codeql database create <database路径> --language=cpp --command="<编译命令>"
    """
    # 检查out_path是否存在，如果存在且目录中存在src.zip文件，说明可能已经生成了数据库，无需重复生成
    if os.path.exists(out_path) and os.listdir(out_path):
        if "src.zip" in os.listdir(out_path):
            print(f"out_path {out_path} is not an empty directory, and src.zip already exists")
            return
        print(f"out_path {out_path} is not an empty directory, but src.zip does not exist, remove it")
        # 修复：使用shutil.rmtree()删除目录，而不是os.remove()
        shutil.rmtree(out_path)
        print(f"Removed directory: {out_path}")
    
    # 检查out_path是否存在，如果不存在则创建
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        print(f"Created directory: {out_path}")
    
    # 先清除项目
    clear_proj(conf_path)
    
    # 检查build.sh文件是否存在
    build_sh_path = os.path.join(conf_path, "build.sh")
    if not os.path.exists(build_sh_path):
        print(f"Error: build.sh not found in {conf_path}")
        return None
    
    # 修复：移除多余的引号转义
    build_result = subprocess.run([
        "codeql", 
        "database", 
        "create", 
        out_path, 
        "--language=cpp", 
        "--command=bash build.sh"
    ], cwd=conf_path, capture_output=True, text=True)
    
    print(build_result.stdout)
    print(build_result.stderr)
    print(build_result.returncode)
    return build_result

if __name__ == "__main__":
    # # 编译FreeRTOSLwIP_StreamingServer项目 (Linux Server)
    # build_proj("/home/haojie/workspace/lcmhalmcp/testcases/freertos_streamserver")
    # 编译FreeRTOSLwIP_StreamingServer项目 (Macbook Laptop)
    build_proj("/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver")
    # 生成FreeRTOSLwIP_StreamingServer项目的CodeQL数据库
    build_proj_dbgen("/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver", "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer_Macbook")
    # 清除FreeRTOSLwIP_StreamingServer项目
    clear_proj("/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver")