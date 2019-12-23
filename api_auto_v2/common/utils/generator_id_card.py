#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/18
# @Author  : Edrain


import datetime
import random

from common.utils.id_card_area_code import area_code

'''
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:
1、地址码 
表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
2、出生日期码 
表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 
3、顺序码 
表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。 
4、校验码计算步骤
    (1)十七位数字本体码加权求和公式 
    S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
    Ai:表示第i位置上的身份证号码数字值(0~9) 
    Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
    (2)计算模 
    Y = mod(S, 11)
    (3)根据模，查找得到对应的校验码 
    Y: 0 1 2 3 4 5 6 7 8 9 10 
    校验码: 1 0 X 9 8 7 6 5 4 3 2
'''


def get_check_bit(num17):
    """
    获取身份证最后一位，即校验码
    :param num17: 身份证前17位字符串
    :return: 身份证最后一位
    """
    wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    zip_wi_num17 = zip(list(num17), wi)
    S = sum(int(i) * j for i, j in zip_wi_num17)
    Y = S % 11
    return check_code[Y]


def get_area_code():
    """
    获取身份证前6位，即地址码
    :return: 身份证前6位
    """
    addr_index = random.randint(0, len(area_code) - 1)
    return area_code[addr_index]


def get_birthday(start="1900-01-01", end="2019-01-01"):
    """
    获取身份证7到14位，即出生年月日
    :param start: 出生日期合理的起始时间
    :param end: 出生日期合理的结束时间
    :return: 份证7到14位
    """
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthday = datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
    return datetime.datetime.strftime(birthday, "%Y%m%d")


def get_random_id_card(second_last=2, last=1):
    """
    随机生成身份证
    :param second_last: 倒数第二位
    :param last: 最后一位
    :return:
    """
    while True:
        sex = random.randint(0, 1)  # 女为0，男为1
        id_number, addr_name = get_area_code()
        id_code = str(id_number) + get_birthday()
        for j in range(2):  # 随机生成年月日后2位
            id_code += str(random.randint(0, 9))
        id_code += str(random.randrange(sex, 9, 2))  # 生成身份证倒数第二位（选出0<=number<9 间的偶数）
        id_code += get_check_bit(id_code)  # 推算出身份证最后一位
        if str(second_last) == id_code[-2]:
            if str(last) == id_code[-1]:
                return id_code
        else:
            continue


if __name__ == "__main__":
    print("身份证号码是：", get_random_id_card())
