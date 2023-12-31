'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 10:13:23
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2023-12-31 22:08:12
FilePath: \ai_painter\main.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import api
from utils.log_util import logger


if __name__ == "__main__":
    logger.info("start AI painter service")
    api.start_service()