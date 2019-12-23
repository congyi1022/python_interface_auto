#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16
# @Author  : Edrain
from common.enums.host_enums import SupplyChainHostEnums
from biz_service.read_env_service import ReadEnv
from common.enums.request_enums import PlatformProjectEnums, ContentTypeEnums

from common.utils.request import request
from project_interface.supplychain.data.supply_chain_input_data import G31UserInputData


class ScPreLoanUploadImageInterface(G31UserInputData):

    def __init__(self):
        self.host_port = ReadEnv().read_env(SupplyChainHostEnums.SC_PRE_LOAN_HOST.value)

    def upload_image(self, token, image_type):
        """上传图像"""
        description = '供应链-上传图像'
        method = "POST"
        path = "/sc/upload/image"
        url = self.host_port + path
        image_body = self.upload_image_body(image_type)
        response = request(method, url, description, params=image_body, token=token, platform=PlatformProjectEnums.SUPPLY_CHAIN.value,
                           content_type=ContentTypeEnums.FORM_DATA.value)
        return response



