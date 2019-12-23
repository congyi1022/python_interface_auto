#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/09/11
# @Author  : Edrain
import time
import redis
from common.enums.host_enums import RedisHostEnums
from common.enums.redis_enums import SupplyChainRedisEnums
from common.utils.logger import Logger
from biz_service.read_env_service import *


class RedisService(object):
    """Redis相关服务"""

    def __init__(self):
        self.redis = redis.Redis(host=ReadEnv().read_env(RedisHostEnums.REDIS_URL.value),
                                 port=ReadEnv().read_env(RedisHostEnums.REDIS_PORT.value))

    def get_redis_value(self, key_content, key_param):
        """
        通过传入key，获取redis里面存储的value值
        :param key_content:
        :param key_param: redis的key中需要传入的参数
        :return: 获取Redis的值
        """
        if type(key_param) != str:
            key_param = str(key_param)
        for item in range(5):
            value_bytes = self.redis.get(f'{key_content}:{key_param}')
            if value_bytes is not None:
                value = str(value_bytes, encoding="utf-8")
                Logger().info(f'【通过{key_param}获取Redis的值】: {value}')
                return value
            else:
                Logger().info("【正在获取Redis的值，请稍等...】")
                time.sleep(1)
        Logger().info("【无法查询获取Redis的值...】")


if __name__ == "__main__":
    get_value = RedisService().get_redis_value(SupplyChainRedisEnums.G31_USER_REGISTERED_CAPTCHA.value, 13188882600)
    print(get_value)
    print(type(get_value))
