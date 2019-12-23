#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16
# @Author  : Edrain
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common.utils.logger import Logger
from biz_service.read_env_service import ReadEnv
from db_dal.db_model.supply_chain_model import ScBorrower
from common.enums.db_enums import DBConfigEnums, DBEnums


def initial_connect(database):
    """初始化连接数据库"""
    try:
        db_ip = ReadEnv().read_env(DBConfigEnums.DB_IP.value)
        db_port = ReadEnv().read_env(DBConfigEnums.DB_PORT.value)
        db_password = ReadEnv().read_env(DBConfigEnums.DB_PASSWORD.value)
        db_username = ReadEnv().read_env(DBConfigEnums.DB_USERNAME.value)
        db_info = f'mysql+pymysql://{db_username}:{db_password}@{db_ip}:{db_port}/{database}'

        # 初始化数据库链接
        engine = create_engine(db_info)
        # 创建DBSession类型
        db_session = sessionmaker(bind=engine)
        # 创建session，实例化
        new_session = db_session()
        return new_session
    except Exception as error_info:
        Logger().error("初始化数据库链接失败：" + str(error_info))


if __name__ == "__main__":
    session = initial_connect(DBEnums.SUPPLYCHAIN.value)
    # rows = session.query(ScBorrower).filter(ScBorrower.mobile == '131888875201').one()
    rows = session.query(ScBorrower).filter(ScBorrower.mobile == '13188887520').first()
    # print(rows)  # 数据不存在：.one raise错误，.first 输出None
    print(rows.name, rows.id_card)
