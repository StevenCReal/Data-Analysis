# 3.1　遍历单个域名
from urllib.request import unquote  # 进行URL解码，URL利用的是ASCII码，对于不在ASCII码中的，如中文，使用%十六进制进行表示
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(
    datetime.datetime.now())  # 用系统当前时间生成一个随机数生成器，保证每次程序运行时，词条的选择都是一个全新的随机路径


def getLinks(articleUrl):
    try:
        html = urlopen('https://baike.baidu.com' + articleUrl)
    except HTTPError as e:
        print(e)
        # 返回空值，中断程序，或者执行另一个方案
    else:
        if html is None:
            print("URL is not found")
        else:
            bsObj = BeautifulSoup(html, features='html.parser')
            return bsObj.findAll('a', {
                'target': '_blank',
                'href': re.compile('/item/.*/[0-9]*$')
            })


links = getLinks('/item/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(unquote(newArticle))
    links = getLinks(newArticle)
