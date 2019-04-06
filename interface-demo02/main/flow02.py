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

        self.tool.write_mobile()  # 向get_mobile.json 中写入手机号码

        for i in range(1, rows_count):
            try:
                is_run = self.data.get_is_run(i)
                if is_run:
                    url = self.data.get_request_url(i)
                    method = self.data.get_request_method(i)
                    data = self.data.get_request_excel_data(i)  # 直接读取 excel 中的 data
                    if data.find("${mobile}") != -1:
                        data = data.replace("${mobile}", self.tool.get_mobile())
                    elif data.find("${idCardNumber}") & data.find("${name}") != -1:
                        data = data.replace("${idCardNumber}", self.tool.getRandomIdCard())
                        name = "雨点" + self.tool.num_chinese(self.tool.get_mobile()[-4:])
                        data = data.replace("${name}", name)
                    elif data.find("${businessLicenseNumber}") != -1:
                        data = data.replace("${businessLicenseNumber}", self.tool.license_no())

                    header = self.data.get_request_header(i)  # 获取 excel 中的 header 关键字
                    expect_data = self.data.get_expect_data(i)
                    expect = json.loads(expect_data)

                    depend_case = self.data.is_depend(i)

                    if depend_case != None:
                        self.depend_data = DependentData(depend_case)
                        depend_response_data = self.depend_data.get_value_for_key(i)  # 获取 依赖字段的 响应数据

                    if header == '{"Content-Type":"application/json"}':
                        header_json = eval(header)
                        res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                    elif header == '{"Content-Type":"multipart/form-data"}':
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
                    elif header == 'get_cookie':
                        use_json = UseJson("../data_config/config_header.json")
                        cookie_value = use_json.get_data("Cookie")
                        header_json = {"Content-Type":"application/json", "Cookie": cookie_value}
                        res = self.run_method.run_main(method, url, data, header=header_json, params=data)
                    elif header == "write_Cookie1":
                        use_header = UseHeader(res)
                        use_header.write_cookie()
                    elif header == "get_Cookie1":
                        use_json = UseJson("../data_config/config_cookie.json")
                        cookie = use_json.get_data("apsid")
                        cookies = {"apsid":cookie}
                        res = self.run_method.run_main(method, url, data=data, header=cookies, params=data)
                    else:
                        res = self.run_method.run_main(method, url, data, header, params=data)

                    if self.tool.is_contain(expect, res):
                        self.data.write_result(i, "pass")
                        pass_count.append(i)
                    else:
                        self.data.write_result(i, json.dumps(res))
                        with open(log_file, "a", encoding="utf-8") as lf:
                            lf.write("\n第%s条用例实际结果与期望结果不一致:\n" % i)
                            lf.write("期望结果：%s\n实际结果：%s\n" %(expect, res))
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





