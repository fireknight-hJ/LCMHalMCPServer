# 核心数据管理模块，集中管理项目全局数据
import json
import config.globs as globs
from models.analyze_results.function_analyze import ReplacementUpdate
from tools.collector.collector import get_mmio_func_list, get_function_info
from agents.analyzer_agent import analyze_functions
from utils.db_cache import check_analyzed_json_log, get_analyzed_json_log, dump_json_log


class DataManager:
    def __init__(self):
        # MMIO函数信息列表
        self.mmio_info_list = {}
        # MMIO函数按文件分类
        self.mmio_infos_by_file = {}
        # 替换更新信息
        self.replacement_updates = {}
        # 替换更新按文件分类
        self.replacement_updates_by_file = {}
        
    
    def replacement_update_log(self, replacement_update: ReplacementUpdate):
        """记录替换更新日志"""
        if globs.ai_log_enable:
            dump_json_log("replacement_update", replacement_update.model_dump())
    
    def get_mmio_info_list(self):
        """获取MMIO函数信息列表"""
        return self.mmio_info_list
    
    def get_mmio_infos_by_file(self):
        """获取按文件分类的MMIO函数信息"""
        return self.mmio_infos_by_file
    
    def get_replacement_updates(self):
        """获取替换更新信息"""
        return self.replacement_updates
    
    def get_replacement_updates_by_file(self):
        """获取按文件分类的替换更新信息"""
        return self.replacement_updates_by_file
    
    def update_function_replacement(self, func_name: str, replace_code: str, reason: str):
        """更新函数替换代码"""
        # 不再检查函数是否在mmio_info_list中，允许更新任何函数
        replacement_update = ReplacementUpdate(
            function_name=func_name, 
            replacement_code=replace_code, 
            reason=reason
        )
        
        self.replacement_updates[func_name] = replacement_update
        self.replacement_update_log(replacement_update)
        
        # 更新按文件分类的替换更新信息
        function_info = get_function_info(globs.db_path, func_name)
        if function_info:
            self.replacement_updates_by_file.setdefault(function_info.file_path, []).append(replacement_update)
        
        return True
    
    async def load_mmio_functions(self):
        """加载MMIO函数信息"""
        # 处理所有MMIO函数
        function_list = get_mmio_func_list(globs.db_path)
        self.mmio_info_list = await analyze_functions(function_list)
        
        # 首先加载所有已经存在的替换更新日志，不管是否是MMIO函数
        self._load_all_replacement_updates()
        
        # 分文件收集信息
        self._organize_data_by_file()
    
    def _load_all_replacement_updates(self):
        """加载所有已经存在的替换更新日志"""
        try:
            import os
            import json
            # 检查替换更新日志目录是否存在
            tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
            if not os.path.exists(tmp_dir):
                return
            
            # 首先收集所有唯一的函数名
            unique_func_names = set()
            for file_name in os.listdir(tmp_dir):
                if file_name.startswith("replacement_update_") and file_name.endswith(".json"):
                    # 直接读取文件内容，从文件内容中提取函数名
                    file_path = os.path.join(tmp_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            json_data = f.read()
                            data_dict = json.loads(json_data)
                            # 从文件内容中提取函数名
                            if "function_name" in data_dict:
                                func_name = data_dict["function_name"]
                                unique_func_names.add(func_name)
                    except Exception as e:
                        print(f"Warning: Failed to extract function name from {file_name}: {e}")
            
            # 对于每个唯一的函数名，使用get_analyzed_json_log获取最新的更新版本
            for func_name in unique_func_names:
                # 使用现有的函数检查并加载替换更新
                if check_analyzed_json_log("replacement_update", func_name):
                    json_data = get_analyzed_json_log("replacement_update", func_name)
                    if json_data:
                        try:
                            data_dict = json.loads(json_data)
                            # 创建ReplacementUpdate对象并添加到replacement_updates
                            self.replacement_updates[func_name] = ReplacementUpdate(**data_dict)
                        except Exception as e:
                            print(f"Warning: Failed to parse replacement update for {func_name}: {e}")
        except Exception as e:
            print(f"Error loading replacement updates: {e}")
    
    def _organize_data_by_file(self):
        """将数据按文件分类组织"""
        for func_name, classify_res in self.mmio_info_list.items():
            function_info = get_function_info(globs.db_path, func_name)
            if not function_info:
                continue
                
            file_path = function_info.file_path
            
            # 组织MMIO信息
            if classify_res and classify_res.has_replacement:
                self.mmio_infos_by_file.setdefault(file_path, []).append(classify_res)
            
            # 组织替换更新信息
            if func_name in self.replacement_updates:
                self.replacement_updates_by_file.setdefault(file_path, []).append(self.replacement_updates[func_name])
    
    def get_replace_func_details_by_file(self, file_path: str):
        """根据文件路径获取替换函数详情"""
        # 尝试直接匹配完整文件路径
        mmio_infos = self.mmio_infos_by_file.get(file_path, [])
        replacement_updates = self.replacement_updates_by_file.get(file_path, [])
        
        if mmio_infos:
            return {
                "file_path": file_path,
                "replaced_function_infos": [info.model_dump() for info in mmio_infos],
                "replacement_updates": [update.model_dump() for update in replacement_updates]
            }
        
        # 模糊匹配c文件名称
        file_name = file_path.split("/")[-1]
        matching_files = []
        
        for fp in self.mmio_infos_by_file.keys():
            if fp.endswith(file_name):
                matching_files.append(fp)
        
        if not matching_files:
            return {"error": f"File {file_path} not found in Replacement MMIO function list, maybe no function replacement in this file?"}
        elif len(matching_files) > 1:
            return {
                "warnning": f"File {file_path} found in multiple files, please specify the full path, then re-run this tool with the full path.",
                "file_paths": matching_files,
            }
        
        full_path = matching_files[0]
        mmio_infos = self.mmio_infos_by_file.get(full_path, [])
        replacement_updates = self.replacement_updates_by_file.get(full_path, [])
        replacement_update_func_names = set([update.function_name for update in replacement_updates])
        
        return {
            "file_path": full_path,
            "replaced_function_infos": [info.model_dump() for info in mmio_infos if info.function_name not in replacement_update_func_names],
            "replacement_updates": [update.model_dump() for update in replacement_updates]
        }
    
    def get_function_analysis_and_replacement(self, func_name: str):
        """根据函数名获取该函数的分析和替换信息
        
        Args:
            func_name: 函数名称
            
        Returns:
            dict: 包含函数分析信息和替换信息的字典
                - mmio_info: 函数的MMIO分析信息
                - replacement_update: 函数的替换更新信息（如果有）
                - function_info: 函数的基本信息（如果有）
                - message: 提示信息（如果有）
        """
        result = {}
        has_replacement = False
        
        # 获取MMIO分析信息
        if func_name in self.mmio_info_list:
            result["mmio_info"] = self.mmio_info_list[func_name].model_dump()
            has_replacement = result["mmio_info"].get("has_replacement", False)
        
        # 获取替换更新信息
        if func_name in self.replacement_updates:
            result["replacement_update"] = self.replacement_updates[func_name].model_dump()
            has_replacement = True
        
        # 获取函数基本信息
        function_info = get_function_info(globs.db_path, func_name)
        if function_info:
            # 获取函数内容
            func_content = ""
            idx = function_info.location_line
            while str(idx) in function_info.function_content_in_lines:
                func_content += function_info.function_content_in_lines[str(idx)] + "\n"
                idx += 1
            
            result["function_info"] = {
                "name": function_info.name,
                "file_path": function_info.file_path,
                "location_line": function_info.location_line,
                "function_content": func_content
            }
        else:
            return {"error": f"Function {func_name} not found in database."}
        
        # 如果没有找到替换信息，添加提示信息
        if not has_replacement:
            result["message"] = "这个函数替换没出现，但是有函数本身的function_info"
        
        return result
    
    def get_function_analysis_and_replacement_formatted(self, func_name: str) -> str:
        """根据函数名获取格式化的函数分析和替换信息（文本格式，便于大模型理解）
        
        Args:
            func_name: 函数名称
            
        Returns:
            str: 格式化的函数分析和替换信息
        """
        # 首先获取结构化数据
        data = self.get_function_analysis_and_replacement(func_name)
        
        # 检查是否有错误
        if "error" in data:
            return f"错误：{data['error']}"
        
        # 构建格式化文本
        formatted_text = []
        formatted_text.append(f"=== {func_name} 函数分析与替换信息 ===")
        
        # 添加函数基本信息
        if "function_info" in data:
            func_info = data["function_info"]
            formatted_text.append("\n【函数基本信息】")
            formatted_text.append(f"- 文件路径：{func_info.get('file_path', '未知')}")
            formatted_text.append(f"- 行号：{func_info.get('location_line', '未知')}")
            formatted_text.append(f"- 函数内容：{func_info.get('function_content', '无法获取')}")
        
        # 添加初始分析信息
        if "mmio_info" in data:
            mmio_info = data["mmio_info"]
            formatted_text.append("\n【初始分析】")
            formatted_text.append(f"- 函数用途：{mmio_info.get('usage_type', '未知')}")
            formatted_text.append(f"- 是否需要替换：{'是' if mmio_info.get('has_replacement', False) else '否'}")
            formatted_text.append(f"- 替换原因：{mmio_info.get('reason', '无')}")
            formatted_text.append(f"- 原始代码：{mmio_info.get('original_code', '无法获取')}")
            formatted_text.append(f"- 推荐替换代码：{mmio_info.get('recommended_code', '无')}")
        
        # 添加更新信息
        if "replacement_update" in data:
            update = data["replacement_update"]
            formatted_text.append("\n【替换更新】")
            formatted_text.append(f"- 更新代码：{update.get('replacement_code', '无')}")
            formatted_text.append(f"- 更新原因：{update.get('reason', '无')}")
        
        # 添加提示信息
        if "message" in data:
            formatted_text.append(f"\n【提示】{data['message']}")
        
        formatted_text.append("\n=== 信息结束 ===")
        
        return "\n".join(formatted_text)
    
    def dump_full_info(self):
        """将所有FunctionClassfier和ReplacementUpdate数据结构dump到同一个log文件中"""
        try:
            import os
            import json
            import time
            
            # 统计has_replacement为true的函数数量
            driver_emulation_functions_count = sum(1 for classify_res in self.mmio_info_list.values() if classify_res and classify_res.has_replacement)
            
            # 构建全量信息字典
            full_info = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "driver_emulation_functions_count": driver_emulation_functions_count,
                "function_classifiers": {},
                "replacement_updates": {}
            }
            
            # 添加FunctionClassfier信息
            for func_name, classify_res in self.mmio_info_list.items():
                if classify_res:
                    full_info["function_classifiers"][func_name] = classify_res.model_dump()
                else:
                    full_info["function_classifiers"][func_name] = None
            
            # 添加ReplacementUpdate信息
            for func_name, replacement_update in self.replacement_updates.items():
                full_info["replacement_updates"][func_name] = replacement_update.model_dump()
            
            # 构建log文件路径
            tmp_dir = os.path.join(globs.db_path, "lcmhal_ai_log")
            if not os.path.exists(tmp_dir):
                os.makedirs(tmp_dir)
            
            # 使用时间戳确保文件名唯一
            timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
            file_path = os.path.join(tmp_dir, f"full_info_{timestamp}.json")
            
            # 写入log文件
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(full_info, f, ensure_ascii=False, indent=2)
            
            print(f"Full info dumped to: {file_path}")
            return True
        except Exception as e:
            print(f"Error dumping full info: {e}")
            return False


# 创建全局数据管理器实例
data_manager = DataManager()