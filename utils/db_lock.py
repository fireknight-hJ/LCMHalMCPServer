import logging
from pathlib import Path
import psutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def find_codeql_db_lock_path(db_path):
    """
    根据CodeQL数据库路径找到对应的锁文件路径
    
    Args:
        db_path (str or Path): CodeQL数据库的路径
        
    Returns:
        Path: 锁文件的完整路径，如果路径结构不符合预期则返回None
    """
    db_path = Path(db_path)
    
    # CodeQL数据库的典型结构: .../DATABASE_NAME/db-language/default/cache/.lock
    # 我们需要找到 db-* 目录（如 db-cpp, db-java 等）
    possible_db_dirs = list(db_path.glob("db-*"))
    
    if not possible_db_dirs:
        logger.warning(f"在数据库路径 {db_path} 中未找到 db-* 目录")
        return None
    
    # 通常只有一个 db-* 目录，取第一个
    db_lang_dir = possible_db_dirs[0]
    lock_file_path = db_lang_dir / "default" / "cache" / ".lock"
    
    return lock_file_path

import subprocess
import os

def get_db_lock_owner_pid(db_path):
    """
    检测指定CodeQL数据库是否被占用，并返回占用进程的PID
    
    Args:
        db_path (str or Path): CodeQL数据库的路径
        
    Returns:
        int or None: 占用数据库的进程PID，如果未被占用则返回None
    """
    lock_file_path = find_codeql_db_lock_path(db_path)
    if lock_file_path is None or not lock_file_path.exists():
        return None
    
    try:
        # 使用lsof命令直接查找打开该文件的进程
        result = subprocess.run(
            ['lsof', '-t', str(lock_file_path)],
            capture_output=True, 
            text=True,
            timeout=5  # 设置超时防止命令卡住
        )
        
        if result.returncode == 0 and result.stdout.strip():
            # lsof -t 返回进程PID
            pid = int(result.stdout.strip())
            
            # 验证进程确实存在且打开了该文件
            try:
                # 使用lsof再次验证，获取详细信息
                verify_result = subprocess.run(
                    ['lsof', '-p', str(pid), str(lock_file_path)],
                    capture_output=True,
                    text=True,
                    timeout=3
                )
                
                if verify_result.returncode == 0:
                    # 获取进程名用于日志
                    proc_name = "unknown"
                    try:
                        proc = psutil.Process(pid)
                        proc_name = proc.name()
                    except:
                        pass
                    
                    logger.info(f"发现进程 {pid} ({proc_name}) 正在占用数据库锁")
                    return pid
                    
            except (subprocess.TimeoutExpired, ValueError, psutil.NoSuchProcess):
                pass
                
    except subprocess.TimeoutExpired:
        logger.warning("lsof命令执行超时")
    except FileNotFoundError:
        logger.warning("系统中未安装lsof命令")
    except Exception as e:
        logger.error(f"使用lsof检查锁文件占用时发生错误: {e}")
    
    return None

def is_db_locked(db_path):
    """
    检查数据库是否被占用（简化版）
    
    Args:
        db_path (str or Path): CodeQL数据库的路径
        
    Returns:
        bool: True表示被占用，False表示空闲
    """
    return get_db_lock_owner_pid(db_path) is not None

def remove_db_lock(db_path, force=True):
    """
    删除CodeQL数据库的锁文件
    
    Args:
        db_path (str or Path): CodeQL数据库的路径
        force (bool): 即使有进程占用也强制删除（不推荐）
        
    Returns:
        tuple: (success: bool, message: str, pid: int or None)
    """
    lock_file_path = find_codeql_db_lock_path(db_path)
    if lock_file_path is None:
        return False, "无法确定锁文件路径", None
    
    # 首先检查是否有进程占用
    owner_pid = get_db_lock_owner_pid(db_path)
    
    if owner_pid is not None and not force:
        return False, f"数据库被进程 {owner_pid} 占用，无法安全删除锁文件", owner_pid
    
    try:
        if lock_file_path.exists():
            # 如果有进程占用但force=True，先尝试终止进程
            if owner_pid is not None and force:
                try:
                    proc = psutil.Process(owner_pid)
                    proc.terminate()
                    logger.warning(f"已强制终止DB占用进程 {owner_pid}")
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    logger.warning(f"无法终止进程 {owner_pid}: {e}")
            
            # 删除锁文件
            lock_file_path.unlink()
            logger.info(f"已删除锁文件: {lock_file_path}")
            return True, "锁文件已成功删除", owner_pid
        else:
            return True, "锁文件不存在，无需删除", None
            
    except PermissionError:
        error_msg = f"权限不足，无法删除锁文件 {lock_file_path}"
        logger.error(error_msg)
        return False, error_msg, owner_pid
    except Exception as e:
        error_msg = f"删除锁文件时发生错误: {e}"
        logger.error(error_msg)
        return False, error_msg, owner_pid

def safe_remove_db_lock(db_path, max_wait=60, check_interval=5):
    """
    安全地删除数据库锁，会等待一段时间如果数据库被占用
    
    Args:
        db_path (str or Path): CodeQL数据库的路径
        max_wait (int): 最大等待时间（秒）
        check_interval (int): 检查间隔（秒）
        
    Returns:
        tuple: (success: bool, message: str, waited: int)
    """
    import time
    
    start_time = time.time()
    waited = 0
    
    while waited < max_wait:
        owner_pid = get_db_lock_owner_pid(db_path)
        
        if owner_pid is None:
            # 没有占用，可以安全删除
            success, message, _ = remove_db_lock(db_path)
            return success, message, waited
        
        logger.info(f"数据库被进程 {owner_pid} 占用，等待中... ({waited}s/{max_wait}s)")
        time.sleep(check_interval)
        waited = time.time() - start_time
    
    # 超时后仍然被占用
    return False, f"等待 {max_wait} 秒后数据库仍然被进程 {owner_pid} 占用", max_wait
