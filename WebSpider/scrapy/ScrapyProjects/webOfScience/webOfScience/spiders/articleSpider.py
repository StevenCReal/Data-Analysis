from scrapy import Spider, Request


class ArticleSpider(Spider):        # All spiders must inherit from this class
    name = "article"
    # 定义spider名字的字符串(string)。spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。
    # name是spider最重要的属性，而且是必须的。
    # 一般做法是以该网站(domain)(加或不加 后缀 )来命名spider。 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite
    allowed_domains = ["apps.webofknowledge.com"]
    start_urls = [
        "http://apps.webofknowledge.com/summary.do?product=UA&parentProduct=UA&search_mode=AdvancedSearch&parentQid=&qid=65&SID=7C9pXPhFcQhlYOeJY4E&&update_back2search_link_param=yes&page=1"
    ]

    def parse(self, response):      #页面分析函数，response是响应页面
        titles = response.xpath(
            'string(//a[@class="smallV110 snowplow-full-record"]//value//text())'       # 由于value标签下文本有三个子部分，返回的是一个列表，因此使用string()将三串字符串连起来
        ).extract()     # 常用有extract()和extract_first()，前者提取所有
        for title in titles:
            fileName = 'paperTitles.txt'  # 爬取的内容存入文件，文件名为：作者-语录.txt
            f = open(fileName, "a+")  # 追加写入文件
            f.write('-' + title)  # 写入名言内容
            f.write('\n')  # 换行
            f.close()  # 关闭文件操作

        next_page = response.xpath(
            '//*[@id="summary_navigation"]/nav/table/tbody/tr/td[3]/a//@href'
        ).extract_first()   # 获取下一页链接

        if next_page is not None:   # 若下一页链接存在
            next_page = response.urljoin(next_page) 
            yield Request(next_page, callback=self.parse)     #scrapy.Request(), callback为对下一页面执行的函数
