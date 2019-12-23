#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/19
# @Author  : Edrain
from enum import Enum


class DBConfigEnums(Enum):
    """数据库配置"""
    DB_IP = "db_ip"
    DB_PORT = "db_port"
    DB_PASSWORD = "db_password"
    DB_USERNAME = "db_username"


class DBEnums(Enum):
    """具体数据库"""
    SUPPLYCHAIN = "supplychain"
