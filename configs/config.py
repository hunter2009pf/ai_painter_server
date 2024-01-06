'''
Author: hunter2009pf angel_clothes@outlook.com
Date: 2023-12-31 19:16:26
LastEditors: hunter2009pf angel_clothes@outlook.com
LastEditTime: 2023-12-31 22:12:50
FilePath: \ai_painter\configs\config.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
import argparse
from dynaconf import Dynaconf
from sys import platform
import os


work_dir = os.getcwd()

AI_PAINTER_ENVIRONMENT = os.getenv('AI_PAINTER_ENVIRONMENT', None) # 开发环境：dev；生产环境：release
 
IS_LINUX = True if (platform == "linux" or platform == "linux2") else False

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        f'{work_dir}/configs/settings_release.yaml' if (AI_PAINTER_ENVIRONMENT == "release") else f'{work_dir}/configs/settings_dev.yaml', 
    ],
) if IS_LINUX else Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[work_dir + '\\configs\\settings_windows.yaml', work_dir + '\\configs\\.secrets.yaml'],
)

parser = argparse.ArgumentParser(prog='ai_painter',
                                 description='draw pictures with AI | '
                                             '使用人工智能绘画')

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
