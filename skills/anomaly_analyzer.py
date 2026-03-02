# 异常分析技能
from typing import Dict, List, Any, Optional
import re
from pathlib import Path

class AnomalyAnalyzer:
    """嵌入式系统异常分析器，增强了对误报死循环的检测和处理"""
    
    def __init__(self):
        # 初始化函数和正常启动序列
        self.init_functions = {
            'FillZerobss', 'LoopFillZerobss', 'CopyDataInit', 
            'LoopCopyDataInit', 'Zero_Init', 'memset', 
            'memcpy', 'memmove', 'Zero_Init_Div'
        }
        
        self.normal_init_sequences = [
            # 正常的启动序列
            ['Reset_Handler', 'SystemInit'],
            ['Reset_Handler', 'SystemClock_Config'],
            ['Reset_Handler', 'FillZerobss'],
            ['Reset_Handler', 'FillZerobss', 'main'],
            # RT-Thread常见序列
            ['Reset_Handler', 'FillZerobss', 'rtthread_startup'],
            ['Reset_Handler', 'FillZerobss', 'SystemInit', 'rt_application_init']
        ]
        
        # 硬件初始化模式匹配
        self.hardware_init_patterns = [
            r'.*GPIO.*Init.*',
            r'.*Clock.*Config.*',
            r'.*RCC.*Init.*',
            r'.*SystemInit.*',
            r'.*HAL.*Init.*',
            r'.*MX.*Init.*'
        ]
    
    def analyze_execution_log(self, log_file_path: str) -> Dict[str, Any]:
        """
        分析执行日志，判断是否为正常异常
        增强了对误报死循环的检测和处理
        
        Args:
            log_file_path: 执行日志文件路径
            
        Returns:
            分析结果字典
        """
        result = {
            'is_anomaly': False,
            'anomaly_type': None,
            'confidence': 0.0,
            'reasoning': '',
            'suggestions': []
        }
        
        if not Path(log_file_path).exists():
            result['reasoning'] = '日志文件不存在'
            return result
        
        try:
            with open(log_file_path, 'r') as f:
                lines = f.readlines()
        except Exception as e:
            result['reasoning'] = f'无法读取日志文件: {e}'
            return result
        
        # 提取函数调用序列
        function_sequence = []
        for line in lines:
            match = re.search(r'current function:\s*(\w+)', line)
            if match:
                function_sequence.append(match.group(1))
        
        if not function_sequence:
            result['reasoning'] = '无法提取函数调用序列'
            return result
        
        # 读取完整日志内容用于误报检测
        with open(log_file_path, 'r') as f:
            log_content = f.read()
        
        # 检查误报死循环：白名单函数被错误标记为循环
        false_positive_result = self._detect_false_positive_loop(log_content)
        
        if false_positive_result['is_false_positive']:
            result.update({
                'is_anomaly': False,  # 误报情况不算异常
                'anomaly_type': 'false_positive_loop',
                'confidence': false_positive_result['confidence'],
                'reasoning': false_positive_result['reasoning'],
                'suggestions': false_positive_result['suggestions']
            })
            return result
        
        # 分析函数序列
        analysis_result = self._analyze_function_sequence(function_sequence)
        
        # 如果检测到死循环但函数在白名单中，可能是误报
        if (analysis_result['is_anomaly'] and 
            analysis_result.get('anomaly_type') == 'dead_loop'):
            loop_function = self._identify_loop_function(function_sequence)
            if loop_function and loop_function in self.init_functions:
                result.update({
                    'is_anomaly': False,  # 覆盖为正常情况
                    'anomaly_type': 'false_positive_loop',
                    'confidence': 0.95,
                    'reasoning': f'检测到误报死循环：初始化函数{loop_function}被错误标记为死循环',
                    'suggestions': [
                        f'确认{loop_function}确实是初始化函数且执行有限次数',
                        f'这是正常的初始化过程，不是真正的死循环',
                        f'建议：1) 将{loop_function}添加到白名单 2) 检查模拟器循环检测配置',
                        f'3) 确认循环检测规则是否正确匹配初始化函数',
                        f'4) 如果误报持续，考虑修改循环检测算法',
                        f'5) 确认初始化函数确实执行了有限次数，不是无限循环'
                    ]
                })
        
        # 更新最终分析结果
        result.update(analysis_result)
        
        return result
    
    def _detect_false_positive_loop(self, log_content: str) -> Dict[str, Any]:
        """
        检测是否为误报的死循环（白名单函数被错误标记为循环）
        
        Args:
            log_content: 日志内容
            
        Returns:
            检测结果
        """
        result = {
            'is_false_positive': False,
            'confidence': 0.0,
            'reasoning': '',
            'suggestions': []
        }
        
        # 检查是否有"Skipping loop detection for whitelisted function"的日志
        if 'Skipping loop detection for whitelisted function' not in log_content:
            return result
        
        # 提取被跳过的函数名
        skipped_funcs = []
        lines = log_content.split('\n')
        for line in lines:
            if 'Skipping loop detection for whitelisted function:' in line:
                match = re.search(r'Skipping loop detection for whitelisted function:\s*(\w+)', line)
                if match:
                    skipped_funcs.append(match.group(1))
        
        if skipped_funcs:
            # 检查这些函数是否在初始化函数白名单中
            false_positive_funcs = [func for func in skipped_funcs if func in self.init_functions]
            
            if false_positive_funcs:
                result.update({
                    'is_false_positive': True,
                    'confidence': 0.95,
                    'reasoning': f'检测到误报死循环：初始化函数{", ".join(false_positive_funcs)}被错误标记为循环',
                    'suggestions': [
                        f'这些是正常的系统初始化函数，不应该进行循环检测',
                        f'建议：1) 将{", ".join(false_positive_funcs)}添加到白名单 2) 修改循环检测逻辑',
                        f'3) 检查模拟器循环检测配置是否正确',
                        f'4) 如果误报持续，考虑修改循环检测算法',
                        f'5) 确认初始化函数确实执行了有限次数，不是无限循环'
                    ]
                })
        
        return result
    
    def _sequence_matches(self, sequence1: List[str], sequence2: List[str]) -> bool:
        """
        检查序列是否匹配（允许部分匹配）
        """
        if len(sequence1) < len(sequence2):
            return False
        
        # 检查前缀匹配
        for i, func in enumerate(sequence2):
            if i >= len(sequence1):
                break
            if sequence1[i] != func:
                return False
        
        return True
    
    def _has_loop_pattern(self, function_sequence: List[str]) -> bool:
        """
        检查是否存在循环模式（重复调用同一函数）
        """
        if len(function_sequence) < 3:
            return False
        
        # 检查是否有函数重复出现
        for i in range(len(function_sequence) - 2):
            if (function_sequence[i] == function_sequence[i + 1] == 
                function_sequence[i + 2]):
                return True
        
        return False
    
    def _identify_loop_function(self, function_sequence: List[str]) -> Optional[str]:
        """
        识别循环中的主要函数
        """
        if not function_sequence:
            return None
        
        # 找出現次數最多的函數
        from collections import Counter
        func_counts = Counter(function_sequence)
        most_common = func_counts.most_common(1)[0][0]
        
        return most_common
    
    def _analyze_function_sequence(self, function_sequence: List[str]) -> Dict[str, Any]:
        """
        分析函数调用序列
        
        Args:
            function_sequence: 函数调用序列
            
        Returns:
            分析结果
        """
        result = {
            'is_anomaly': False,
            'anomaly_type': None,
            'confidence': 0.0,
            'reasoning': '',
            'suggestions': []
        }
        
        # 1. 检查是否是正常的初始化序列
        for sequence in self.normal_init_sequences:
            if self._sequence_matches(function_sequence, sequence):
                result.update({
                    'is_anomaly': False,
                    'anomaly_type': 'normal_init_sequence',
                    'confidence': 0.9,
                    'reasoning': f'检测到正常的初始化序列: {sequence}',
                    'suggestions': ['建议将相关函数添加到循环检测白名单']
                })
                return result
        
        # 2. 检查是否包含大量初始化函数
        init_count = sum(1 for func in function_sequence if func in self.init_functions)
        total_calls = len(function_sequence)
        
        if init_count > total_calls * 0.7:  # 70%以上是初始化函数
            result.update({
                'is_anomaly': False,
                'anomaly_type': 'init_routine',
                'confidence': 0.8,
                'reasoning': f'检测到初始化例程，包含{init_count}个初始化函数调用',
                'suggestions': [
                    f'建议将以下函数添加到白名单: {", ".join(set(function_sequence) & self.init_functions)}',
                    '这些是正常的系统初始化函数，不应该被视为死循环'
                ]
            })
            return result
        
        # 3. 检查循环模式
        if self._has_loop_pattern(function_sequence):
            loop_function = self._identify_loop_function(function_sequence)
            if loop_function and loop_function in self.init_functions:
                result.update({
                    'is_anomaly': False,
                    'anomaly_type': 'init_loop',
                    'confidence': 0.85,
                    'reasoning': f'检测到初始化函数{loop_function}的循环模式，这可能是正常的初始化循环',
                    'suggestions': [
                        f'建议将{loop_function}添加到白名单',
                        '这是正常的初始化代码模式'
                    ]
                })
                return result
            else:
                result.update({
                    'is_anomaly': True,
                    'anomaly_type': 'dead_loop',
                    'confidence': 0.9,
                    'reasoning': f'检测到死循环模式，函数: {loop_function}',
                    'suggestions': [
                        '检查循环条件',
                        '验证循环终止条件',
                        '考虑添加超时机制'
                    ]
                })
                return result
        
        # 4. 默认情况
        if function_sequence:
            result.update({
                'is_anomaly': True,
                'anomaly_type': 'unknown_pattern',
                'confidence': 0.5,
                'reasoning': f'未识别的执行模式，序列: {function_sequence}',
                'suggestions': ['需要人工分析执行日志']
            })
        
        return result
    
    def suggest_whitelist_functions(self, log_file_path: str) -> List[str]:
        """
        基于日志建议需要添加到白名单的函数
        
        Args:
            log_file_path: 日志文件路径
            
        Returns:
            建议的函数列表
        """
        suggested = set()
        
        try:
            with open(log_file_path, 'r') as f:
                lines = f.readlines()
                
            for line in lines:
                match = re.search(r'current function:\s*(\w+)', line)
                    if match:
                        func = match.group(1)
                    # 检查是否是初始化函数
                    if (func in self.init_functions or
                        any(re.match(pattern, func) for pattern in self.hardware_init_patterns)):
                        suggested.add(func)
                        
        except Exception as e:
            print(f"分析日志时出错: {e}")
        
        return list(suggested)