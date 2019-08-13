#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9
# @Author  : Edrain
import pymysql
import yaml

from api_auto_v1.util.use_yaml import UseYaml


class UseMysql(object):

    def __init__(self):
        conf = yaml.safe_load(open("../../data_config/env.yaml"))
        host = conf["mysql"]["host"]
        port = conf["mysql"]["port"]
        user = conf["mysql"]["user"]
        password = conf["mysql"]["password"]
        charset = conf["mysql"]["charset"]
        self.connect = pymysql.connect(host=host,
                                       port=port,
                                       user=user,
                                       password=password,
                                       charset=charset
                                       )
        self.cursor = self.connect.cursor()  # 游标
        self.use_yaml = UseYaml()

    def __del__(self):
        """析构函数，实例删除时触发"""
        # print("开始回收对象")
        self.cursor.close()  # 关闭游标
        self.connect.close()  # 关闭连接

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

    def select_borrower_code(self):
        """根据手机号查询code"""
        user_mobile = self.use_yaml.read_yaml_user_mobile()
        str = "SELECT * FROM mysql.user WHERE mobile={}".format(user_mobile)
        result = self.select_db(str)
        code = result[0][1]  # 放回的是一个元组，通过下标访问元组
        self.use_yaml.write_yaml_borrower_code_sql(code)
        return code

