#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/16
# @Author  : Edrain
import json
import requests
from common.enums.request_enums import PlatformProjectEnums
from common.utils.logger import Logger
from common.utils.config_headers_data import *

req = []  # 全局变量


def request(method, url, description, params=None, token=None, platform=PlatformProjectEnums.UNIVERSAL.value,
            content_type=ContentTypeEnums.APPLICATION_JSON.value):
    """
    重新封装requests方法，自定义调用
    :param method: 新建 Request 对象要使用的HTTP方法
    :param url: 新建 Request 对象的URL
    :param description: 调用该方法，会实现的功能描述
    :param params: 传入参数，Request 对象的查询字符中要发送的字典或字节内容
    :param token: 用户token
    :param platform: 项目平台信息
    :param content_type: Content-Type的类型
    :return:
    """
    global req  # global代表应用全局变量
    Logger().info(f'【功能描述】：{description}')
    Logger().info(f'【请求地址】：{str(url)}')
    try:
        if platform == PlatformProjectEnums.UNIVERSAL.value:  # 平台选择为通用
            if content_type == ContentTypeEnums.APPLICATION_JSON.value:
                headers_content_type(method, url, params, content_type, header_content_type_json)
        elif platform == PlatformProjectEnums.SUPPLY_CHAIN.value:  # 平台选择为供应链
            g31_headers_without_cookie = get_g31_headers_without_cookie()
            g31_headers_with_cookie = get_g31_headers_with_cookie(token, content_type)
            if content_type == ContentTypeEnums.APPLICATION_JSON.value:
                headers_content_type(method, url, params, content_type, g31_headers_without_cookie)
            elif content_type == ContentTypeEnums.CUSTOMIZE.value:
                headers_content_type(method, url, params, content_type, g31_headers_with_cookie)
            elif content_type == ContentTypeEnums.FORM_DATA.value:
                headers_content_type(method, url, params, content_type, g31_headers_with_cookie)
            else:
                headers_content_type(method, url, params, content_type, g31_headers_with_cookie)
        else:
            Logger().info('platForm平台参数有误！')
        if content_type != ContentTypeEnums.FORM_DATA.value:
            Logger().info(f'【请求参数】：{params}')
        Logger().info("【Response】：" + req.text)
    except Exception as error:
        Logger().error(error)
    if req.status_code == 200:
        return req.json()
    else:
        Logger().info(f'【请求有误，status_code={req.status_code}】')


def headers_content_type(method, url, params, content_type, detail_headers):
    """
    填写headers
    :param method: 新建 Request 对象要使用的HTTP方法
    :param url:  新建 Request 对象的URL
    :param params:  传入参数，Request 对象的查询字符中要发送的字典或字节内容
    :param content_type:  Content-Type的类型
    :param detail_headers: 详细的headers填写
    :return:
    """
    global req  # global代表应用全局变量
    if content_type in [ContentTypeEnums.APPLICATION_JSON.value, ContentTypeEnums.CUSTOMIZE.value]:
        req = requests.request(method, url, data=json.dumps(params), headers=detail_headers)
    elif content_type == ContentTypeEnums.FORM_DATA.value:
        req = requests.request(method, url, data=params[0], files=params[1], headers=detail_headers)
    else:
        req = requests.request(method, url, params=params, headers=detail_headers)
    Logger().info(f'【Headers 】：{detail_headers}')


def schedule(method, url, description):
    """
    定时器任务执行
    :param method: 新建 Request 对象要使用的HTTP方法
    :param url: 新建 Request 对象的URL
    :param description: 调用该方法，会实现的功能描述
    :return:
    """
    req_schedule = requests.request(method, url, headers=header_content_type_json)
    Logger().info(f'【定时任务--功能描述】：{description}')
    Logger().info(f'【定时任务--请求地址】：{url}')
    Logger().info(f'【定时任务--Headers 】：{header_content_type_json}')
    Logger().info(f'【定时任务--Response】:{req_schedule.text}')


if __name__ == "__main__":
    # request("GET", "http://www.httpbin.org/get", "这个接口哇，可以干好多的事情哇~")
    # request("GET", "http://www.httpbin.org/get", "这个接口哇，可以干好多的事情哇~", platform=PlatformProjectEnums.SUPPLY_CHAIN.value)
    # schedule("GET", "http://www.httpbin.org/get", "定时任务哇，可以干好多的事情哇~")
    request("GET", "http://www.httpbin.org/anything/", "这个接口哇，可以干好多的事情哇~", params="哇哈哈")

