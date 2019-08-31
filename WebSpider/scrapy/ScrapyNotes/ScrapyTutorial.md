# Scrapy Tutorial
<!-- TOC -->
[1.1. Creating a project](#11-creating-a-project)

[1.2. Writing a *spider* to crawl a site and extract data](#12-writing-a-spider-to-crawl-a-site-and-extract-data)auto  
* [1.2.1. First Spider](#121-first-spider)  
* [1.2.2. How to run our spider ?](#122-how-to-run-our-spider-)  
* [1.2.3. A shortcut to the start_requests method](#123-a-shortcut-to-the-start_requests-method)  
* [1.2.4. extracting data](#124-extracting-data)  

[1.3. Changing spider to recursively follow links](#13-changing-spider-to-recursively-follow-links)  
* [1.3.1. extracting the link](#131-extracting-the-link)  
* [1.3.2. follow the link extracting above:](#132-follow-the-link-extracting-above)
<!-- /TOC -->
## 1.1. Creating a project
Before you start scraping, you will have to set up a new Scrapy project : 
```
[shell] scrapy startproject projectName
```
<center>

![directory][directory]
**directory**

</center>


## 1.2. Writing a *spider* to crawl a site and extract data
### 1.2.1. First Spider
```
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
```

- Spiders must subclass scrapy. Spider and define the initial requests to make. 
- *start_requests()* : must return **an iterable of Requests** (you can return a list of requests or write a generator function) which the Spider will begin to crawl from.

### 1.2.2. How to run our spider ?
```
[shell] scrapy crawl quotes
```

### 1.2.3. A shortcut to the start_requests method
```
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
```
The *parse()* method will be called to handle each of the requests for those URLs, even though we haven’t explicitly
told Scrapy to do so. This happens because parse() is Scrapy’s **default callback method**.

### 1.2.4. extracting data
- using the Scrapy shell:  
```
[shell] scrapy shell "http://quotes.toscrape.com/page/1/"
        # use double quotes on Windows
```
- The result of running *response.css( 'title' )* is a list-like object called **SelectorList**, which represents a list of Selector objects that wrap around XML/HTML elements and allow you to run further queries to fine-grain the selection or extract the data.
```
[shell] response.css('title')
>>> [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

[shell] response.css('title::text').getall()    
        # extract the text from the title above.
        # If we don’t specify ::text, we’d get the full title element, including its tags
>>> ['Quotes to Scrape']
```
- The result of calling *.getall( )* is a **list** (not SelectorList).
- Besides the *getall( )* method, you can also use *get()* and *re()* to extract the first result and extract using **regular expressions** respectively:
```
[shell]response.css('title::text').re(r'Quotes.*')
>>> ['Quotes to Scrape']
[shell] response.css('title::text').re(r'Q\w+')
>>> ['Quotes']
[shell] response.css('title::text').re(r'(\w+) to (\w+)')
>>> ['Quotes', 'Scrape']
```

> **What is yield ?**  
(Notes in Evernote.)


## 1.3. Changing spider to recursively follow links
### 1.3.1. extracting the link
We can see a link to the next page with the following markup:
```
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
```
- To extract the attribute *href*:
```
[shell] response.css('li.next a::attr(href)').get()
>>> '/page/2/'
[shell] response.css('li.next a').attrib['href]
>>> '/page/2/'
```
### 1.3.2. follow the link extracting above:
```
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
```

> **urljoin()** 
We can build a full absolute URL using the urljoin() method (since the links can be relative). There are 2 ways to use it:
> ```
> next_page = response.urljoin(next_page) # use the url of respnose as baseurl
> next_page2 = urljoin(base,url) # explicitly pass the baseurl
> ```

> **response.follow()**  
it allows you to use relative URLs directly, and you can also pass a selector to *response.follow()* :  
>```
> next_page = response.css('li.next a::attr(href)').get()
> if next_page is not None:
>     yield response.follow(next_page, callback=self.parse)
>
> for href in response.css('li.next a::attr(href)'):
>     yield response.follow(href, callback=self.parse)
>```

[directory]:https://github.com/StevenCReal/Data-Analysis/blob/master/WebSpider/scrapy/ScrapyNotes/%E6%89%B9%E6%B3%A8%202019-08-31%20001222.jpg?raw=true
