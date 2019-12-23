#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/18
# @Author  : Edrain
import random


def get_phone_number(product=31):
    """
    生成手机号码，手机号码末尾随机四位数字
    :param product:传入产品号
    :return: 手机号
    """
    first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]  # 倒数第一位数字
    second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
    third = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
    fourth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
    return f"1{product}8888{fourth}{third}{second}{first}"  # 拼接手机号


def get_bank_card_number(is_success=True):
    head = 621700
    middle = random.randint(10000000000, 99999999999)
    if is_success:
        last2 = random.randint(3, 9)
        last1 = random.randint(4, 7)
    else:
        last2 = 8
        last1 = 0

    return str(head) + str(middle) + str(last2) + str(last1)


def convert_num_to_chinese(num):
    """阿拉伯数字转换为中文汉字"""
    num_dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                "8": "八", "9": "九"}
    y = u""
    for x in u"" + str(num):
        y += num_dict[str(x)]
    return str(y)


def get_g31_license_no():
    """随机生成15位营业执照号"""
    license_no = ""
    for i in range(15):
        num = random.randint(0, 9)
        license_no += str(num)
    return license_no


if __name__ == "__main__":
    print(get_phone_number())
