import os
import sys

# 设置变量
os.environ['SCRIPT_PATH'] = '/home/haojie/workspace/lcmhalmcp/testcases/server/nxp/NXP_FATFS_BareMetal'
os.environ['DB_PATH'] = '/home/haojie/workspace/dbs_server/DATABASE_NXP_FATFS_BareMetal'
os.environ['SRC_PATH'] = '/home/haojie/mcuxsdk-workspace/mcuxsdk'
os.environ['PROJ_PATH'] = '/home/haojie/mcuxsdk-workspace'

sys.path.append('/home/haojie/workspace/lcmhalmcp')

try:
    from tools.emulator.core import emulate_proj
    emulate_proj()
except Exception as e:
    print(e)