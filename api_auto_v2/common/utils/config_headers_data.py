#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/16
# @Author  : Edrain
from common.enums.request_enums import ContentTypeEnums

header_content_type_json = {"Content-Type": "application/json"}


def get_g31_headers_without_cookie():
    """生成31G不带cookie的header"""
    headers = dict()
    headers['Product'] = "31G"
    headers['Content-Type'] = "application/json"
    return headers


def get_g31_headers_with_cookie(token, content_type=ContentTypeEnums.APPLICATION_JSON.value):
    """
    header传入供应链token，获取header
    :param token:
    :param content_type:
    :return:
    """
    headers = dict()
    headers['x-auth-token'] = token
    headers['Product'] = "31G"
    if content_type != ContentTypeEnums.FORM_DATA.value:
        headers['Content-Type'] = ContentTypeEnums.APPLICATION_JSON.value
    return headers
