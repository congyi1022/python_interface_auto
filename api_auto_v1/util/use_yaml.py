#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7
# @Author  : Edrain
import json

from ruamel.yaml import YAML


class UseYaml(object):

    def read_yaml(self, yaml, key):
        """根据key 读取yaml中的value"""
        with open(yaml) as f:
            content = YAML().load(f)
            return content[key]

    def write_yaml(self, yaml_file, key, value):
        """根据key 修改yaml中的value"""
        with open(yaml_file) as f:
            yaml = YAML()
            content = yaml.load(f)
        with open(yaml_file, 'w') as nf:
            content[key] = value
            yaml.dump(content, nf)
        return self

    def read_yaml_user_cookie(self):
        """读取 user.yaml 的 cookie"""
        cookie = self.read_yaml("../../data_config/user.yaml", "user_cookie")
        return cookie

    def write_yaml_user_cookie(self, resp):
        """更新 user.yaml 的 cookie"""
        token = json.loads(resp.response.text)["token"]  # 获取token
        self.write_yaml("../../data_config/user.yaml", "user_cookie", token)
        return self

    def read_yaml_user_mobile(self):
        """读取user.yaml 的 user_mobile"""
        user_mobile = self.read_yaml("../../data_config/user.yaml", "user_mobile")
        return user_mobile

    def write_yaml_borrower_code_sql(self, borrower_code):
        """更新user.yaml 的 borrower_code"""
        self.write_yaml("../../data_config/user.yaml", "borrower_code", borrower_code)
        return self
