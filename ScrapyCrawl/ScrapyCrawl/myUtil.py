# -*- coding: utf-8 -*-
# @Time    : 2018/4/29/029 22:28
# @Author  : XuWenzhong
# @Email   : xuwenzhong1994@163.com
# @File    : myUtil.py
# @Version : 1.0.1
# @Software: PyCharm


def iscontainkeywords(title):
    result = False
    with open("keywords.txt", "r") as f:
        for line in f.read().splitlines():
            if line in title:
                result = True
                break
            else:
                result = False
        return result
