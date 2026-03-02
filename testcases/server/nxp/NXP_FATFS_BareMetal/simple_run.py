#!/usr/bin/env python3

import os
import sys

# 设置全局变量
SCRIPT_PATH = "/home/haojie/workspace/lcmhalmcp/testcases/server/nxp/NXP_FATFS_BareMetal"
DB_PATH = "/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal"
SRC_PATH = "/home/haojie/mcuxsdk-workspace/mcuxsdk"
PROJ_PATH = "/home/haojie/mcuxsdk-workspace"

# 设置环境变量
os.environ['LCMHAL_SCRIPT_PATH'] = SCRIPT_PATH
os.environ['LCMHAL_DB_PATH'] = DB_PATH
os.environ['LCMHAL_SRC_PATH'] = SRC_PATH
os.environ['LCMHAL_PROJ_PATH'] = PROJ_PATH

print('=== NXP FATFS BareMetal 模拟器配置 ===')
print(f'Script Path: {SCRIPT_PATH}')
print(f'DB Path: {DB_PATH}')
print(f'Src Path: {SRC_PATH}')
print(f'Proj Path: {PROJ_PATH}')
print('=====================================')

# 添加项目路径
sys.path.insert(0, '/home/haojie/workspace/lcmhalmcp')

# 尝试导入并运行模拟器
try:
    from tools.emulator.core import emulate_proj
    print('开始运行模拟器...')
    result = emulate_proj()
    print(f'模拟器运行结果: {result}')
except Exception as e:
    print(f'错误: {e}')
    import traceback
    traceback.print_exc()