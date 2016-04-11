import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re


class NuaaImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print '------------Download....---------------'
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    # def file_path(self, request, response=None, info=None):
    #     re_id = '(?<=xh=)\d+(?=$)'
    #     id = re.compile(re_id)
    #     id = id.findall(request.url)[0]
    #     re_college = '(?<=xh=)\d\d'
    #     college = re.compile(re_college)
    #     college = college.findall(request.url)[0]
    #     re_grade = '(?<=xh=\d\d)\d\d'
    #     grade = re.compile(re_grade)
    #     grade = grade.findall(request.url)[0]
    #     re_major = '(?<=xh=\d{4})\d'
    #     major = re.compile(re_major)
    #     major = major.findall(request.url)[0]
    #     re_mclass = '(?<=xh=\d{5})\d\d'
    #     mclass = re.compile(re_mclass)
    #     mclass = mclass.findall(request.url)[0]
    #     filename = u'full/{0}/{1}/{2}/{3}/{4}'.format(college, grade, major, mclass, id)
    #     return filename
