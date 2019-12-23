#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/18
# @Author  : Edrain
from enum import Enum


class PlatformProjectEnums(Enum):
    UNIVERSAL = "universal"
    SUPPLY_CHAIN = "supply_chain"


class ContentTypeEnums(Enum):
    APPLICATION_JSON = "application/json"
    FORM_DATA = "form-data"
    SUPPLY_CHAIN_HEADER = "supply_chain_header"
    CUSTOMIZE = "customize"
