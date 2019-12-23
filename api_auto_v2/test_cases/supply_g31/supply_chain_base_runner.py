#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15
# @Author  : Edrain
from common.utils.generator_id_card import get_random_id_card
from common.utils.generator_initial_data import get_phone_number, convert_num_to_chinese, get_g31_license_no


class SupplyChainBaseRunner(object):
    user_mobile = get_phone_number()
    user_name = f'哇哈哈{convert_num_to_chinese(user_mobile[-4:])}'
    id_card_number = get_random_id_card(2, 4)
    PASSWORD = '123456a'
    REG_CODE = 1234
    business_license_number = get_g31_license_no()
    CH_MOBILE = 18888881886
    url_param = "?path=31G"
