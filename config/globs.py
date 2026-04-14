# 全局的CodeQL数据库路径
db_path = "/home/haojie/workspace/dbs_server/DATABASE_LwIP_StreamingServer" # linux
# db_path = "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_FreeRTOSLwIP_StreamingServer" # mac
script_path = ""
src_path = ""
proj_path = ""
# AI Memory日志开关
ai_log_enable = True
# Session ID，用于统一管理一次运行的所有日志
session_id = ""
# 语言偏好设置，用于控制提示语言选择
language_preference = "zh"  # 默认使用中文
# 是否在每次 UpdateFunctionReplacement 时启用“Rubric + 编译验证”事务流程（默认开启）
enable_compile_verify = True
# 是否将 BufferFunction 并入 MMIOFunction 集合（默认开启，减少 UART buffer 路径漏检）
enable_buffer_functions_as_mmio = True

# --- 毕设/消融实验（见 doc/thesis_experiments.md）---
# experiment_mode: full = VerifyReplacement + Fixer + 未验证替换清空；no_feedback = 不挂载验证/修复工具，采纳结构化输出中的替换
experiment_mode = "full"
# tool_profile: full = Collector 全部 MCP 工具；minimal = 仅 GetFunctionInfo（源码上下文消融）
tool_profile = "full"
# LangGraph agent↔tools 最大步数（默认与历史行为一致）
analyzer_recursion_limit = 50
# 是否在 lcmhal_ai_log session 中记录每次 LLM ainvoke 的 usage 与耗时
llm_usage_log_enable = False

import os
import sys
import yaml
from utils.ai_log_manager import ai_log_manager
from utils.log_index import log_index_manager

# 默认配置
default_config = {
    "script_path": "/home/haojie/workspace/lcmhalmcp/testcases/server/stm32/LwIP_StreamingServer",
    "db_path": "/home/haojie/workspace/dbs_server/DATABASE_LwIP_StreamingServer",
    "src_path": "/home/haojie/posixGen_Demos/LwIP_StreamingServer",
    "proj_path": "/home/haojie/posixGen_Demos/LwIP_StreamingServer"
}

def load_config_from_yaml(script_path):
    # script_path 为空时回退到默认（仅用于 recover/clean 等）；run 命令应在 main 中强制要求传入
    if not script_path:
        script_path = default_config["script_path"]
        print(f"script_path 为空，使用默认: {script_path}（若在 run 流程请确保传入 testcase 目录）")
    
    config_path = os.path.join(script_path, "lcmhal_config.yml")
    
    # 检查配置文件是否存在
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                return config if config else default_config
        except Exception as e:
            print(f"读取配置文件失败: {e}")
            return default_config
    else:
        # 创建默认配置文件
        os.makedirs(script_path, exist_ok=True)
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                yaml.dump(default_config, f, default_flow_style=False, allow_unicode=True)
            print(f"已在 {config_path} 创建默认配置文件")
        except Exception as e:
            print(f"创建配置文件失败: {e}")
        return default_config


def _parse_bool(v, default=False) -> bool:
    if v is None:
        return default
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("1", "true", "yes", "on"):
        return True
    if s in ("0", "false", "no", "off", ""):
        return False
    return default


def globs_init(config):
    # 需要使用global关键字声明这些是全局变量
    global script_path, db_path, src_path, proj_path, session_id
    global experiment_mode, tool_profile, analyzer_recursion_limit, llm_usage_log_enable

    script_path = config.get("script_path")
    db_path = config.get("db_path")
    src_path = config.get("src_path")
    proj_path = config.get("proj_path")

    experiment_mode = str(config.get("experiment_mode", "full") or "full").strip().lower()
    if experiment_mode not in ("full", "no_feedback"):
        experiment_mode = "full"
    tool_profile = str(config.get("tool_profile", "full") or "full").strip().lower()
    if tool_profile not in ("full", "minimal"):
        tool_profile = "full"
    try:
        analyzer_recursion_limit = int(config.get("analyzer_recursion_limit", 50))
    except (TypeError, ValueError):
        analyzer_recursion_limit = 50
    if analyzer_recursion_limit < 2:
        analyzer_recursion_limit = 2
    llm_usage_log_enable = _parse_bool(config.get("llm_usage_log_enable", False), False)

    # 环境变量覆盖 YAML（便于命令行实验而无需改文件）
    _em = os.environ.get("LCMHAL_EXPERIMENT_MODE", "").strip().lower()
    if _em in ("full", "no_feedback"):
        experiment_mode = _em
    _tp = os.environ.get("LCMHAL_TOOL_PROFILE", "").strip().lower()
    if _tp in ("full", "minimal"):
        tool_profile = _tp
    _arl = os.environ.get("LCMHAL_ANALYZER_RECURSION_LIMIT", "").strip()
    if _arl.isdigit():
        v = int(_arl, 10)
        analyzer_recursion_limit = v if v >= 2 else 2
    if _parse_bool(os.environ.get("LCMHAL_LLM_USAGE_LOG", ""), False):
        llm_usage_log_enable = True

    if (
        experiment_mode != "full"
        or tool_profile != "full"
        or analyzer_recursion_limit != 50
        or llm_usage_log_enable
    ):
        print(
            f"[globs] experiment_mode={experiment_mode} tool_profile={tool_profile} "
            f"analyzer_recursion_limit={analyzer_recursion_limit} llm_usage_log_enable={llm_usage_log_enable}",
            file=sys.stderr,
        )

    # print(f"配置已加载:")
    # print(f"  script_path: {script_path}")
    # print(f"  db_path: {db_path}")
    # print(f"  src_path: {src_path}")
    # print(f"  proj_path: {proj_path}")
    
    # 初始化日志索引管理器
    log_index_manager.initialize(db_path)
    
    # 扫描旧的日志文件，建立索引
    log_index_manager.scan_legacy_logs()
    
    # 初始化AI日志管理器的session
    if ai_log_enable:
        session_id = ai_log_manager.initialize_session(db_path)
        print(f"Session ID: {session_id}", file=sys.stderr)


def get_session_id():
    """获取当前session ID"""
    global session_id
    return session_id


def finalize_session():
    """结束当前session，保存所有日志"""
    global session_id
    if session_id and ai_log_enable:
        ai_log_manager.finalize_session()
        log_index_manager.register_session(
            session_id,
            ai_log_manager.session_log_file,
            {"script_path": script_path, "db_path": db_path}
        )
        print(f"Session {session_id} finalized and logged.")
        summ = (ai_log_manager.session_metadata or {}).get("llm_usage_summary")
        if summ and isinstance(summ, dict):
            n = summ.get("invoke_count", 0)
            tms = summ.get("total_elapsed_ms", 0)
            tp = summ.get("total_prompt_tokens")
            tc = summ.get("total_completion_tokens")
            tt = summ.get("total_tokens")
            line = f"[LLM Usage] invokes={n} total_elapsed_ms={tms}"
            if tp is not None and tc is not None:
                line += f" prompt_tokens={tp} completion_tokens={tc}"
                if tt is not None:
                    line += f" total_tokens={tt}"
            print(line)