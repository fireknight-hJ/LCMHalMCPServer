import os
import json
import glob
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import threading


class LogIndexManager:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._initialized = True
        self.log_dir: Optional[str] = None
        self.index_file: Optional[str] = None
        self._index_data: Dict[str, Any] = {}
        self._index_lock = threading.Lock()
    
    def initialize(self, db_path: str):
        with self._index_lock:
            self.log_dir = os.path.join(db_path, "lcmhal_ai_log")
            Path(self.log_dir).mkdir(parents=True, exist_ok=True)
            
            self.index_file = os.path.join(self.log_dir, "log_index.json")
            
            self._load_index()
    
    def _load_index(self):
        if self.index_file is None or not os.path.exists(self.index_file):
            self._index_data = {
                "sessions": {},
                "legacy_logs": {},
                "last_updated": datetime.now().isoformat()
            }
            return
        
        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                self._index_data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load log index: {e}")
            self._index_data = {
                "sessions": {},
                "legacy_logs": {},
                "last_updated": datetime.now().isoformat()
            }
    
    def _save_index(self):
        if self.index_file is None:
            return
        
        self._index_data["last_updated"] = datetime.now().isoformat()
        
        try:
            with open(self.index_file, 'w', encoding='utf-8') as f:
                json.dump(self._index_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to save log index: {e}")
    
    def register_session(
        self,
        session_id: str,
        session_file: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        with self._index_lock:
            self._index_data["sessions"][session_id] = {
                "session_file": session_file,
                "created_at": datetime.now().isoformat(),
                "metadata": metadata or {}
            }
            self._save_index()
    
    def register_legacy_log(
        self,
        msg_type: str,
        function_name: str,
        log_file: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        with self._index_lock:
            key = f"{msg_type}_{function_name}"
            
            if key not in self._index_data["legacy_logs"]:
                self._index_data["legacy_logs"][key] = []
            
            self._index_data["legacy_logs"][key].append({
                "log_file": log_file,
                "created_at": datetime.now().isoformat(),
                "metadata": metadata or {}
            })
            
            self._save_index()
    
    def get_session_info(self, session_id: str) -> Optional[Dict[str, Any]]:
        with self._index_lock:
            return self._index_data["sessions"].get(session_id)
    
    def get_all_sessions(self) -> List[Dict[str, Any]]:
        with self._index_lock:
            sessions = []
            for session_id, info in self._index_data["sessions"].items():
                sessions.append({
                    "session_id": session_id,
                    **info
                })
            return sessions
    
    def get_legacy_logs(
        self,
        msg_type: Optional[str] = None,
        function_name: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        with self._index_lock:
            results = []
            
            for key, logs in self._index_data["legacy_logs"].items():
                parts = key.split("_", 1)
                if len(parts) != 2:
                    continue
                
                log_type, func_name = parts
                
                if msg_type is not None and log_type != msg_type:
                    continue
                
                if function_name is not None and func_name != function_name:
                    continue
                
                for log_entry in logs:
                    results.append({
                        "msg_type": log_type,
                        "function_name": func_name,
                        **log_entry
                    })
            
            return results
    
    def find_latest_legacy_log(
        self,
        msg_type: str,
        function_name: str
    ) -> Optional[Dict[str, Any]]:
        logs = self.get_legacy_logs(msg_type, function_name)
        
        if not logs:
            return None
        
        return max(logs, key=lambda x: x.get("created_at", ""))
    
    def scan_legacy_logs(self):
        if self.log_dir is None:
            return
        
        with self._index_lock:
            pattern = os.path.join(self.log_dir, "*.json")
            files = glob.glob(pattern)
            
            for file_path in files:
                filename = os.path.basename(file_path)
                
                if filename.startswith("session_"):
                    continue
                
                if filename == "log_index.json":
                    continue
                
                parts = filename.replace(".json", "").split("_")
                
                if len(parts) >= 2:
                    msg_type = parts[0]
                    function_name = "_".join(parts[1:-1])
                    
                    key = f"{msg_type}_{function_name}"
                    
                    if key not in self._index_data["legacy_logs"]:
                        self._index_data["legacy_logs"][key] = []
                    
                    existing_files = [
                        log["log_file"] for log in self._index_data["legacy_logs"][key]
                    ]
                    
                    if file_path not in existing_files:
                        self._index_data["legacy_logs"][key].append({
                            "log_file": file_path,
                            "created_at": datetime.fromtimestamp(
                                os.path.getmtime(file_path)
                            ).isoformat(),
                            "metadata": {"scanned": True}
                        })
            
            self._save_index()
    
    def cleanup_old_logs(self, days: int = 30):
        if self.log_dir is None:
            return
        
        cutoff_time = datetime.now().timestamp() - (days * 24 * 60 * 60)
        removed_count = 0
        
        with self._index_lock:
            for key in list(self._index_data["legacy_logs"].keys()):
                self._index_data["legacy_logs"][key] = [
                    log for log in self._index_data["legacy_logs"][key]
                    if os.path.exists(log["log_file"]) and
                       os.path.getmtime(log["log_file"]) > cutoff_time
                ]
                
                if not self._index_data["legacy_logs"][key]:
                    del self._index_data["legacy_logs"][key]
                    continue
            
            for session_id in list(self._index_data["sessions"].keys()):
                session_info = self._index_data["sessions"][session_id]
                session_file = session_info.get("session_file")
                
                if session_file and os.path.exists(session_file):
                    if os.path.getmtime(session_file) < cutoff_time:
                        try:
                            os.remove(session_file)
                            del self._index_data["sessions"][session_id]
                            removed_count += 1
                        except Exception as e:
                            print(f"[ERROR] Failed to remove old session file: {e}")
            
            self._save_index()
        
        return removed_count
    
    def get_index_stats(self) -> Dict[str, Any]:
        with self._index_lock:
            return {
                "total_sessions": len(self._index_data["sessions"]),
                "total_legacy_logs": sum(
                    len(logs) for logs in self._index_data["legacy_logs"].values()
                ),
                "last_updated": self._index_data.get("last_updated"),
                "log_dir": self.log_dir
            }


log_index_manager = LogIndexManager()
