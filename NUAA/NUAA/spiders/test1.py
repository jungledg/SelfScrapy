# # -*- coding: utf-8 -*-
# import re
#
# import scrapy
# from scrapy.http import Request, FormRequest
# from scrapy.selector import Selector
# from NUAA.items import NuaaItem
# from NUAA.settings import *
#
#
# class NuaapicSpider(scrapy.Spider):
#     name = "nuaapic"
#     allowed_domains = ["ded.nuaa.edu.cn"]
#     start_urls = ['http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh=161330219']
#
#     college = 1  # 需判断
#     grade = 12
#     major = 1
#     mclass = 1  # 需判断
#     stu_id = 1  # 需判断
#
#     last_stu = 0
#     last_class = 0
#     last_major = 0
#     last_grade = 0
#     last_college = 0
#
#     def __init__(self):
#         self.headers = HEADER
#         self.cookies = COOKIES
#
#     def start_requests(self):
#         for i, url in enumerate(self.start_urls):
#             yield FormRequest(url, meta={'cookiejar': 1}, headers=self.headers, cookies=self.cookies,
#                               callback=self.parse_item)
#
#     def parse_item(self, response):
#         # selector = Selector(response)
#         # f = open('new.txt','a+')
#         # f.write("%s\n%s\n%s" % (response.url, response.headers, response.body))
#         # f.close()
#         for self.college in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16]:
#             for self.grade in range(12, 15):
#                 if self.last_grade == '1':
#                     self.last_grade = '0'
#                 else:
#                     for self.major in range(1, 7):
#                         if self.last_major == '1':
#                             self.last_major = '0'
#                         else:
#                             for self.mclass in range(1, 7):
#                                 if self.last_class == '1':
#                                     self.last_class = '0'
#                                 else:
#                                     for self.stu_id in range(1, 45):
#                                         if self.last_stu == '1':
#                                             self.last_stu = '0'
#                                         else:
#                                             iurl = u"http://ded.nuaa.edu.cn/netean/GetPic.asp?pic=xh&xh={0}{1}{2}{3}{4}".format(
#                                                     self.getRealInfo(self.college),
#                                                     self.grade,
#                                                     self.major,
#                                                     self.getRealInfo(self.mclass),
#                                                     self.getRealInfo(self.stu_id))
#                                             yield Request(url=iurl, meta={'cookiejar': 1}, headers=self.headers,
#                                                           cookies=self.cookies,
#                                                           callback=self.getPic)
#
#     def getPic(self, response):
#         if response.status == '504':
#             url = response.url
#             stu = re.findall(r"\d\d(?=$)", url).pop()
#             cla = re.findall(r"\d\d(?=\d\d$)", url).pop()
#             maj = re.findall(r"\d(?=\d\d\d\d$)", url).pop()
#             # gra = re.findall(r"\d\d(?=\d\d\d\d\d$)", url).pop()
#             # clo = re.findall(r"\d\d(?=\d\d\d\d\d\d\d$)", url).pop()
#             if stu != '01':
#                 self.last_stu = 1
#             else:
#                 if cla != '01':
#                     self.last_class = 1
#                 else:
#                     if maj != '1':
#                         self.last_major = 1
#                     else:
#                         self.last_grade = 1
#         else:
#             item = NuaaItem()
#             f = open('url_record.txt', 'a+')
#             print >> f, response.url
#             f.close()
#             item['image_urls'] = [response.url]
#             return item
#
#     def getRealInfo(self, mclass):
#         if mclass < 10:
#             return '0' + mclass.__str__()
#         else:
#             return mclass.__str__()
