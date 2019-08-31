from urllib.request import urlopen, urlretrieve, urljoin
from bs4 import BeautifulSoup

def getESTPaper(doi):
    try:
        html=urlopen("https://pubs.acs.org/doi/"+doi)
        bsObj = BeautifulSoup(html, "html.parser")
    except:
        print("cannot get paper!")
    else:
        pdfLink = bsObj.find('a',{"title":"PDF"}).attrs['href']
        print(pdfLink)

def getDOI(pageUrl):
    try:
        html=urlopen(pageUrl)
        bsObj = BeautifulSoup(html, "html.parser")
    except :
        print("cannot find DOI!")
    else:
        doi= bsObj.find('span',text='DOI:').next_sibling().get_text()
        print(doi)
        return doi

# try:
#     html = urlopen("http://apps.webofknowledge.com/summary.do?locale=en_US&errorKey=&viewType=summary&product=UA&search_mode=Analyze&page=1&qid=4&SID=5E4nnIMnWt17COedDJW&parentProduct=UA")
#     bsObj = BeautifulSoup(html,features='html.parser')
# except:
#     print('Wrong!')
# else:
#     for searchResult in bsObj.findAll('div',{'class':'search-results'}):
#         for item in searchResult.findAll('div',{'class':'search-results-item'}):
#             pageUrl = item.find('a',{'class':'smallV110 snowplow-full-record'}).attrs['href']
#             if pageUrl:
#                 pageUrl = urljoin('http://apps.webofknowledge.com/',pageUrl)
#                 doi = getDOI(pageUrl)
#                 getPaper(doi)
#             else:
#                 print("not Found!")

# doi = getDOI('http://apps.webofknowledge.com/full_record.do?product=UA&search_mode=Analyze&qid=4&SID=5E4nnIMnWt17COedDJW&page=1&doc=1')
# print(doi)

getESTPaper('10.1021/acs.est.7b05559')