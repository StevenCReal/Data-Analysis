from urllib.request import unquote  # 进行URL解码，URL利用的是ASCII码，对于不在ASCII码中的，如中文，使用%十六进制进行表示
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(
    'https://baike.baidu.com/item/%E6%96%B0%E6%B3%BD%E8%A5%BF%E5%B7%9E'
)  # 如‘凯’字，表示为%E5%87%AF
bsObj = BeautifulSoup(html, features="html.parser")
linkList = bsObj.findAll('a', {
    'target': '_blank',
    'href': re.compile('/item/.*')
})

for i in range(2):
    linkList.pop(-1)
for j in range(5):
    linkList.pop(0)

for link in linkList:
    if 'href' in link.attrs:
        print(unquote(link.attrs['href']))  # unquote()可对URL进行解码，输出中文

# 过滤条件应考虑：
# 1.在哪个范围查找
# 2.是否有共同的标签；标签是否有共同属性；属性是否有共同的值；
# 3.使用交集、并集、非集进一步筛选
