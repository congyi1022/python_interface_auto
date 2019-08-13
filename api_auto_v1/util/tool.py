#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6
# @Author  : Edrain
import random


class Tool(object):

    def upload_image(self):
        """上传照片"""
        with open("../../data_config/upload_photo.jpg", "rb") as f:  # 打开上传文件
            r = f.read()
        file_image = {"file": ("this_is_photo.jpg", r, "image/jpeg")}
        return file_image

    def num_chinese(self, num):
        """阿拉伯数字转换为中文汉字"""
        dict = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七",
                "8": "八", "9": "九"}
        y = u""
        for x in u"" + str(num):
            y += dict[str(x)]
        return str(y)

