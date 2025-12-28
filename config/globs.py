# 全局的CodeQL数据库路径
# db_path = "/home/haojie/workspace/DBS/DATABASE_FreeRTOSLwIP_StreamingServer" # linux

db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer" # mac
script_path = ""
src_path = ""
proj_path = ""
# AI Memory日志开关
ai_log_enable = True

import os
import yaml

# 默认配置
default_config = {
    "script_path": "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/freertos_streamserver",
    "db_path": "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer",
    "src_path": "/Users/jie/Documents/workspace/lcmhalgen/posixGen_Demos/LwIP_StreamingServer",
    "proj_path": "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
}

def load_config_from_yaml(script_path):
    config_path = os.path.join(script_path, "lcmhal_config.yml")
    
    # 检查配置文件是否存在
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                return config if config else default_config
        except Exception as e:
            print(f"读取配置文件失败: {e}")
            return default_config
    else:
        # 创建默认配置文件
        os.makedirs(script_path, exist_ok=True)
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                yaml.dump(default_config, f, default_flow_style=False, allow_unicode=True)
            print(f"已在 {config_path} 创建默认配置文件")
        except Exception as e:
            print(f"创建配置文件失败: {e}")
        return default_config


def globs_init(config):
    # 需要使用global关键字声明这些是全局变量
    global script_path, db_path, src_path, proj_path
    
    script_path = config.get("script_path")
    db_path = config.get("db_path")
    src_path = config.get("src_path")
    proj_path = config.get("proj_path")
    # print(f"配置已加载:")
    # print(f"  script_path: {script_path}")
    # print(f"  db_path: {db_path}")
    # print(f"  src_path: {src_path}")
    # print(f"  proj_path: {proj_path}")