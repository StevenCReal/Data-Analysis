# -*- coding: utf-8 -*-
from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
import time
import os

# urlList = []
# nameList = []


def getPicLinks(pageUrl):
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    for link in bsObj.find("div", {
            'class': 'news_bom-left'
    }).findAll('a', target='_blank'):
        picName = link.attrs['title']
        savingPath = "C:\\Users\\schen\\Pictures\\Girls\\" + picName + '\\'
        if os.path.exists(savingPath):
            continue
        picUrl = urljoin(pageUrl, link.attrs['href'])
        print(picName)
        print(picUrl)
        getPic(picUrl, savingPath)

    next_page = bsObj.find('div', {
        'class': 'news_bom'
    }).find('div', {
        'class': 'page'
    }).find('a', text=u"下一页").attrs['href']
    next_page = urljoin(pageUrl, next_page)
    if next_page is not None:
        getPicLinks(next_page)


def getPic(pageUrl, savingPath):
    # global urlList, nameList
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')

    img = bsObj.find("div", {
        'class': 'picsbox picsboxcenter'
    }).find("img", {"src": re.compile("https://img\.lovebuy99\.com.*jpg$")})
    imgName = bsObj.find("h1").get_text()
    imgUrl = img.attrs['src']
    # print(imgName)
    # print(imgUrl)
    # urlList.append(imgUrl)
    # nameList.append(imgName)
    if not os.path.exists(savingPath):
        os.mkdir(savingPath)
    urlretrieve(imgUrl, filename=savingPath + imgName + ".jpg")

    next_page = bsObj.find('a', text=u"下一页")
    next_pageUrl = urljoin(pageUrl, next_page.attrs['href'])
    # print(next_pageUrl)
    if next_page.attrs['href'] != "#":
        time.sleep(1)
        getPic(next_pageUrl, savingPath)


# def downloadPics(urlList, nameList):
#     path = "C:\\Users\\schen\\Pictures\\Girls\\" + nameList[0]
#     print(path)
#     if not os.path.exists(path):
#         os.mkdir(path)
#     for i in range(len(urlList)):
#         urlretrieve(urlList[i], filename=path + nameList[i] + ".jpg")
#         print(nameList[i])
#         print("--------downloading--------")
#     print("-------done--------")

getPicLinks("https://www.7160.com/rentiyishu")
# getPic("https://www.7160.com/rentiyishu/61748/index.html")
# downloadPics(urlList, nameList)
