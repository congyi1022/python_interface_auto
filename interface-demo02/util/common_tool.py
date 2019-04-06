# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 14:38
# @Author  : Edrain
import random
import datetime
from util.use_json import UseJson
from util.addr import addr


class CommonTool:

    def is_contain(self, str_one, str_two):
        """判断一个字符串是否在另一个字符串中。str_one:查找的字符串，str_two:被查找的字符串"""
        return str_two == str_one
        # print(str_one.items() & str_two.items())
        # flag = None
        # if str_one in str_two:
        #     flag = True
        # else:
        #     flag = False
        # return flag

    def phone_code_generator(self):
        """手机号码末尾随机四位数字"""
        # 倒数第一位数字
        first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        second = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        third = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        fourth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9][random.randint(0, 9)]
        # 拼接手机号
        return "1888888{}{}{}{}".format(fourth, third, second, first)

    def write_mobile(self):
        """写入 get_mobile.json 手机号码"""
        get_mobile = self.phone_code_generator()
        use_json = UseJson("../data_config/get_mobile.json")
        use_json.write_data(get_mobile)

    def get_mobile(self):
        """读取 get_mobile.json 里面的 手机号码"""
        # get_mobile = self.phone_code_generator()
        use_json = UseJson("../data_config/get_mobile.json")
        # use_json.write_data(get_mobile)
        get_mobile = use_json.read_data()
        return get_mobile

    def num_chinese(self, num):
        """阿拉伯数字转换为中文汉字"""
        dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                "8": "八", "9": "九"}
        y = u""
        for x in u"" + str(num):
            y += dict[str(x)]
        return y

    def license_no(self):
        """随机生成15位营业执照号"""
        license_no = ""
        for i in range(15):
            num = random.randint(0, 9)
            license_no += str(num)
        return license_no

    def getCheckBit(self, num17):
        """
        获取身份证最后一位，即校验码
        :param num17: 身份证前17位字符串
        :return: 身份证最后一位
        """
        Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        checkCode = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        # checkCode = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        zipWiNum17 = zip(list(num17), Wi)
        S = sum(int(i) * j for i, j in zipWiNum17)
        Y = S % 11
        return checkCode[Y]

    def getAddrCode(self):
        """
        获取身份证前6位，即地址码
        :return: 身份证前6位
        """
        addrIndex = random.randint(0, len(addr) - 1)
        return addr[addrIndex]

    def getBirthday(self, start="1900-01-01", end="2019-01-01"):
        """
        获取身份证7到14位，即出生年月日
        :param start: 出生日期合理的起始时间
        :param end: 出生日期合理的结束时间
        :return: 份证7到14位
        """
        days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
        birthday = datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
        return datetime.datetime.strftime(birthday, "%Y%m%d")

    def getRandomIdCard(self, sex=0):
        """获取随机身份证 :param sex: 性别，默认为男 :return: 返回一个随机身份证"""
        for i in range(15):
            idNumber, addrName = self.getAddrCode()
            idCode = str(idNumber) + self.getBirthday()
            for j in range(2):
                idCode += str(random.randint(0, 9))
            idCode += str(random.randrange(sex, 9, 2))
            idCode += self.getCheckBit(idCode)
            end = idCode[-1]
            # if int(end) % 2 == 0:
            if end in ["0", "2", "4", "6", "8"]:
                # print(end)
                return str(idCode)
            else:
                continue

