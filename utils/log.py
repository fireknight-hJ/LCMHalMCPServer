from typing import Dict
import logging
import os
import time
import glob

import config.globs as globs

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



# 定义日志函数，加入各种level
def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)

def log_debug(message: str):
    logger.debug(message)

def log_warning(message: str):
    logger.warning(message)
