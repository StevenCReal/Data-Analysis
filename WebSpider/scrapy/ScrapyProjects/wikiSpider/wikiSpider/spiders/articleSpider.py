from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor


class ArticleSpider(CrawlSpider):
    name = 'article'
    allowed_domains = ['wikihow.com']
    start_urls = [
        'https://www.wikihow.com/Make-Sex-Last-Longer',
        'https://www.wikihow.com/Talk-to-Your-Wife-or-Girlfriend-about-Oral-Sex'
    ]
    rules = [
        Rule(LinkExtractor(allow=('^/[A-Z]+'), ),
             callback="parse_item",
             follow=True)
    ]

    def parse_item(self, response):
        item = Article()
        try:
            title = response.xpath("//h1/a/text()")[0].extract()
        except IndexError:
            print("nothing found!")
        else:
            print("Title is: " + title)
            item['title'] = title
            return item
