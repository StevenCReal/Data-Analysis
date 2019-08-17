from urllib.request import urlopen
from bs4 import BeautifulSoup

wikiHowItems = set()


def getLink(pageUrl):
    global wikiHowItems
    html = urlopen("http://www.wikihow.com" + pageUrl)
    bsObj = BeautifulSoup(html, features='html.parser')
    if pageUrl not in wikiHowItems:
        wikiHowItems.add(pageUrl)
        try:
            title = bsObj.h1.find('a').get_text()
            introduction = bsObj.findAll('p')[2].get_text()
        except AttributeError:
            print("Some Attributes not found, ignore it!")
        else:
            print('Theme: ' + title)
            print('Introduction: ' + introduction)
            print('--' * 8)
            print(wikiHowItems)
    relatedItems = bsObj.findAll('a', {'class': 'related-title'})
    for item in relatedItems:
        getLink(item.attrs['href'])


getLink('/Eat-Cheese')
