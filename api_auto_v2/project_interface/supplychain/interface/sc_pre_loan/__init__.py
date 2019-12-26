#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21
# @Author  : Edrain
"""
__init__.py 的作用：相当于把自身整个文件夹当作一个包来管理，每当有外部import的时候，就会自动执行里面的函数。
"""
from biz_service.read_env_service import ReadEnv
from common.enums.host_enums import SupplyChainHostEnums

HostPort = ReadEnv().read_env(SupplyChainHostEnums.SC_PRE_LOAN_HOST.value)
__all__ = ['HostPort']
