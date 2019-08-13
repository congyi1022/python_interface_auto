#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7
# @Author  : Edrain
import datetime
import random


class UseData(object):

    def phone_generator(self):
        """手机号码末尾随机四位数字"""
        # 倒数第一位数字
        first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        third = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        fourth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        # 拼接手机号
        return "1318888{}{}{}{}".format(fourth, third, second, first)

    def get_random_id_card(self):
        """模型mock身份证"""
        sex = random.randint(0, 1)  # 女为0，男为1
        for i in range(30):
            id_number, addr_name = self.get_addr_code()
            id_code = str(id_number) + self.get_birthday()
            for j in range(2):  # 随机生成年月日后2位
                id_code += str(random.randint(0, 9))
            id_code += str(random.randrange(sex, 9, 2))  # 生成身份证倒数第二位（选出0<=number<9 间的偶数）
            id_code += self.get_check_bit(id_code)  # 推算出身份证最后一位
            end = id_code[-1]
            if end in ["1", "2", "3"]:
                second_to_last = id_code[-2]
                if second_to_last in ["1", "2", "3"]:
                    return id_code
            else:
                continue

    def get_check_bit(self, num17):
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

    def get_addr_code(self):
        """
        获取身份证前6位，即地址码
        :return: 身份证前6位
        """
        from util.addr import addr
        addr_index = random.randint(0, len(addr) - 1)
        return addr[addr_index]

    def get_birthday(self, start="1900-01-01", end="2019-01-01"):
        """
        获取身份证7到14位，即出生年月日
        :param start: 出生日期合理的起始时间
        :param end: 出生日期合理的结束时间
        :return: 份证7到14位
        """
        days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
        birthday = datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
        return datetime.datetime.strftime(birthday, "%Y%m%d")


