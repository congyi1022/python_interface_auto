#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7
# @Author  : Edrain
import yaml

from py_requests.base_api import BaseApi


conf = yaml.safe_load(open("../../data_config/env.yaml"))
host = conf["host"]


class ApiUploadImagePost(BaseApi):
    """上传图像"""
    base_url = "/upload/image"
    url = host + base_url
    params = {}
    method = "POST"
    headers = {"accept": "application/json"}
