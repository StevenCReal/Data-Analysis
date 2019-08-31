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
    """
    抓取页面所有链接
    """
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    for link in bsObj.find("div", {
            'class': 'news_bom-left'
    }).findAll('a', target='_blank'):
        picName = link.attrs['title']   # 同一model的图片放在一个文件夹中，picName为文件夹名字
        savingPath = "C:\\Users\\schen\\Pictures\\Girls\\" + picName + '\\' # 图片保存路径，最后要加上\，否则图片会保存在文件夹外
        if os.path.exists(savingPath):  # 判断该文件夹是否已经存在
            continue
        picUrl = urljoin(pageUrl, link.attrs['href'])   # 转化为绝对路径
        print(picName)
        print(picUrl)
        getPic(picUrl, savingPath)

    # 进入下一页
    next_page = bsObj.find('div', {
        'class': 'news_bom'
    }).find('div', {
        'class': 'page'
    }).find('a', text=u"下一页").attrs['href']
    next_page = urljoin(pageUrl, next_page)
    if next_page is not None:
        getPicLinks(next_page)


def getPic(pageUrl, savingPath):
    """
    抓取所有图片
    """
    # global urlList, nameList
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')

    img = bsObj.find("div", {
        'class': 'picsbox picsboxcenter'
    }).find("img", {"src": re.compile("https://img\.lovebuy99\.com.*jpg$")})
    imgName = bsObj.find("h1").get_text()   # 获取图片名字
    imgUrl = img.attrs['src']
    # print(imgName)
    # print(imgUrl)
    # urlList.append(imgUrl)
    # nameList.append(imgName)
    if not os.path.exists(savingPath):  # 为每一model创建文件夹
        os.mkdir(savingPath)
    urlretrieve(imgUrl, filename=savingPath + imgName + ".jpg") # 下载图片，注意filename格式，前面必须要加保存路径，才能将图片保存在指定文件夹中，否则将保存在当前文件夹

    # 抓取下一页的图片
    next_page = bsObj.find('a', text=u"下一页")
    next_pageUrl = urljoin(pageUrl, next_page.attrs['href'])
    # print(next_pageUrl)
    if next_page.attrs['href'] != "#":
        time.sleep(1)   # 暂停1秒，避免网站访问过快被反爬机制认为是蜘蛛
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

getPicLinks("https://www.7160.com/rentiyishu/list_1_1.html")
# getPic("https://www.7160.com/rentiyishu/61748/index.html")
# downloadPics(urlList, nameList)
