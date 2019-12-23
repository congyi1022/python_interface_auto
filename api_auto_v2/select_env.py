#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/08/15
# @Author  : Edrain
import re
from pathlib import Path

ENV = "ENV_19"  # 从env_config文件夹里面，选择当前运行的环境

home_path = re.findall(r".*?api_auto_v2", str(Path.cwd()))  # 正则匹配出文件夹的主路径

