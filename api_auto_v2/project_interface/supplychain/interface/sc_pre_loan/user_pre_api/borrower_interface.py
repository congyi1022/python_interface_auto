#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16
# @Author  : Edrain
from biz_service.read_env_service import ReadEnv
from common.enums.host_enums import SupplyChainHostEnums
from common.enums.request_enums import PlatformProjectEnums, ContentTypeEnums
from common.utils.request import request
from project_interface.supplychain.data.supply_chain_input_data import G31UserInputData


class ScPreLoanBorrowerInterface(G31UserInputData):

    def __init__(self):
        self.host_port = ReadEnv().read_env(SupplyChainHostEnums.SC_PRE_LOAN_HOST.value)

    def borrower_save_base_info(self, token):
        """保存借款人资料"""
        description = '供应链-保存借款人资料'
        method = "POST"
        path = "/sc/saveBaseInfo"
        url = self.host_port + path
        params = self.borrower_save_base_info_body()
        response = request(method, url, description, token=token, params=params,
                           platform=PlatformProjectEnums.SUPPLY_CHAIN.value,
                           content_type=ContentTypeEnums.SUPPLY_CHAIN_HEADER.value)
        return response
