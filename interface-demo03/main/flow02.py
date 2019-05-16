# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 17:37
# @Author  : Edrain
import json
import requests

from data.dependent_data import DependentData
from data.get_data import GetData
from util.common_tool import CommonTool
from util.print_log import initLogging
from util.send_get_post import SendGetPost
from util.send_mail import SendEmail
from util.use_header import UseHeader
from util.use_json import UseJson


class BaseFlow:

    def __init__(self):
        self.run_method = SendGetPost()
        self.data = GetData()
        self.tool = CommonTool()
        self.send_mail = SendEmail()

    # def mobile(self, data):
    #     # data["mobile"] = self.tool.phone_code_generator()
    #     data["mobile"] = self.__mobile__
    #     return data

    def base_run(self):
        res = None
        pass_count = []
        fail_count = []
        no_run_count = []
        rows_count = self.data.get_case_rows()

        log_file = "../log/interface-demo02.log"     # 每次执行用例前，将log日志文件清空数据
        with open(log_file, "w") as lf:
            lf.seek(0, 0)       # 加上lf.seek(0)，把文件定位到position 0；若没有这句话，文件是定位到数据最后，truncate也是从最后这里删除。
            lf.truncate()

        # self.__mobile__ = self.tool.phone_code_generator()
        self.tool.write_mobile()  # 向get_mobile.json 中写入手机号码

        for i in range(1, rows_count):
            try:
                is_run = self.data.get_is_run(i)
                if is_run:
                    url = self.data.get_request_url(i)
                    method = self.data.get_request_method(i)
                    # data = self.data.get_request_data(i)  # 获取excel 中的 data
                    data = self.data.get_request_excel_data(i)  # 直接读取 excel 中的 data
                    if data.find("${mobile}") != -1:
                        # data = data.replace("${mobile}", self.__mobile__)
                        data = data.replace("${mobile}", self.tool.get_mobile())
                    elif data.find("${idCardNumber}") & data.find("${name}") != -1:
                        data = data.replace("${idCardNumber}", self.tool.getRandomIdCard())
                        name = "雨点" + self.tool.num_chinese(self.tool.get_mobile()[-4:])
                        data = data.replace("${name}", name)
                    elif data.find("${businessLicenseNumber}") != -1:
                        data = data.replace("${businessLicenseNumber}", self.tool.license_no())

                    # data = self.data.get_request_excel_data_wrapper(i, self.mobile)  # 直接读取 excel 中的 data
                    # data = self.data.get_data_values(i)
                    # data = self.data.get_data_values_wrapper(i, self.mobile)
                    header = self.data.get_request_header(i)  # 获取 excel 中的 header 关键字
                    # header_json = self.data.get_header_value(i)  # 获取 json 中的 header_key 对应的头文件数据
                    expect_data = self.data.get_expect_data(i)
                    expect = json.loads(expect_data)

                    depend_case = self.data.is_depend(i)

                    if depend_case != None:
                        self.depend_data = DependentData(depend_case)
                        depend_response_data = self.depend_data.get_value_for_key(i)  # 获取 依赖字段的 响应数据
                        # depend_key = self.data.get_depend_field(i)  # 获取 请求依赖的 key
                        # data[depend_key] = depend_response_data  # 将依赖case的响应返回中某个字段的value赋值给该接口请求中某个参数

                    if header == '{"Content-Type":"application/json"}':
                        header1 = eval(header)
                        # header1 = {"Content-Type": "application/json"}
                        # data = json.dumps(data)
                        # res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                        res = self.run_method.run_main(method, url, data, header=header1, params=data)
                    elif header == '{"Content-Type":"multipart/form-data"}':
                        # data = {"imageType": "ID_CARD_FRONT_IMAGE"}
                        data = eval(data)  # 把 str 转成 dict
                        with open("H:/wahh.jpg", "rb") as f:  # 打开上传文件
                            r = f.read()
                        files = {"file": ("wahh.jpg", r, "image/jpeg")}
                        use_json = UseJson("../data_config/config_header.json")
                        header_json = use_json.read_data()
                        # header_json = {  # "Content-Type": "multipart/form-data",  # 不要画蛇添足写这一句
                        #     "Cookie": "SESSION=NGExN2Y0MzUtNjVhNy00MDRkLWIyZjItMGFjZWVlMDFiZjM5"}
                        response = requests.post(url=url, data=data, files=files, headers=header_json)  # 获取返回请求
                        res = response.text
                        # res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                    elif header == 'get_cookie':
                        use_json = UseJson("../data_config/config_header.json")
                        cookie_value = use_json.get_data("Cookie")
                        # a = json.dumps(cookie1)
                        # cookie = re.findall(r'{(.*?)}', a)
                        # cookie_value = cookie1['Cookie']
                        header_json = {"Content-Type":"application/json", "Cookie": cookie_value}
                        res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                    elif header == "write_Cookie1":
                        # res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                        use_header = UseHeader(res)
                        use_header.write_cookie()
                    elif header == "get_Cookie1":
                        use_json = UseJson("../data_config/cookie.json")
                        cookie = use_json.get_data("apsid")
                        cookies = {"apsid":cookie}
                        res = self.run_method.run_main(method, url, data=data, header=cookies, params=data)
                    else:
                        res = self.run_method.run_main(method, url, data, header, params=data)

                    if self.tool.is_contain(expect, res):
                        self.data.write_actual(i, json.dumps(res, ensure_ascii=False))  # 返回值为中文时，不乱码
                        self.data.write_result(i, "PASS")
                        pass_count.append(i)
                    else:
                        self.data.write_actual(i, json.dumps(res, ensure_ascii=False))
                        self.data.write_result(i, "FAIL")
                        with open(log_file, "a", encoding="utf-8") as lf:
                            lf.write("\n第{}条用例实际结果与期望结果不一致:\n".format(i))
                            lf.write("期望结果：{}\n实际结果：{}\n".format(expect, res))
                        fail_count.append(i)
                else:
                    no_run_count.append(i)

            except Exception as e:
                self.data.write_result(i, str(e))
                with open(log_file, "a", encoding="utf-8") as lf:
                    lf.write("\n第%s条用例报错：\n" % i)
                initLogging(log_file, e)
                fail_count.append(i)

        # self.send_mail.send_main(pass_count,fail_count,no_run_count)


if __name__ == '__main__':
    run = BaseFlow()
    run.base_run()





