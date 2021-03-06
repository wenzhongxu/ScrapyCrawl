# -*- coding: utf-8 -*-
# @Time    : 2018/4/29/029 22:11
# @Author  : XuWenzhong
# @Email   : xuwenzhong1994@163.com
# @File    : creditCrawl.py
# @Version : 1.0.1
# @Software: PyCharm

from items import ScrapycrawlItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from datetime import datetime


class CreditcrawlSpider(CrawlSpider):
    name = 'CreditCrawl'

    def __init__(self, rule):
        self.rule = rule
        self.name = rule["rulename"]
        self.allowed_domains = rule["allowed_domains"].split(",")
        self.start_urls = rule["start_urls"].split(",")

        rule_list = list()
        # 添加'下一页'的规则
        # if rule["NEXT_PAGE"]:
        #     rule_list.append(Rule(LinkExtractor(restrict_xpaths = rule["NEXT_PAGE"])))
        # 添加抽取文章链接的规则
        rule_list.append(Rule(LinkExtractor(
            allow=re.compile(eval(rule["allow_url"])),
            restrict_xpaths=rule["extract_from"]),
            callback='parse_item',
            follow=False))
        self.rules = tuple(rule_list)

        super(CreditcrawlSpider, self).__init__()

    def parse_item(self, response):
        self.log('This is a news page! %s' % response.url)

        newsitem = ScrapycrawlItem()

        title = response.xpath(self.rule["title_xpath"])[0].extract()
        newsitem["_id"] = title
        newsitem["title"] = title

        # 发布时间
        pubtime = response.xpath(self.rule["datetime_xpath"])[0].extract()
        newsitem["datetime"] = pubtime

        # 链接
        newsitem["srcUrl"] = response.url

        author = response.xpath(self.rule["author_xpath"])[0].extract()
        newsitem["author"] = author

        content = response.xpath(self.rule["content_xpath"]).extract()
        # content = updateImgSrc(content, response.url)
        newsitem["content"] = content

        # 频道
        newsitem["orgSrc"] = self.rule["orgsrc"]
        # 网站名称
        newsitem["siteName"] = self.rule["sitename"]
        # 来源——抓取所得
        src = response.xpath(self.rule["src_xpath"])[0].extract()
        newsitem["src"] = src
        # 分类
        newsitem["summary"] = self.rule["summary"]
        # 更新时间
        newsitem["updatetime"] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
        # 是否过滤负面关键字
        newsitem["isfilter"] = self.rule["isfilter"]

        yield newsitem
