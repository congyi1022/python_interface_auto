# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 22:39
# @Author  : Edrain
import openpyxl
import xlrd
from xlutils.copy import copy
import pandas as pd


class UseExcel:
    def __init__(self, file_name=None, sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            self.file_name = '../test_case/test_api_case03.xlsx'
            self.sheet_name = 1
        self.df = self.read_data()

    def read_data(self):
        """获取sheets的内容"""
        datas = pd.read_excel(self.file_name, sheet_name=self.sheet_name)
        return datas
        # data = xlrd.open_workbook(self.file_name)
        # tables = data.sheets()[self.sheet_name]
        # return tables

    def get_nrows(self):
        """获取单元格的行数"""
        rows = self.df.shape[0]
        return rows
        # tables = self.data
        # return tables.nrows

    def get_cell_value(self, row, column):
        """获取某一个单元格的内容 row:行;column:列"""
        cell = self.df.iloc[row, column]
        return cell
        # tables = self.data
        # cell = tables.cell_value(row, column)
        # return cell

    def get_row_values(self, row_num):
        """根据 行号，找到该行的数据"""
        row_data = self.df.loc[row_num].to_dict()
        return row_data

    def get_column_values(self, column=None):
        """根据 列号，找到该列的数据"""
        # row_data = self.df.loc[column].to_dict()
        # return row_data
        if column != None:
            column_data =self.df.loc[column].to_dict()
        else:
            column_data = self.df.loc[0].to_dict()
        return column_data

    def get_row_num(self, case_id):
        """根据对应case_id找到对应行的 行号"""
        num = 0
        # columndata = self.get_column_values()
        columndata = self.df.iloc[:, 0]
        for data in columndata:
            if case_id in data:
                return num
            num += 1
        return num

    def get_row_data(self, case_id):
        """根据对应case_id找到对应行的 数据"""
        row_num = self.get_row_num(case_id)
        return self.get_row_values(row_num)

    def write_value(self, row, column, value):
        """写入到 excel数据，row，column，value"""
        wb = openpyxl.load_workbook(self.file_name)  # 打开excel文档
        # sheet = wb['Sheet1']
        sheet = wb.worksheets[self.sheet_name]  # 访问sheet页的第一页
        sheet.cell(row=row+2, column=column+1, value=value)  # 将值写入某指定单元格
        wb.save(self.file_name)  # 保存excel

    def excel_update(self, col, row, value):
            df = pd.read_excel(self.file_name)
            df.loc[col, row] = value
            df.to_excel(self.file_name, index=None)


if __name__ == '__main__':
    useexcel = UseExcel('../test_case/test.xlsx', 0)
    print("read_data:", useexcel.read_data())
#     # print("get_nrows:", useexcel.get_nrows())
#     # print("get_cell_value:", useexcel.get_cell_value(4, 0))
#     # print("get_row_values:", useexcel.get_row_values(5))
#     # print("get_column_values:", useexcel.get_column_values(1))
#     print("get_row_num:", useexcel.get_row_num("test_02"))
#     # print("get_row_data:", useexcel.get_row_data("test_05"))
#     print("write_value:", useexcel.write_value(2, 3, 'test003'))
#     print("excel_update:", useexcel.excel_update(1, 3, 'test003'))



