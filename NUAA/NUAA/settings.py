# -*- coding: utf-8 -*-

# Scrapy settings for NUAA project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NUAA'

SPIDER_MODULES = ['NUAA.spiders']
NEWSPIDER_MODULE = 'NUAA.spiders'

ITEM_PIPELINES = {
    'NUAA.pipelines.NuaaPipeline': 1,
}
IMAGES_STORE = 'D:\\my homework\\Python\\SelfScrapy'

HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "ded.nuaa.edu.cn",
    "Pragma": "no-cache",
    "Referer": "http://ded.nuaa.edu.cn/netean/com/jbqkcx.asp",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}

COOKIES = {
    'LogonType': '%B0%E0%BC%B6',
    'user': '1613303',
    '_gscu_463181622': '49207429w4jxtf26',
    '_gscbrs_463181622': '1',
    '_ga': 'GA1.3.153033992.1453826677',
    'ASP.NET_SessionId': 'tnr2nw55iuw5l0z1k3yvvf55',
    'ASPSESSIONIDQCSBDQTB': 'EDKJPPODHHMMLDBGOBAGBGBN',
    'ASPSESSIONIDAQRAARSD': 'COLDOLLAGICCDBHEMGKNBADP',
    'CanViewPhotoFilter': '161330219',
    'DedHasLogin': '1',
    'PwdStrengthPass': '1'
}

RETRY_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'NUAA (+http://www.yourdomain.com)'
