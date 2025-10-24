import os
import subprocess

# TODO: 项目编译（暂定运行指令人工指定）

# @mcp
def build_proj(conf_path: str):
    """build project, return build result"""
    # 执行conf_path下的build.sh脚本
    build_result = subprocess.run(["bash", "build.sh"], cwd=conf_path, capture_output=True, text=True)
    print(build_result.stdout)
    print(build_result.stderr)
    print(build_result.returncode)
    return build_result


if __name__ == "__main__":
    build_proj("/home/haojie/workspace/lcmhalmcp/testcases/freertos_streamserver")
