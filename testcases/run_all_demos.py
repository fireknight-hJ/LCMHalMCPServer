#!/usr/bin/env python3
"""
运行testcases/macbook目录下所有demo的脚本
- 最多同时运行3个demo
- 某个demo异常退出时，跳过并继续运行下一个
- 记录每个demo的运行结果
- 将标准输出重定向到testcases_out文件夹中的文件
"""

import os
import subprocess
import concurrent.futures
import time

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# 测试用例目录
TESTCASES_DIR = os.path.join(PROJECT_ROOT, 'testcases', 'macbook')
# 输出目录
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'testcases_out')
# 最大并行运行数
MAX_WORKERS = 3

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_all_demo_paths():
    """获取所有demo的路径"""
    demo_paths = []
    
    # 遍历macbook目录下的所有目录
    for item in os.listdir(TESTCASES_DIR):
        item_path = os.path.join(TESTCASES_DIR, item)
        
        # 如果是目录
        if os.path.isdir(item_path):
            # 特殊处理rt-thread目录，需要遍历其子目录
            if item == 'rt-thread':
                for subitem in os.listdir(item_path):
                    subitem_path = os.path.join(item_path, subitem)
                    if os.path.isdir(subitem_path) and not subitem.startswith('.'):
                        demo_paths.append(subitem_path)
            else:
                demo_paths.append(item_path)
    
    return demo_paths


def run_demo(demo_path):
    """运行单个demo"""
    demo_name = os.path.basename(demo_path)
    print(f"开始运行: {demo_name}")
    print(f"路径: {demo_path}")
    
    # 构建输出文件路径
    output_file = os.path.join(OUTPUT_DIR, f"{demo_name}_output.txt")
    error_file = os.path.join(OUTPUT_DIR, f"{demo_name}_error.txt")
    
    try:
        # 构建命令行
        cmd = [
            'python3', '-m', 'main',
            demo_path
        ]
        
        # 运行命令
        start_time = time.time()
        result = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=3600  # 设置1小时超时
        )
        end_time = time.time()
        
        # 计算运行时间
        run_time = end_time - start_time
        
        # 将输出写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.stdout)
        
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(result.stderr)
        
        print(f"输出已保存到: {output_file}")
        print(f"错误输出已保存到: {error_file}")
        
        # 检查结果
        if result.returncode == 0:
            print(f"✓ {demo_name} 运行成功 (耗时: {run_time:.2f}秒)")
            return {
                'demo': demo_name,
                'path': demo_path,
                'status': 'success',
                'time': run_time,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'output_file': output_file,
                'error_file': error_file
            }
        else:
            print(f"✗ {demo_name} 运行失败 (返回码: {result.returncode})")
            return {
                'demo': demo_name,
                'path': demo_path,
                'status': 'failed',
                'returncode': result.returncode,
                'time': run_time,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'output_file': output_file,
                'error_file': error_file
            }
    
    except subprocess.TimeoutExpired:
        print(f"✗ {demo_name} 运行超时")
        # 写入超时信息到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('')
        
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write('运行超时（超过1小时）')
        
        return {
            'demo': demo_name,
            'path': demo_path,
            'status': 'timeout',
            'stdout': '',
            'stderr': '运行超时（超过1小时）',
            'output_file': output_file,
            'error_file': error_file
        }
    except Exception as e:
        print(f"✗ {demo_name} 运行异常: {e}")
        # 写入异常信息到文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('')
        
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(str(e))
        
        return {
            'demo': demo_name,
            'path': demo_path,
            'status': 'error',
            'error': str(e),
            'stdout': '',
            'stderr': str(e),
            'output_file': output_file,
            'error_file': error_file
        }


def main():
    """主函数"""
    print("开始运行所有demo...")
    print(f"项目根目录: {PROJECT_ROOT}")
    print(f"测试用例目录: {TESTCASES_DIR}")
    print(f"最大并行数: {MAX_WORKERS}")
    print()
    
    # 获取所有demo路径
    demo_paths = get_all_demo_paths()
    print(f"找到 {len(demo_paths)} 个demo:")
    for i, path in enumerate(demo_paths, 1):
        print(f"{i}. {os.path.basename(path)} - {path}")
    print()
    
    # 运行结果
    results = []
    
    # 使用线程池并行运行demo
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # 提交所有任务
        future_to_demo = {executor.submit(run_demo, path): path for path in demo_paths}
        
        # 处理结果
        for future in concurrent.futures.as_completed(future_to_demo):
            demo_path = future_to_demo[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"处理 {os.path.basename(demo_path)} 结果时发生异常: {e}")
    
    print()
    print("=" * 80)
    print("运行结果汇总:")
    print("=" * 80)
    
    # 统计结果
    success_count = 0
    failed_count = 0
    timeout_count = 0
    error_count = 0
    
    for result in results:
        status = result['status']
        if status == 'success':
            success_count += 1
        elif status == 'failed':
            failed_count += 1
        elif status == 'timeout':
            timeout_count += 1
        elif status == 'error':
            error_count += 1
    
    print(f"成功: {success_count}")
    print(f"失败: {failed_count}")
    print(f"超时: {timeout_count}")
    print(f"错误: {error_count}")
    print(f"总计: {len(results)}")
    print()
    
    # 显示失败的demo
    if failed_count > 0 or timeout_count > 0 or error_count > 0:
        print("失败的demo:")
        for result in results:
            if result['status'] != 'success':
                print(f"- {result['demo']} ({result['status']})")
                if 'error' in result:
                    print(f"  错误: {result['error']}")
                elif 'returncode' in result:
                    print(f"  返回码: {result['returncode']}")
        print()
    print("所有demo运行完成！")
    
    # 将汇总结果写入文件
    summary_file = os.path.join(OUTPUT_DIR, "summary.txt")
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("运行结果汇总:\n")
        f.write("=" * 80 + "\n")
        f.write(f"成功: {success_count}\n")
        f.write(f"失败: {failed_count}\n")
        f.write(f"超时: {timeout_count}\n")
        f.write(f"错误: {error_count}\n")
        f.write(f"总计: {len(results)}\n")
        f.write("\n")
        
        if failed_count > 0 or timeout_count > 0 or error_count > 0:
            f.write("失败的demo:\n")
            for result in results:
                if result['status'] != 'success':
                    f.write(f"- {result['demo']} ({result['status']})\n")
                    if 'error' in result:
                        f.write(f"  错误: {result['error']}\n")
                    elif 'returncode' in result:
                        f.write(f"  返回码: {result['returncode']}\n")
                    if 'output_file' in result:
                        f.write(f"  输出文件: {result['output_file']}\n")
                    if 'error_file' in result:
                        f.write(f"  错误文件: {result['error_file']}\n")
        
        f.write("\n")
        f.write("所有demo运行完成！\n")
    
    print(f"汇总结果已保存到: {summary_file}")


if __name__ == "__main__":
    main()
