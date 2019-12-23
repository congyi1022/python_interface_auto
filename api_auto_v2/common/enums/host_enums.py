#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/19
# @Author  : Edrain
from enum import Enum


class RedisHostEnums(Enum):
    REDIS_URL = "redis_url"
    REDIS_PORT = "redis_port"


class SupplyChainHostEnums(Enum):
    SC_PRE_LOAN_HOST = "sc_pre_loan_host"
