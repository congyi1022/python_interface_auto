#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/09
# @Author  : Edrain
import logging
import os
import time
from pathlib import Path
from api_auto_v2.select_env import home_path


class Logger:

    def __init__(self):
        log_name = time.strftime("%Y-%m-%d") + ".log"
        path = Path(home_path[0]) / "log" / log_name  # 路径拼接
        log_path = str(path)
        # 生成日志文件,日期命名，没有就创建
        if os.path.exists(log_path):
            file = open(log_path, "a")
            file.close()
        else:
            file = open(log_path, "w")
            file.close()

        self.logger = logging.getLogger(log_path)
        self.logger.setLevel(logging.DEBUG)

        # 设置格式
        fmt_log = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(module)s]--日志信息：%(message)s")
        fmt_console = logging.Formatter("[%(asctime)s]-[%(levelname)s]-%(message)s")
        # 设置控制台日志
        self.sh = logging.StreamHandler()
        self.sh.setFormatter(fmt_console)
        self.sh.setLevel(logging.DEBUG)
        # 设置文件日志
        self.fh = logging.FileHandler(log_path, encoding="utf-8")
        self.fh.setFormatter(fmt_log)
        self.fh.setLevel(logging.DEBUG)

        self.logger.addHandler(self.sh)
        self.logger.addHandler(self.fh)

    def debug(self, message):
        self.logger.debug(message)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def info(self, message):
        self.logger.info(message)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def warning(self, message):
        self.logger.warning(message)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def error(self, message):
        self.logger.error(message)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)

    def critical(self, message):
        self.logger.critical(message)
        self.logger.removeHandler(self.sh)
        self.logger.removeHandler(self.fh)


if __name__ == "__main__":
    pass
