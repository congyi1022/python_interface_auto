#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25
# @Author  : Edrain
import pytest

from biz_service.funding_serivce import FundingService
from test_cases.supply_g31.supply_chain_base_runner import SupplyChainBaseRunner


class TestSupplyChainFunding(SupplyChainBaseRunner):
    test_funding_data = [("31G", "20192231G"), ("31G", "20198831G")]

    @pytest.mark.parametrize("product_no, loan_number", test_funding_data)  # 通过parametrize，传入参数
    def test_funding_g31(self, product_no, loan_number):
        """招商银行 放款"""
        FundingService().funding_zhaoshang_pay(product_no, loan_number)

    @pytest.mark.parametrize("loan_number", ["20192231G", "20198831G"])
    def test_funding_chinapay_batchPay(self, loan_number):
        """银联 放款"""
        FundingService().funding_chinapay_batchPay(loan_number)
