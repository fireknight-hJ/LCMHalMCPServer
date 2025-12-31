import os
import json
import time
import uuid
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import threading


class AILogManager:
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
        self.session_id: Optional[str] = None
        self.log_dir: Optional[str] = None
        self.session_log_file: Optional[str] = None
        self.session_metadata: Dict[str, Any] = {}
        self._session_lock = threading.Lock()
        self._enabled = True
    
    def initialize_session(self, db_path: str, session_id: Optional[str] = None) -> str:
        with self._session_lock:
            if session_id is None:
                session_id = str(uuid.uuid4())
            
            self.session_id = session_id
            self.log_dir = os.path.join(db_path, "lcmhal_ai_log")
            
            Path(self.log_dir).mkdir(parents=True, exist_ok=True)
            
            timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            self.session_log_file = os.path.join(
                self.log_dir,
                f"session_{session_id}_{timestamp}.json"
            )
            
            self.session_metadata = {
                "session_id": session_id,
                "start_time": datetime.now().isoformat(),
                "logs": [],
                "agent_message_counts": {}
            }
            
            self._save_session_metadata()
            
            return session_id
    
    def get_session_id(self) -> Optional[str]:
        return self.session_id
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def set_enabled(self, enabled: bool):
        self._enabled = enabled
    
    def _serialize_data(self, data: Any) -> Any:
        """
        递归地将数据转换为可 JSON 序列化的格式
        """
        if isinstance(data, (str, int, float, bool)) or data is None:
            return data
        elif isinstance(data, dict):
            return {key: self._serialize_data(value) for key, value in data.items()}
        elif isinstance(data, (list, tuple)):
            return [self._serialize_data(item) for item in data]
        elif hasattr(data, 'model_dump'):
            return data.model_dump()
        elif hasattr(data, '__dict__'):
            return self._serialize_data(data.__dict__)
        else:
            return str(data)

    def log_agent_interaction(
        self,
        agent_name: str,
        interaction_type: str,
        data: Dict[str, Any],
        function_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        with self._session_lock:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "agent_name": agent_name,
                "interaction_type": interaction_type,
                "function_name": function_name,
                "data": self._serialize_data(data),
                "metadata": self._serialize_data(metadata or {})
            }
            
            self.session_metadata["logs"].append(log_entry)
            self._save_session_metadata()
    
    def log_agent_result(
        self,
        agent_name: str,
        result: Dict[str, Any],
        function_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        self.log_agent_interaction(
            agent_name=agent_name,
            interaction_type="result",
            data=result,
            function_name=function_name,
            metadata=metadata
        )
    
    def log_agent_error(
        self,
        agent_name: str,
        error: str,
        function_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        self.log_agent_interaction(
            agent_name=agent_name,
            interaction_type="error",
            data={"error": error},
            function_name=function_name,
            metadata=metadata
        )
    
    def get_session_logs(self, agent_name: Optional[str] = None) -> List[Dict[str, Any]]:
        if self.session_id is None:
            return []
        
        logs = self.session_metadata.get("logs", [])
        
        if agent_name is not None:
            logs = [log for log in logs if log.get("agent_name") == agent_name]
        
        return logs
    
    def get_function_logs(self, function_name: str) -> List[Dict[str, Any]]:
        if self.session_id is None:
            return []
        
        logs = self.session_metadata.get("logs", [])
        return [log for log in logs if log.get("function_name") == function_name]
    
    def save_legacy_log(
        self,
        msg_type: str,
        result: Dict[str, Any],
        function_name: Optional[str] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        self.log_agent_interaction(
            agent_name=msg_type,
            interaction_type="legacy",
            data=result,
            function_name=function_name,
            metadata={"legacy_format": True}
        )
    
    def _save_session_metadata(self):
        if self.session_log_file is None:
            return
        
        try:
            with open(self.session_log_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_metadata, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to save session metadata: {e}")
    
    def finalize_session(self):
        if self.session_id is None:
            return
        
        with self._session_lock:
            self.session_metadata["end_time"] = datetime.now().isoformat()
            self.session_metadata["log_count"] = len(self.session_metadata.get("logs", []))
            self._save_session_metadata()
    
    def export_session(self, file_path: Optional[str] = None) -> str:
        if self.session_id is None:
            raise ValueError("No active session")
        
        if file_path is None:
            timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            file_path = os.path.join(
                self.log_dir,
                f"session_export_{self.session_id}_{timestamp}.json"
            )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.session_metadata, f, ensure_ascii=False, indent=2)
        
        return file_path
    
    def log_langgraph_node(
        self,
        agent_name: str,
        node_name: str,
        state: Dict[str, Any],
        function_name: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        with self._session_lock:
            messages = state.get("messages", [])
            agent_key = f"{agent_name}_{function_name or 'default'}"
            
            last_count = self.session_metadata["agent_message_counts"].get(agent_key, 0)
            current_count = len(messages)
            
            new_messages = messages[last_count:]
            
            new_messages_summary = []
            for msg in new_messages:
                msg_dict = {}
                
                if isinstance(msg, dict):
                    msg_dict["type"] = msg.get("type", "dict")
                    msg_dict["role"] = msg.get("role", "unknown")
                    msg_dict["content"] = str(msg.get("content", ""))[:500]
                elif hasattr(msg, '__class__'):
                    msg_dict["type"] = msg.__class__.__name__
                    if hasattr(msg, 'role'):
                        msg_dict["role"] = msg.role
                    if hasattr(msg, 'content'):
                        msg_dict["content"] = str(msg.content)[:500]
                    if hasattr(msg, 'tool_calls') and msg.tool_calls:
                        msg_dict["tool_calls"] = [
                            {"name": call.get("name"), "args": str(call.get("args", {}))[:200]}
                            for call in msg.tool_calls
                        ]
                else:
                    msg_dict["type"] = "unknown"
                    msg_dict["content"] = str(msg)[:500]
                
                new_messages_summary.append(msg_dict)
            
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "agent_name": agent_name,
                "interaction_type": "langgraph_node",
                "node_name": node_name,
                "function_name": function_name,
                "data": {
                    "total_messages": current_count,
                    "new_messages": len(new_messages),
                    "message_range": [last_count, current_count - 1] if new_messages else [],
                    "new_messages_summary": new_messages_summary,
                    "state_keys": list(state.keys())
                },
                "metadata": metadata or {}
            }
            
            self.session_metadata["logs"].append(log_entry)
            self.session_metadata["agent_message_counts"][agent_key] = current_count
            self._save_session_metadata()

    def log_langgraph_node_start(
        self,
        agent_name: str,
        node_name: str,
        state: Dict[str, Any],
        function_name: Optional[str] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        self.log_langgraph_node(
            agent_name=agent_name,
            node_name=node_name,
            state=state,
            function_name=function_name,
            metadata={"phase": "start"}
        )

    def log_langgraph_node_end(
        self,
        agent_name: str,
        node_name: str,
        state: Dict[str, Any],
        function_name: Optional[str] = None
    ):
        if not self._enabled or self.session_id is None:
            return
        
        self.log_langgraph_node(
            agent_name=agent_name,
            node_name=node_name,
            state=state,
            function_name=function_name,
            metadata={"phase": "end"}
        )

    def clear_session(self):
        with self._session_lock:
            self.session_id = None
            self.session_log_file = None
            self.session_metadata = {}


ai_log_manager = AILogManager()
