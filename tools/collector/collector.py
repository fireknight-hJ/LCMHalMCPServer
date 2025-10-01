from utils.db_file import read_struct_definition_to_string
from config.collector_infos import *
import subprocess
# import pandas as pd
import json
import re


# general infos
function_dict = {}
struct_dict = {}
enum_dict = {}
# vtor infos
vtor_list = []
# mmio & driver infos
mmio_function_dict = {}
driver_function_dict = {}
buffer_function_dict = {}

def run_query_and_return_json(query_file : str):
    """
    运行 query 文件并返回获取的json信息
    """
    # 运行query文件
    try:
        subprocess.run([
            "codeql", "query", "run", query_file,
            "--database", db_path,
            "--output", output_bqrs,
        ], check=True)
        subprocess.run(
            [
            "codeql", "bqrs", "decode", output_bqrs,
            "--output", output_json,
            "--format", "json"
        ], check=True)
    except:
        query_string1 = "codeql query run " + query_file + " --database=" + db_path + " --output=" + output_bqrs
        query_string2 = "codeql bqrs decode" + output_bqrs + " --output=" + output_json + " --format=" + "json"
        print("[ERR] Running codeql query failed: \n\t" + query_string1 + "\n\t" + query_string2)
        return
    # 收集运行query的结果
    # df = pd.read_csv(output_csv)
    with open(output_json, "r") as fp:
        # 解析json结果
        result = json.load(fp)
        result = result["#select"]["tuples"]
        return result

def parse_interrupt_vector_table(file_path : str):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    interrupt_functions = []
    is_in_vector_table = False

    for line in lines:
        line = line.strip()

        # 检查 .section .isr_vector 段
        if '.section' in line and '.isr_vector' in line:
            is_in_vector_table = True

        # 找到 g_pfnVectors 标签并开始解析
        if is_in_vector_table and 'g_pfnVectors:' in line:
            is_in_vector_table = True  # 确保找到向量表的开头
            continue  # 跳过标签行

        # 找到 .word 指令，并提取中断处理函数名
        if is_in_vector_table and line.startswith('.word'):
            # 提取函数名
            parts = re.split(r'\s+', line)
            if len(parts) > 1:
                function_name = parts[1]
                interrupt_functions.append(function_name)

        # 如果到达其他节段，结束解析
        if is_in_vector_table and '.section' in line and '.isr_vector' not in line:
            break

    return interrupt_functions

def enum_collector():
    """
    运行enum_collector_query_file获取所有enum信息
    { 'ENUM_NAME' : 0x00 ...}
    """
    result = run_query_and_return_json(enum_collector_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        function_dict[i[0]] = i[1]
    # 打印成功信息
    print("enum_collected")

def function_collector():
    """
    运行function_collector_query_file获取所有函数体信息
    {   'function_name' : {
            'file_path' : '/path/to/csrc.c'
            'location_line' : 121
            'function_content' : "void func() {...}"
        }
        ...
    }
    """
    result = run_query_and_return_json(function_collector_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        function_dict[i[0]] = {}
        function_dict[i[0]]["file_path"] = i[1]
        function_dict[i[0]]["location_line"] = i[2]
        function_dict[i[0]]["function_content"] = read_struct_definition_to_string(i[1], i[2])
    # 打印成功信息
    print("function_collected")

def vtor_collector():
    """
    从vtor_sfile中收集函数中断向量表信息
    vtor_list = ['UART_ISR', 'I2C_ISR', ...]
    """
    global vtor_list
    vtor_list = parse_interrupt_vector_table(vtor_sfile)

def mmio_function_collector():
    """
    运行mmio_function_query_file获取所有mmio函数体信息
    {   'function_name' : {
            'file_path' : '/path/to/csrc.c'
            'location_line' : 121
            'function_content' : "void func() {...}"
        }
        ...
    }
    """
    result = run_query_and_return_json(mmio_function_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        mmio_function_dict[i[0]] = {}
        mmio_function_dict[i[0]]["file_path"] = i[1]
        mmio_function_dict[i[0]]["location_line"] = i[2]
        mmio_function_dict[i[0]]["function_content"] = read_struct_definition_to_string(i[1], i[2])
    # 打印成功信息
    print("function_collected")

def driver_function_collector():
    """
    运行driver_function_query_file获取所有driver函数体信息
    {   'function_name' : {
            'file_path' : '/path/to/csrc.c'
            'location_line' : 121
            'function_content' : "void func() {...}"
        }
        ...
    }
    """
    result = run_query_and_return_json(driver_function_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        driver_function_dict[i[0]] = {}
        driver_function_dict[i[0]]["file_path"] = i[1]
        driver_function_dict[i[0]]["location_line"] = i[2]
        driver_function_dict[i[0]]["function_content"] = read_struct_definition_to_string(i[1], i[2])
    # 打印成功信息
    print("function_collected")

def buffer_function_collector():
    """
    运行buffer_function_query_file获取所有buffer函数体信息
    {   'function_name' : {
            'file_path' : '/path/to/csrc.c'
            'location_line' : 121
            'function_content' : "void func() {...}"
        }
        ...
    }
    """
    result = run_query_and_return_json(buffer_function_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        driver_function_dict[i[0]] = {}
        driver_function_dict[i[0]]["file_path"] = i[1]
        driver_function_dict[i[0]]["location_line"] = i[2]
        driver_function_dict[i[0]]["function_content"] = read_struct_definition_to_string(i[1], i[2])
    # 打印成功信息
    print("function_collected")

def struct_collector():
    """
    运行struct_collector_query_file获取所有struct信息
    {   'struct_name' : {
            'file_path' : '/path/to/csrc.c'
            'location_line' : 121
            'struct_members' : {var1: type1, var2: type2 ...}
            'struct_content' : "void func() {...}"
        }
        ...
    }
    """
    result = run_query_and_return_json(struct_collector_query_file)
    # 保存解析结果到json格式内容中
    for i in result:
        if i[0] not in struct_dict:
            struct_dict[i[0]] = {}
            struct_dict[i[0]]["file_path"] = i[3]
            struct_dict[i[0]]["location_line"] = i[4]
            struct_dict[i[0]]["struct_content"] = read_struct_definition_to_string(i[3], i[4])
            struct_dict[i[0]]["struct_members"] = {}
        struct_dict[i[0]]["struct_members"][i[1]] = i[2]
    # 打印成功信息
    print("struct_collected")
    
# name, var, typeName, s.getFile(), s.getLocation().getStartLine(), number

def collect_infos():
    """
    
    """
    # general info get
    function_collector()
    struct_collector()
    enum_collector()
    # vtor function list get
    # vtor_collector()
    # mmio infos get
    mmio_function_collector()
    driver_function_collector()
    buffer_function_collector()
    print("collection over")
    # TODO: mmio structs collector
    # TODO: driver structs collector
    


def save_infos_into_json_file():
    """
    save infos into json file
    """
    data = {
        "function_dict": function_dict,
        "struct_dict": struct_dict,
        "enum_dict": enum_dict,
        "vtor_list": vtor_list,
        "mmio_function_dict": mmio_function_dict,
        "driver_function_dict": driver_function_dict,
        "buffer_function_dict": buffer_function_dict,
    }
    with open(output_json_file,"w") as fp:
        json.dump(data, fp=fp, indent=4)

def load_data_from_json(input_file):
    """
    load infos from json file
    """
    # 从 JSON 文件中加载数据
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
        # 恢复数据到原来的结构
        function_dict = data.get("function_dict", {})
        struct_dict = data.get("struct_dict", {})
        enum_dict = data.get("enum_dict", {})
        vtor_list = data.get("vtor_list", [])
        mmio_function_dict = data.get("mmio_function_dict", {})
        driver_function_dict = data.get("driver_function_dict", {})
        buffer_function_dict = data.get("buffer_function_dict", {})
    return (function_dict, struct_dict, enum_dict, vtor_list, mmio_function_dict, driver_function_dict, buffer_function_dict)

if __name__ == "__main__":
    # collect infos in code
    collect_infos()
    # save info into json
    save_infos_into_json_file()
    # print 
    print("saving_over")


    