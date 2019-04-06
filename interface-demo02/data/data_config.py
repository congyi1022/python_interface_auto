# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 18:07
# @Author  : Edrain


class GlobalVar:
    """case id"""
    id = "0"
    name = "1"
    url = "2"
    run = "3"
    request_way = "4"
    request_header = "5"
    case_depend = "6"
    data_depend = "7"
    field_depend = "8"
    request_data = "9"
    expect = "10"
    result = "11"


def get_id():
    """获取case id"""
    return GlobalVar.id


def get_name():
    """获取 name"""
    return GlobalVar.name


def get_url():
    """获取 url"""
    return GlobalVar.url


def get_run():
    """获取run"""
    return GlobalVar.run


def get_request_way():
    """获取request_way"""
    return GlobalVar.request_way


def get_request_header():
    """获取 request_header"""
    return GlobalVar.request_header


def get_case_depend():
    """获取 case_depend"""
    return GlobalVar.case_depend


def get_data_depend():
    """获取 data_depend"""
    return GlobalVar.data_depend


def get_field_depend():
    """获取 field_depend"""
    return GlobalVar.field_depend


def get_request_data():
    """获取 request_data"""
    return GlobalVar.request_data


def get_expect():
    """获取 expect"""
    return GlobalVar.expect


def get_result():
    """获取 result"""
    return GlobalVar.result




