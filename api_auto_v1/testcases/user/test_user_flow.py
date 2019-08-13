#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6
# @Author  : Edrain
import json
from api_auto_v1.api.user_pre_api.borrower_auth import *
from api_auto_v1.api.user_pre_api.upload import ApiUploadImagePost
from api_auto_v1.util.tool import Tool
from api_auto_v1.util.use_data import UseData
from api_auto_v1.util.use_mysql import UseMysql
from api_auto_v1.util.use_yaml import UseYaml


class TestUserFlow(object):
    conf = yaml.safe_load(open("../../data_config/user.yaml"))
    password = conf["password"]
    reg_code = conf["reg_code"]
    tool = Tool()
    use_yaml = UseYaml()
    use_data = UseData()
    use_mysql = UseMysql()
    mobile = use_data.phone_generator()
    name = "接口{}".format(tool.num_chinese(mobile[-4:]))
    id_card_number = use_data.get_random_id_card()

    def test_borrower_get_sms_code(self):
        """获取注册验证码"""
        ApiBorrowerAuthSmsCodePost() \
            .set_json({"mobile": self.mobile, "template": "CAPTCHA_SC_REG"}) \
            .run().validate("json().message", "成功")

    def test_borrower_reg_by_sms_code(self):
        """用户注册"""
        resp = ApiBorrowerRegBySmsCodePost() \
            .set_json(
            {"mobile": self.mobile, "captcha": "123456", "password": self.password, "confirmPassword": self.password,
             "regCode": self.reg_code}) \
            .run()
        assert json.loads(resp.response.text)["message"] == "成功"
        print("手机号：{} ，名字：{} ，身份证号：{} ".format(self.mobile, self.name, self.id_card_number))

    def test_borrower_login_by_pwd(self):
        """手机号码、密码 登录"""
        self.use_mysql.select_borrower_code()  # 关联数据库，通过手机查询code
        resp = ApiBorrowerLoginByPwdPost() \
            .set_json({"mobile": self.mobile, "password": self.password}) \
            .run()
        assert json.loads(resp.response.text)["message"] == "登录成功"
        self.use_yaml.write_yaml_user_cookie(resp)

    def test_upload_id_card_front_image(self):
        """使用 cookie, 上传身份证正面照"""
        cookie = self.use_yaml.read_yaml_user_cookie()
        resp = ApiUploadImagePost() \
            .set_header("Cookie", cookie) \
            .set_params(imageType="FRONT_IMAGE") \
            .set_file(self.tool.upload_image()) \
            .run()
        assert json.loads(resp.response.text)["message"] == "成功"
