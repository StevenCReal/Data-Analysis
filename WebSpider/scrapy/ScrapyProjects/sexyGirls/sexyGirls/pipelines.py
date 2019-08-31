# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re


class SexygirlsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield Request(image_url)

    def file_path(self, request, response=None, info=None):
        name = request.meta['item']
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        image_guid = request.url.split('/')[-1]
        filename = u'full/{0}/{1}'.format(
            name, image_guid)  # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item
