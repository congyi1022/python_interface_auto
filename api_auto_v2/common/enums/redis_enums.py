#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/17
# @Author  : Edrain
from enum import Enum


class SupplyChainRedisEnums(Enum):
    """供应链--Redis相关的枚举"""
    G31_USER_REGISTERED_CAPTCHA = "CAPTCHA:supply:regist_verify_code:MOBILE"  # 31G 用户端-获取注册验证码
    G31_CH_REGISTERED_CAPTCHA = "CAPTCHA:supply:supply_login_code:MOBILE"  # 31G CH端-获取注册验证码
