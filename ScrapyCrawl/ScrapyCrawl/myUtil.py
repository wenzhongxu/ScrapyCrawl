# -*- coding: utf-8 -*-
# @Time    : 2018/4/29/029 22:28
# @Author  : XuWenzhong
# @Email   : xuwenzhong1994@163.com
# @File    : myUtil.py
# @Version : 1.0.1
# @Software: PyCharm

import re


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


def smart2date(date_string):
    """
        新闻的发布时间解析字符串,转化成标准时间
        如果解析失败,返回当前时间
        样例:
        2015/12/20 12:11:56
        2015\12\20 12:11:56
        2015-12-20 15:43:50
        2015年12月20日 12时00分00秒
    """
    # re_data = r"(\d{1,4}[-|\/|年]\d{1,2}[-|\/|月]\d{1,2}[\s|日]+\\d{1,2}:\d{1,2}:\d{1,2})"
    # re_data = re.compile("(\d{1,4}[-|\/|年])(\d{1,2}[-|\/|月])(\d{1,2}[\s|日]+)(\d{1,2}[\:|时]+)(\d{1,2}[\:|分]+)\
    # (\d{1,2}[秒]?)")
    # re_data = re.compile("\d{1,4}[-|\/|年]\d{1,2}[-|\/|月]\d{1,2}[\s|日]+\d{1,2}[\:|时]+\d{1,2}[\:|分]+\d{1,2}[秒]?")
    re_en = re.compile("(\d{1,4})[-\/](\d{1,2})[-\/](\d{1,2})[\s]+(\d{1,2}):(\d{1,2}):(\d{1,2})")
    re_cn = re.compile(u"(\d{1,4})年(\d{1,2})月(\d{1,2})日.?(\d{1,2})时(\d{1,2})分(\d{1,2})秒")
    re_d_en = re.compile("(\d{1,4})[-\/](\d{1,2})[-\/](\d{1,2})")
    re_d_cn = re.compile(u"(\d{1,4})年(\d{1,2})月(\d{1,2})日")
    match = re_en.search(date_string)
    # 极其愚蠢的正则
    if match:
        date_str = match.group(0)
    else:
        match = re_cn.search(date_string)
        if match:
            date_str = match.group(0)
        else:
            match = re_d_en.search(date_string)
            if match:
                date_str = match.group(0)
            else:
                match = re_d_cn.search(date_string)
                if match:
                    date_str = match.group(0)
                else:
                    date_str = ""
    return date_str

    # re_data = re.compile("\d{1,4}.+\d{1,2}.+\d{1,2}.+\d{1,2}[\:|时]+\d{1,2}[\:|分]+\d{1,2}秒?")
    # match = re_data.search(date_string)
    # if match:
    #     print match.group()
    # else:
    #     print "None"


if __name__ == '__main__':
    print(smart2date(u"2016年02月16日 10:09"))
    print(smart2date(u"2016-02-16 17:30"))
    pass
    # print smart2date("2015年12月20日 12时00分00秒 中国")
    # print smart2date("2015-12-20 15:43:50")
    # re_data = re.compile(u"20\d{1,2}[-|/|\\|年]\d{1,2}[-|/|\\|月]\d{1,2}日?\s+\d{1,2}[:|时]\d{1,2}[:|分]\d{1,2}秒?")
    # re_data = re.compile("((\d{1,4})[-\/](\d{1,2})[-\/](\d{1,2})[\s]+(\d{1,2}):(\d{1,2}):(\d{1,2}))")
    # re_data = re.compile("((\d{1,4})年(\d{1,2})月(\d{1,2})日\s+(\d{1,2})时(\d{1,2})分(\d{1,2})秒)")
    # re_data = re.compile(u"((\d{1,4})[-\/年](\d{1,2})[-\/月](\d{1,2})[日\s]+(\d{1,2})[:时](\d{1,2})[:分](\d{1,2})[秒])")
    # date_string = u"2015-12-20 15:43:50"
    # # date_string = u"2015年12月20日 12时00分00秒 "
    # match = re_data.match(date_string)
    # if match:
    #     print match.groups()
    # else:
    #     print "None"
    # string = "2015年12月20日 12时00分00秒 "
    # if "年" in string && "月" in string && "日" in string:
    #     print(1)
    # else:
    #     print(0)
