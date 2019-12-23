#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15
# @Author  : Edrain
import pytest

from common.utils.logger import Logger
from project_interface.supplychain.enums.resource_files_enums import ResourceFilesSupplyChainUserEnums
from project_interface.supplychain.enums.supply_chain_base_runner_enums import SupplyChainCaptchaEnums
from project_interface.supplychain.interface.sc_pre_loan.user_pre_api.borrower_auth_interface import \
    ScPreLoanBorrowerAuthInterface
from project_interface.supplychain.interface.sc_pre_loan.user_pre_api.borrower_interface import \
    ScPreLoanBorrowerInterface
from project_interface.supplychain.interface.sc_pre_loan.user_pre_api.upload_interface import \
    ScPreLoanUploadImageInterface
from test_cases.supply_g31.supply_chain_base_runner import SupplyChainBaseRunner


class TestSupplyChainWorkFlow31gUser(SupplyChainBaseRunner):

    def test_work_flow_01(self):
        """发送注册验证码"""
        ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(self.user_mobile,
                                                                SupplyChainCaptchaEnums.USER_LOGIN_CAPTCHA.value)

    def test_work_flow_02(self):
        """注册新用户"""
        ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(self.user_mobile,
                                                                SupplyChainCaptchaEnums.USER_LOGIN_CAPTCHA.value)
        ScPreLoanBorrowerAuthInterface().borrower_reg_by_sms_code()

    def test_work_flow_03(self):
        """注册新用户上传step1"""
        ScPreLoanBorrowerAuthInterface().borrower_auth_sms_code(self.user_mobile,
                                                                SupplyChainCaptchaEnums.USER_LOGIN_CAPTCHA.value)
        ScPreLoanBorrowerAuthInterface().borrower_reg_by_sms_code()
        resp = ScPreLoanBorrowerAuthInterface().borrower_auth_sa_login_by_pwd()
        token = resp["accessToken"]
        if resp["errorCode"]['code'] == "SUCCESSFULLY":
            Logger().info("【======注册成功======】token：{}".format(token))
        ScPreLoanUploadImageInterface().upload_image(token, ResourceFilesSupplyChainUserEnums.ID_CARD_FRONT_IMAGE.value)
        ScPreLoanUploadImageInterface().upload_image(token, ResourceFilesSupplyChainUserEnums.ID_CARD_BACK_IMAGE.value)
        ScPreLoanUploadImageInterface().upload_image(token, ResourceFilesSupplyChainUserEnums.HEAD_IMAGE.value)
        ScPreLoanBorrowerInterface().borrower_save_base_info(token)


if __name__ == '__main__':
    pytest.main()
