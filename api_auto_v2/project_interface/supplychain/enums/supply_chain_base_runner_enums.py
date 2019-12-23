#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/08/19
# @Author  : Edrain
from enum import Enum


class SupplyChainCaptchaEnums(Enum):
    USER_LOGIN_CAPTCHA = 'CAPTCHA_SC_REG'
    CH_LOGIN_CAPTCHA = 'CAPTCHA_SC_AGENCY_LOGIN'


class SupplyChainBusinessCreditType(Enum):
    BUSINESS_CREDIT_TYPE_ORDER = "ORDER"
    BUSINESS_CREDIT_TYPE_RAPID = "RAPID"
