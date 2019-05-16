# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 17:49
# @Author  : Edrain
import requests
from util.use_json import UseJson


class UseHeader:

    def __init__(self, response):
        self.respone = response

    def get_response_url(self):
        """获取登录返回的token的url"""
        url = self.respone['data']['url'][0]
        return url

    def get_cookie(self):
        """获取cookie的jar文件"""
        url = self.get_response_url()
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        usejson = UseJson()
        usejson.write_data(cookie)


# if __name__ == '__main__':
#     useheader = UseHeader()
#     print(useheader.get_response_url())
#     print(useheader.get_cookie())
