#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/07/15
# @Author  : Edrain
from pathlib import Path

from biz_service.redis_service import RedisService
from common.enums.redis_enums import SupplyChainRedisEnums
from select_env import home_path
from test_cases.supply_g31.supply_chain_base_runner import SupplyChainBaseRunner


class G31UserInputData(SupplyChainBaseRunner):

    def borrower_auth_sms_code_body(self, mobile, template):
        """获取注册验证"""
        body = dict()
        body['mobile'] = mobile
        body['template'] = template
        return body

    def borrower_reg_by_sms_code_body(self):
        """通过手机号，得到Redis中的验证码"""
        body = dict()
        body['mobile'] = self.user_mobile
        captcha = RedisService().get_redis_value(SupplyChainRedisEnums.G31_USER_REGISTERED_CAPTCHA.value,
                                                 self.user_mobile)
        if captcha is not None:
            body['captcha'] = captcha
        else:
            body['captcha'] = '123456'
        body['password'] = self.PASSWORD
        body['confirmPassword'] = self.PASSWORD
        body['product'] = {"value": "31G", "name": "G31", "displayName": "小雨车"}
        body['regCode'] = self.REG_CODE
        return body

    def borrower_auth_sa_login_by_pwd_body(self):
        """'供应链-CH端用户密码登录'"""
        body = dict()
        body['mobile'] = self.user_mobile
        body['password'] = self.PASSWORD
        return body

    def upload_image_body(self, image_type):
        """供应链-上传照片"""
        image_path = Path(home_path[0]) / "resource_files" / "supply_chain" / f"{image_type}.jpg"
        with open(image_path, "rb") as f:  # 打开上传文件
            r = f.read()
        file_image = {"file": ("this_is_photo.jpg", r, "image/jpeg")}
        image_type = {"imageType": image_type}
        body = [image_type, file_image]
        return body

    def borrower_save_base_info_body(self):
        """保存借款人资料"""
        body = dict()
        body['name'] = self.user_name
        body['idCardNumber'] = self.id_card_number
        body['valid'] = '20000122-长期'
        return body


if __name__ == '__main__':
    print(G31UserInputData().borrower_save_base_info_body())
    print(type(G31UserInputData().borrower_save_base_info_body()))
