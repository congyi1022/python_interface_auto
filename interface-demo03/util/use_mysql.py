# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 18:19
# @Author  : Edrain
import pymysql

from util.use_json import UseJson


class UseMySql:

    def __init__(self):
        self.connect = pymysql.connect(host='127.0.0.1',
                                  port=3306,
                                  user='edrain',
                                  password='thisispassword',
                                  charset='utf8'
                                  )
        self.cursor = self.connect.cursor()  # 游标

    def __del__(self):
        """析构函数，实例删除时触发"""
        # print("开始回收对象")
        self.cursor.close()  # 关闭游标
        self.connect.close()  # 关闭连接
        # print("回收对象完毕")

    def select_db(self, sql):
        """sql查询数据库"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()  # 获取所有查询结果
        return result

    def change_db(self, sql):
        """sql更改数据库"""
        try:
            self.cursor.execute(sql)  # 执行sql
            self.connect.commit()  # 提交更改
            print("SQL执行成功。")
        except Exception as e:
            self.connect.rollback()  # 回滚
            print("SQL执行失败，错误信息：", e)

    # def select_db1(self, sql):
    #     """封装数据库查询"""
    #     connect = self.get_mysql_connect()
    #     cursor = connect.cursor()  # 获取连接
    #     cursor.execute(sql)  # 建立游标
    #     result = cursor.fetchall()  # 获取所有查询结果
    #     cursor.close()  # 关闭游标
    #     connect.close()  # 关闭连接
    #     return result

    def select_borrowercode(self):
        """根据手机号查询sc_borrower.code"""
        # mobile = 18888884356
        use_json = UseJson("../data_config/get_mobile.json")
        mobile = use_json.read_data()
        str = "SELECT * FROM supplychain.`sc_borrower` WHERE mobile={}".format(mobile)
        result = self.select_db(str)
        code = result[0][1]  # 放回的是一个元组，通过下标访问元组
        use_json = UseJson("../data_config/borrowerCode.json")
        use_json.write_data({"borrowerCode": "{}".format(code)})


if __name__ == '__main__':
    usemysql = UseMySql()
    usemysql.select_borrowercode()
    # mobile = 18888884356
    # str = "SELECT * FROM supplychain.`sc_borrower` WHERE mobile = {}".format(mobile)
    # result = usemysql.select_db(str)
    # print(result)
    # print(result[0][1])  # 放回的是一个元组，通过下标访问元组
    # print(usemysql.change_db("UPDATE supplychain.sc_borrower SET `name`='小雨点2166' WHERE id= 261"))
    # print(usemysql.change_db("UPDATE supplychain.sc_borrower SET `name`='小雨2166' WHERE id= 261"))


