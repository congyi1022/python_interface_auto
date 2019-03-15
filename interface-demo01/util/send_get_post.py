# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 11:08
# @Author  : Edrain
import requests


class RunMain:
    """接口请求类型"""

    def send_get(self, url, params, headers):
        response = requests.get(url=url, params=params, headers=headers).json()
        return response

    def send_post(self, url, data, headers):
        response = requests.post(url=url, data=data, headers=headers).json()
        return response

    def run_main(self, url, params, data, headers, method):
        response = None
        if method == "GET":
            response = self.send_get(url, params, headers)
        else:
            response = self.send_post(url, data, headers)
        return response
