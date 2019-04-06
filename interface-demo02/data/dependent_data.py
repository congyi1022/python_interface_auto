# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 15:17
# @Author  : Edrain
import base64
import hashlib

from util.common_tool import CommonTool
from util.use_excel import UseExcel
from util.send_get_post import SendGetPost
from data.get_data import GetData
from jsonpath_rw import parse


class DependentData:

    def __init__(self, case_id):
        self.case_id = case_id
        self.use_excel = UseExcel()
        self.run_method = SendGetPost()
        self.data = GetData()
        self.tool = CommonTool()

    def get_case_row_data(self):
        """通过 case_id 去获取依赖 case_id 的整行数据"""
        row_data = self.use_excel.get_row_data(self.case_id)
        return row_data

    def run_dependent(self):
        """执行依赖测试，获取结果"""
        row_num = self.use_excel.get_row_num(self.case_id)
        request_data = self.data.get_request_excel_data(row_num)  # 直接读取 excel 中的 data
        if request_data.find("${mobile}") != -1:
            request_data = request_data.replace("${mobile}", self.tool.get_mobile())

        header = self.data.get_request_header(row_num)
        header = eval(header)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = self.run_method.run_main(method, url, data=request_data, header=header, params=request_data)
        return res

    def get_value_for_key(self, row):
        """获取依赖字段的响应数据，通过执行依赖测试case来获取响应数据，响应中某个字段数据作为依赖key的value"""
        depend_data = self.data.get_depend_key(row)  # 获取依赖的返回数据 key
        response_data = self.run_dependent()  # 执行依赖 case 返回结果
        get_depend_data = [match.value for match in parse(depend_data).find(response_data)][0]
        if depend_data == "accessToken":
            # get_depend_data = hashlib.md5(get_depend_data.encode(encoding='UTF-8')).hexdigest()  # md5加密
            get_depend_data = base64.b64encode(get_depend_data.encode('utf-8')).decode("utf-8")  # base64加密
            self.use_file(get_depend_data)
        return get_depend_data

    def md5(self):
        str = '387ff00e-1a54-49b3-87ca-a95ad3c9e08a'
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    def base64(self):
        a = "39397778-f129-41f4-ba28-68af53f5728c"
        jm = base64.b64encode(a.encode('utf-8'))
        b = str(jm)
        base = b[2:-1]
        return base

    def use_file(self, header_cookie):
        config_header = "../data_config/config_header.json"
        with open(config_header, "w") as ch:
            ch.write('{{"Cookie": "SESSION={}"}}'.format(header_cookie))


if __name__ == '__main__':
    dependentdata = DependentData("test_10")
    # print(dependentdata.get_case_row_data())
    # print(dependentdata.run_dependent())
    print(dependentdata.get_value_for_key(11))
    # print("md5:", dependentdata.md5())
    # print("base64:", dependentdata.base64())
    # dependentdata.use_file()
