#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/16
# @Author  : Edrain
import os
from pathlib import Path
from dotenv import load_dotenv
from select_env import ENV, home_path


class ReadEnv(object):
    """读取环境配置"""

    def __init__(self):
        data_folder = Path(home_path[0]).joinpath("env_config", ENV)  # 路径拼接
        self.path = str(data_folder) + ".env"

    def read_env(self, *args):
        """
        读取环境配置
        :param args:输入key，获取value
        :return:
        """
        load_dotenv(dotenv_path=self.path)
        env = os.getenv(*args)
        return env


if __name__ == '__main__':
    gh = ReadEnv()
    print(gh.read_env("db_ip"))
    print(gh.read_env("db_ip", "db_port"))
