#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16
# @Author  : Edrain
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, ForeignKey, Index, JSON, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, BIT, INTEGER, LONGTEXT, MEDIUMTEXT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ScBorrower(Base):
    __tablename__ = 'sc_borrower'
    __table_args__ = (
        Index('uniq_mobile_merchantid', 'mobile', 'merchant_id', unique=True),
        Index('uniq_idcard_merchantid', 'merchant_id', 'id_card', unique=True)
    )

    id = Column(BIGINT(20), primary_key=True, comment='自增主键')
    code = Column(String(32), nullable=False, unique=True, comment='uuid')
    white_list_id = Column(BIGINT(20), comment='白名单表主键')
    name = Column(String(50), comment='姓名')
    id_card = Column(String(50), nullable=False, comment='身份证号码')
    mobile = Column(String(20), nullable=False, comment='手机号码')





