# 练习导入reque模块和BeautifulSoup类
# 学习urlopen()函数，创建BeautifulSoup对象
# 使用BeautifulSoupd的findAll()函数
# 学会利用tag，attributes参数过滤HTML页面，知道还有recursive, text, limit, keyword参数

from urllib.request import urlopen  # urlib库和BeautifulSoup类最常用
from bs4 import BeautifulSoup

html = urlopen('https://movie.douban.com/subject/26581837/comments?status=P'
               )  # 抓取《上海堡垒》20条评论
bsobj = BeautifulSoup(html, features='html.parser')  # 创建BeautifulSoup对象
commentList = bsobj.findAll('span', {'class': 'short'})  # findAll()和find()最常用
print(len(commentList))
for comment in commentList:
    print(comment.get_text()
          )  # .get_text()把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串

headers = bsobj.findAll({'h1', 'h2', 'h3'})  # 可传入标签或标签组
for header in headers:
    print(header.get_text())
