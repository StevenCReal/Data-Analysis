# -*- coding: utf-8 -*-
import scrapy
from sexyGirls.items import SexygirlsItem  # 在sexyGirls文件夹下包括__init__.py，Python就会把文件夹当作一个package，里面的py文件就能够在外面被import了
from urllib.parse import urljoin


class sexyGirlSpider(scrapy.Spider):
    name = "sexyGirl"
    allowed_domains = ["win4000.com"]
    start_urls = ['http://www.win4000.com/meinvtag4_1.html']

    def parse(self, response):
        list = response.xpath("string(//div[@class='tab_box']//div[@class='']//ul[@class='clearfix']//li//a//@href)").extract()
        for girl in list:
            imgUrl = girl
            imgUrl = "www.win4000.com" + girl
            print('我是: '+ imgUrl)
            yield scrapy.Request(imgUrl, callback=self.content)

        next_page = response.xpath("string(//div[@class = 'pages']//div//a[contains(text(),'下一页')]//@href)").extract_first()  # 根据文本查找标签
        # next_page = urljoin("https://www.mn52.com/xingganmeinv/", next_page)
        if next_page is not None:
            # 下一页
            yield scrapy.Request(next_page, callback=self.parse)

    def content(self, response):
        item = SexygirlsItem()
        item.name = response.xpath(
            "//div[@class='ptitle']//h1//text()")
        item.ImgUrl = response.xpath("string(//div[@class='Detail-tjList']//ul[@id='adwallpaper']//li//a//span//img//@src)").extract_first()
        yield item
