# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 22:39
# @Author  : Edrain
import xlrd
from xlutils.copy import copy


class UseExcel:
    def __init__(self, file_name=None, sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            self.file_name = '../test_case/test_api_case03.xlsx'
            self.sheet_name = 0
        self.data = self.read_data()

    def read_data(self):
        """获取sheets的内容"""
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_name]
        return tables

    def get_nrows(self):
        """获取单元格的行数"""
        tables = self.data
        return tables.nrows

    def get_cell_value(self, row, column):
        """获取某一个单元格的内容 row:行;column:列"""
        tables = self.data
        cell = tables.cell_value(row, column)
        return cell

    def get_row_data(self, case_id):
        """根据对应case_id找到对应行的 数据"""
        row_num = self.get_row_num(case_id)
        self.get_row_values(row_num)

    def get_row_num(self, case_id):
        """根据对应case_id找到对应行的 行号"""
        num = 0
        columndata = self.get_column_values()
        for data in columndata:
            if case_id in data:
                return num
            num += 1
        return num

    def get_row_values(self, row_num):
        """根据 行号，找到该行的数据"""
        tables = self.data
        row_data = tables.row_values(row_num)
        return row_data

    def get_column_values(self, column=None):
        """根据 列号，找到该列的数据"""
        if column != None:
            column_data = self.data.col_values(column)
        else:
            column_data = self.data.col_values(0)
        return column_data

    def write_value(self, row, column, value):
        """写入到 excel数据，row，column，value"""
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, column, value)
        write_data.save(self.file_name)


if __name__ == '__main__':
    useexcel = UseExcel()
    print("read_data:", useexcel.read_data())
    print("get_nrows:", useexcel.get_nrows())
    print("get_cell_value:", useexcel.get_cell_value(1, 3))

    print("get_row_num:", useexcel.get_row_num("test_11"))
    print("get_row_data:", useexcel.get_row_data("test_05"))

    print("get_row_values:", useexcel.get_row_values(3))
    print("get_column_values:", useexcel.get_column_values(1))


