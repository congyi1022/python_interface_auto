#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7
# @Author  : Edrain
from time import sleep

from db_dal.db_model.supply_chain_model import ScBorrower
from common.utils.logger import Logger
from biz_service.mysql_service import initial_connect


class SupplyChainDBData(object):

    def __init__(self):

        # 初始化数据库链接
        self.session = initial_connect("supplychain")
        self.wait_time = 2

    def query_borrower_code_by_mobile(self, mobile):
        """
        通过手机号查询borrower_code
        :param mobile: 31G 用户注册的手机号
        :return: borrower_code
        """
        try:
            for item in range(self.wait_time):
                data = self.session.query(ScBorrower).filter(ScBorrower.mobile == mobile).first()
                sleep(0.5)
                if data is not None:
                    borrower_code = data.code
                    Logger().info(f'【supplychain.sc_borrower】表中有该条数据,注册成功，borrowerCode为：{borrower_code}')
                    self.session.close()
                    return borrower_code
                else:
                    Logger().warning("【supplychain.sc_borrower】表中无该条数据,查询失败")
        except Exception as error:
            Logger().info(error)
