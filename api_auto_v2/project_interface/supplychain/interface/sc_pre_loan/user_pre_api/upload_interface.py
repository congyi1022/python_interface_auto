#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16
# @Author  : Edrain
from common.enums.request_enums import PlatformProjectEnums, ContentTypeEnums
from common.utils.request import request
from project_interface.supplychain.data.supply_chain_input_data import G31UserInputData
from project_interface.supplychain.interface.sc_pre_loan import HostPort


class ScPreLoanUploadImageInterface(G31UserInputData):

    def upload_image(self, token, image_type):
        """上传图像"""
        description = '供应链-上传图像'
        method = "POST"
        path = "/sc/upload/image"
        url = HostPort + path
        image_body = self.upload_image_body(image_type)
        response = request(method, url, description, params=image_body, token=token,
                           platform=PlatformProjectEnums.SUPPLY_CHAIN.value,
                           content_type=ContentTypeEnums.FORM_DATA.value)
        return response
