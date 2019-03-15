# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 13:45
# @Author  : Edrain
import json
import unittest

import requests

from util.send_get_post import RunMain


class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有用例运行之前只执行一次\n")

    def setUp(self):
        print("每个用例开始之前执行")
        self.run = RunMain()

    def tearDown(self):
        print("每个用例结束之后执行")

    @classmethod
    def tearDownClass(cls):
        print("所有用例运行之后只执行一次")

    def test_01(self):
        url = 'https://api.douban.com/v2/book/search'
        params = {"q": "小王子"}
        res = self.run.run_main(url, params, None, None, "GET")
        print(res)
        self.assertEqual(res['count'], 20, '返回的count有20条')
        print("这是get测试方法")

    @unittest.skip("无条件跳过此用例")
    def test_02(self):
        url = 'http://10.244.76.19:8079/sc/heqi/sync/bypartner'
        test_data = {"partnerId": 5204}
        headers = {"Content-Type": "application/json"}
        res = self.run.run_main(url, None, json.dumps(test_data), headers, "POST")      # 为content-type为application/json格式
        print("这里是返回的值：", res)
        self.assertEqual(res['executed'], True, '返回executed状态，为True')
        # self.assertEqual(res.get("code"), '200', '返回状态错误，不为200')
        self.assertEqual(res['errorCode']['code'], 'SUCCESSFULLY')
        print("这是post测试方法")

    @unittest.skip("无条件跳过此用例")
    def test_03(self):
        test_url = 'http://10.244.76.19:8079/sc/heqi/sync/bypartner'
        datalist = {"partnerId": 5204}
        head = {"Content-Type": "application/json"}  # 定义头部
        response = requests.post(test_url, data=json.dumps(datalist), headers=head)  # 发起一个请求，使用post方法
        result = response.text  # 读取请求返回的结果
        print(result)  # 打印返回的结果
        print("这是post测试方法")




