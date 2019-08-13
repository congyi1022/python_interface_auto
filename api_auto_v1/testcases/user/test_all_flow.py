#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12
# @Author  : Edrain
from api_auto_v1.testcases.user.test_user_flow import TestUserFlow


class TestAllFlow(object):

    def test_all_flow(self):
        """用户端注册 + 上传照片"""
        user = TestUserFlow()  # user端
        user.test_borrower_get_sms_code()
        user.test_borrower_reg_by_sms_code()
        user.test_borrower_login_by_pwd()
        user.test_upload_id_card_front_image()
