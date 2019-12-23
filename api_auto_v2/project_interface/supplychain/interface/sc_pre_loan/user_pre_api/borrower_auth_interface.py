#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15
# @Author  : Edrain
from common.enums.host_enums import SupplyChainHostEnums
from common.enums.request_enums import PlatformProjectEnums
from common.utils.request import request
from biz_service.read_env_service import ReadEnv
from project_interface.supplychain.data.supply_chain_input_data import G31UserInputData


class ScPreLoanBorrowerAuthInterface(G31UserInputData):
    def __init__(self):
        self.host_port = ReadEnv().read_env(SupplyChainHostEnums.SC_PRE_LOAN_HOST.value)

    def borrower_auth_sms_code(self, mobile, template):
        """获取注册验证码"""
        description = '供应链-获取注册验证码'
        method = "POST"
        path = "/sc/auth/get"
        url = self.host_port + path
        params = self.borrower_auth_sms_code_body(mobile, template)
        response = request(method, url, description, params=params, platform=PlatformProjectEnums.SUPPLY_CHAIN.value)
        return response

    def borrower_reg_by_sms_code(self):
        """供应链-用户注册"""
        description = '供应链-用户注册'
        method = "POST"
        path = "/sc/auth/bysmscode"
        url = self.host_port + path
        params = self.borrower_reg_by_sms_code_body()
        response = request(method, url, description, params=params, platform=PlatformProjectEnums.SUPPLY_CHAIN.value)
        return response

    def borrower_auth_sa_login_by_pwd(self):
        """供应链-用户密码登录"""
        description = '供应链-用户密码登录'
        method = "POST"
        path = "/sc/borrower/auth/!/login/bypwd"
        url = self.host_port + path
        params = self.borrower_auth_sa_login_by_pwd_body()
        response = request(method, url, description, params=params, platform=PlatformProjectEnums.SUPPLY_CHAIN.value)
        return response

