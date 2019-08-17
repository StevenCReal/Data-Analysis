# -*- coding: utf-8 -*-
# 3.2　采集整个网站

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen('https://www.wikihow.com' + pageUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    for link in bsObj.findAll('a', {'class': 'related-title'}):
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)


getLinks('/Protest-Safely')
