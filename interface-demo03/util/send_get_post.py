# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 17:40
# @Author  : Edrain
import requests


class SendGetPost:
    """发送 Get/Post 请求"""

    def get_main(self, url, params=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=params, headers=header)
        else:
            res = requests.get(url=url, params=params)
        return res.json()

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data.encode(), headers=header)
        else:
            res = requests.post(url=url, data=data.encode())
        return res.json()

    def run_main(self, method, url, data=None, header=None, params=None):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, params, header)
        return res
