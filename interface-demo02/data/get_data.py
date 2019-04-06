# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 17:54
# @Author  : Edrain
from data import data_config
from util.use_excel import UseExcel
from util.use_json import UseJson


class GetData:

    def __init__(self):
        self.use_excel = UseExcel()

    def get_case_rows(self):
        """获取excel的行数，得到的就是case的个数"""
        return self.use_excel.get_nrows()

    def get_is_run(self, row):
        """获取是否执行"""
        flag = None
        column = int(data_config.get_run())
        run_model = self.use_excel.get_cell_value(row, column)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    def get_request_method(self, row):
        """获取请求方式"""
        column = int(data_config.get_request_way())
        request_method = self.use_excel.get_cell_value(row, column)
        return request_method

    def get_request_url(self, row):
        """获取url"""
        column = int(data_config.get_url())
        url = self.use_excel.get_cell_value(row, column)
        return url

    def get_request_header(self, row):
        """获取请求头 header"""
        column = int(data_config.get_request_header())
        data = self.use_excel.get_cell_value(row, column)
        if data == " ":
            return None
        else:
            return data

    def get_header_value(self, row):
        """获取头关键字 拿到data数据"""
        use_json = UseJson('../data_config/request_header.json')
        request_header = use_json.get_data(self.get_request_header(row))
        return request_header

    def get_request_data(self, row):
        """获取请求数据"""
        column = int(data_config.get_request_data())
        data = self.use_excel.get_cell_value(row, column)
        if data == "":
            return None
        return data

    def get_request_excel_data(self, row):
        """获取 excel 中请求的数据"""
        colunm = int(data_config.get_request_data())
        excel_data = self.use_excel.get_cell_value(row, colunm)
        return excel_data

    def get_request_excel_data_wrapper(self, row, fun):
        """获取 excel 中请求的数据"""
        request_excel_data = self.get_request_excel_data(row)
        return fun(request_excel_data)

    def get_data_values(self, row):
        """通过获取请求关键字拿到data数据"""
        use_json = UseJson('../data_config/request_data.json')
        request_data = use_json.get_data(self.get_request_data(row))
        return request_data

    def get_data_values_wrapper(self, row, func):
        data_values = self.get_data_values(row)
        return func(data_values)

    def get_expect_data(self, row):
        """获取预期结果"""
        column = int(data_config.get_expect())
        expect= self.use_excel.get_cell_value(row, column)
        return expect

    def write_result(self, row, value):
        """写入数据"""
        column = int(data_config.get_result())
        self.use_excel.write_value(row, column, value)

    def get_depend_key(self, row):
        """获取依赖数据的 key"""
        column = int(data_config.get_data_depend())
        depend_key = self.use_excel.get_cell_value(row, column)
        if depend_key == "":
            return None
        else:
            return depend_key

    def is_depend(self, row):
        """判断是否有 case依赖"""
        column = int(data_config.get_case_depend())
        depend_case_id = self.use_excel.get_cell_value(row, column)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_depend_field(self, row):
        """获取请求依赖 字段"""
        column = int(data_config.get_field_depend())
        data = self.use_excel.get_cell_value(row, column)
        if data == "":
            return None
        else:
            return data


# if __name__ == '__main__':
#     getdata = GetData()
#     print(getdata.get_case_rows())
#     print(getdata.get_depend_field(12))



