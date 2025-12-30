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
        if func_name not in self.mmio_info_list:
            return False
        
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
    
    def load_mmio_functions(self):
        """加载MMIO函数信息"""
        # 处理所有MMIO函数
        function_list = get_mmio_func_list(globs.db_path)
        self.mmio_info_list = analyze_functions(function_list)
        
        # 处理所有替换更新日志
        for func_name, classify_res in self.mmio_info_list.items():
            if check_analyzed_json_log("replacement_update", func_name):
                json_data = get_analyzed_json_log("replacement_update", func_name)
                if json_data:
                    data_dict = json.loads(json_data)
                    self.replacement_updates[func_name] = ReplacementUpdate(**data_dict)
        
        # 分文件收集信息
        self._organize_data_by_file()
    
    def _organize_data_by_file(self):
        """将数据按文件分类组织"""
        for func_name, classify_res in self.mmio_info_list.items():
            function_info = get_function_info(globs.db_path, func_name)
            if not function_info:
                continue
                
            file_path = function_info.file_path
            
            # 组织MMIO信息
            if classify_res.has_replacement:
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


# 创建全局数据管理器实例
data_manager = DataManager()