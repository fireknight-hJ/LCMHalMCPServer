# 测试函数分析和替换信息的获取功能
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.data_manager import data_manager
from config.globs import db_path
from tools.collector.collector import get_function_info

# 测试函数
def test_function_info():
    print("===== 测试函数分析和替换信息获取 ====")
    
    # 测试一个可能没有替换信息的函数
    test_func_name = "UART_Transmit_IT"
    
    print(f"\n1. 测试函数: {test_func_name}")
    print("-" * 50)
    
    # 首先检查函数是否存在
    func_info = get_function_info(db_path, test_func_name)
    if func_info:
        print(f"函数基本信息存在: {func_info.name} in {func_info.file_path}:{func_info.location_line}")
    else:
        print(f"函数 {test_func_name} 不存在于数据库中")
        return
    
    # 测试结构化数据获取
    structured_data = data_manager.get_function_analysis_and_replacement(test_func_name)
    print("\n2. 结构化数据:")
    print(f"- 包含mmio_info: {'mmio_info' in structured_data}")
    print(f"- 包含replacement_update: {'replacement_update' in structured_data}")
    print(f"- 包含function_info: {'function_info' in structured_data}")
    print(f"- 包含message: {'message' in structured_data}")
    
    if 'message' in structured_data:
        print(f"- 提示信息: {structured_data['message']}")
    
    # 测试格式化输出
    formatted_output = data_manager.get_function_analysis_and_replacement_formatted(test_func_name)
    print("\n3. 格式化输出:")
    print(formatted_output)

if __name__ == "__main__":
    test_function_info()
