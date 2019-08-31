from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


def getAllExternalLinks(pageUrl):
    """获取当前页面的全部外链"""
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    excludeUrl = pageUrl.replace('http://', '').split('/')[0]
    extLinks = []
    for link in bsObj.findAll('a',
                              href=re.compile("^(http|www)((?!" + excludeUrl +
                                              ").)*$")):
        if link.attrs['href'] is not None:
            extLinks.append(link.attrs['href'])
    if len(extLinks) == 0:
        nextIntLink = getNextIntLink(pageUrl)
        return getAllExternalLinks(nextIntLink)
    else:
        return extLinks


def getAllInternalLinks(pageUrl):
    """获取当前链接的全部内链"""
    html = urlopen(pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    includeUrl = pageUrl.replace('http://', '').split('/')[0]
    intLinks = []
    for link in bsObj.findAll('a',
                              href=re.compile("^(/|.*" + includeUrl + ")")):
        intLinks.append(link.attrs['href'])
    return intLinks


def getRandomExternalLink(pageUrl):
    """进入当前页面的任一外链"""
    extLinks = getAllExternalLinks(pageUrl)
    nextExtLink = extLinks[random.randint(0, len(extLinks) - 1)]  # 获取任一外链
    return nextExtLink  # 未解决：如果所有页面都被访问过或是被屏蔽该怎么解决？


def getNextIntLink(pageUrl):
    """获取当前页面的一个内链"""
    intLinks = getAllInternalLinks(pageUrl)
    nextIntLink = intLinks[random.randint(0, len(intLinks) - 1)]  # 获取任一内链
    return nextIntLink


def followExternalOnly(StartingPage):
    """从当前链接进入下一外链页面"""
    nextExtLink = getRandomExternalLink(StartingPage)
    print(nextExtLink)
    pages.add(nextExtLink)
    followExternalOnly(nextExtLink)


followExternalOnly("http://oreilly.com")
