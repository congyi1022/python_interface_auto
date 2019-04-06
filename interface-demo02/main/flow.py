# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 16:15
# @Author  : Edrain
import time
import unittest
from test_case.test_case01 import Test01
from util import HTMLTestRunner
from util.send_mail import SendEmail


class BaseFlow:

    def __init__(self):
        self.send_mail = SendEmail()

    def run_case(self):
        suite = unittest.TestSuite()
        # suite的2种用法：
        # 第一种suite.addTest()
        suite.addTest(Test01('test_01'))
        suite.addTest(Test01('test_02'))
        # 2种用法：第二种suite.addTests()
        # suite.addTests(map(Test01, ["test_01", "test_02"]))

        # 输出结果：测试结果直接输出在控制台
        # unittest.TextTestRunner().run(suite)

        # 输出结果：将测试结果以report.html形式生成
        now = time.strftime("%Y-%m-%d %H%M", time.localtime())  # 取当前时间
        filename = "../report/" + now + "-report.html"  # 保存的报告路径和名称
        fp = open(filename, 'wb')
        HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'接口自动化测试报告Demo01', description=u'测试者：哇哈哈').run(suite)

        # 发送邮件带测试报告附件
        # self.send_mail.send_main()


if __name__ == '__main__':
    run = BaseFlow()
    run.run_case()
