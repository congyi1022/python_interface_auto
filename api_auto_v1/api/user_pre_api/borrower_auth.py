#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6
# @Author  : Edrain
import yaml
from py_requests.base_api import BaseApi


conf = yaml.safe_load(open("../../data_config/env.yaml"))
host = conf["host"]


class ApiBorrowerAuthSmsCodePost(BaseApi):
    """获取注册验证码"""
    base_url = "/borrower/auth/!/smscode/get"
    url = host + base_url
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}


class ApiBorrowerRegBySmsCodePost(BaseApi):
    """输入验证码，注册"""
    base_url = "/borrower/auth/!/reg/bysmscode"
    url = host + base_url
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}


class ApiBorrowerLoginByPwdPost(BaseApi):
    base_url = "/borrower/auth/!/login/bypwd"
    url = host + base_url
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}

