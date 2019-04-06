# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 17:17
# @Author  : Edrain
import json


class UseJson:

    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = '../data_config/config_header.json'
        self.data = self.read_data()

    def read_data(self):
        """读取json文件"""
        with open(self.file_path) as fp:
            data = json.load(fp)
            # data = fp.read()
            return data

    def get_data(self, key):
        """根据关键字获取数据"""
        '''
            dict['key']只能获取存在的值，如果不存在则触发KeyError
            dict.get(key, default=None)，返回指定键的值，如果值不在字典中返回默认值None
            excel文件中请求数据有可能为空，所以用get方法获取
        '''
        # return self.data[key]
        return self.data.get(key)

    def write_data(self, data):
        """将cookies数据写入json文件"""
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    usejson = UseJson()
    print(usejson.read_data())
    print(type(usejson.read_data()))
    # print(usejson.get_data("edrain"))
    # usejson.write_data("testx")

