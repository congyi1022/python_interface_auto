#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18
# @Author  : Edrain
import pytest
import allure
from project_interface.supplychain.interface.sc_pre_loan.user_pre_api.borrower_auth_interface import \
    ScPreLoanBorrowerAuthInterface


@allure.feature("供应链-获取注册验证码接口测试")
class TestBorrowerAuthSmsCodeInterface(object):
    """供应链-获取注册验证码接口测试"""

    @allure.story('所有参数都填写')
    def test_borrower_auth_sms_code_interface_case01(self):
        """供应链-获取注册验证码
        所有参数都填写
        """
        mobile = '18823481234'
        template = 'CAPTCHA_SC_REG'
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(mobile, template)
        assert resp['message'] == "成功"

    @allure.story('mobile 字段校验为空')
    def test_borrower_auth_sms_code_interface_case02(self):
        """供应链-获取注册验证码
        手机号为空
        """
        mobile = ''
        template = 'CAPTCHA_SC_REG'
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(mobile, template)
        assert resp['message'] == "发送验证码失败"

    @allure.story('template 字段校验为空')
    def test_borrower_auth_sms_code_interface_case03(self):
        """供应链-获取注册验证码
        类型为空
        """
        mobile = '18823481234'
        template = ''
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(mobile, template)
        assert resp['message'] == "请求参数有误"

    @allure.story('手机号超长 字段校验为空')
    def test_borrower_auth_sms_code_interface_case04(self):
        """供应链-获取注册验证码 手机号超长
        """
        mobile = '1882348123414444111111111111111111'
        template = 'CAPTCHA_SC_REG'
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(mobile, template)
        assert resp['message'] == "发送验证码失败"

    borrower_auth_sms_code_interface_test_data = [("18823481234", "CAPTCHA_SC_REG", "成功"),
                                                  ("", "CAPTCHA_SC_REG", "发送验证码失败"),
                                                  ("18823481234", "", "请求参数有误")
                                                  ]

    @allure.story('参数化')
    @pytest.mark.parametrize(("mobile_data", "template_data", "message_data"),  # 用例参数
                             borrower_auth_sms_code_interface_test_data)  # 用例参数的参数化数据
    def test_borrower_auth_sms_code_interface_case05(self, mobile_data, template_data, message_data):
        """供应链-用户登录接口参数化
        """
        mobile = mobile_data
        template = template_data
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(mobile, template)
        assert resp['message'] == message_data

