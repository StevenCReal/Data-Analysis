# 学习正则表达式
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re

html = urlopen(
    "https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html#tab=album&stat=y_new.singerlist.singerpic"
)
bsobj = BeautifulSoup(html, features="html.parser")
images = bsobj.findAll("img", {
    "src":
    re.compile("//y.gtimg.cn/music/photo_new/.*\.jpg\?max_age=2592000")     # 使用正则表达式精准查找
})
for image in images:
    print(image["src"])

attrs = bsobj.body.div.img.attrs    # 利用Tag.attrs获取标签的全部属性，返回的是一个Python字典对象
print(attrs)

