# urllib库学习
from urllib.request import urlopen
from urllib.request import build_opener
from urllib.request import Request
from urllib.parse import urlencode
from urllib.request import ProxyHandler, HTTPHandler, install_opener
from urllib.request import HTTPSHandler

# """浏览器的模拟——Headers属性"""
# headers = (
#     "User-Agent",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
# )  # headers定义格式： ("User-Agent", "具体信息")
# url = "http://www.bilibili.com"

# # 模拟浏览器方法一：使用build_opener()修改报头
# opener = build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()
# # 方法二：使用add_header()添加报头
# req = Request(url)
# req.add_header(
#     'User-Agent',
#     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
# )
# data2 = urlopen(req).read(
# )  # the URL url, which can be either a string or a Request object.


# """超时设置"""
# for i in range(1,100):
#     try:
#         req2 = Request(url)
#         req2.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36")
#         data3 = urlopen(req2, timeout=0.1).read()
#         print(len(data3))
#     except Exception as e:
#         print("Error: "+str(e))

# """
# 常用HTTP协议请求方法
# 可以使用HTTP协议请求进行客户端与服务器端之间的消息传递
# """
# # GET请求：直接在URL中写上要传递的信息向服务端发送GET请求，例如在URL后面添加GET请求的字段名河字段内容等信息
# # 略

# # POST请求
# loginUrl = "https://www.iqianyue.com/mypost"
# formData = {'name':'schen1998@outlook.com','pass':'176115-Cyw'}    # 构建表单数据——字典形式
# formData = urlencode(formData).encode('utf-8')  # 将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
# req = Request(loginUrl,formData)    # 创建Request对象
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36')

# data = urlopen(req).read()
# print(len(data))

# """设置代理服务器"""
# def use_proxy(proxy_addr, url):
#     proxy = ProxyHandler({'http':proxy_addr})   # 设置代理服务器信息，格式： ProxyHandler({'http':代理服务器地址})
#     opener = build_opener(proxy,HTTPHandler)    # 创建自定义的opener对象
#     install_opener(opener)  # 创建全局默认的opener对象，这样后面才能默认使用我们自定义的opener,并能直接使用urlopen
#     try:
#         req = Request(url)
#         req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36')
#         data = urlopen(req,timeout=5).read().decode('utf-8')
#     except Exception as e:
#         print(str(e))
#         return 0
#     else:
#         return data

# proxy_addr = '139.159.47.22:39593'
# url = 'https://www.csdn.net'
# data = use_proxy(proxy_addr,url)
# print(len(data))

"""开启DebugLog，边运行边打印调试日记"""
httphd = HTTPHandler(debuglevel=1)
httpshd = HTTPSHandler(debuglevel=1)
opener = build_opener(httphd,httpshd)
install_opener(opener)
data = urlopen('http://www.csdn.net').read().decode('utf-8')
print(len(data))

"""异常处理"""
from urllib.error import URLError, HTTPError
# HTTPError是URLError的一个子类
# 常用try...except语句来捕获异常信息
# 发生URLError的原因：
# 1.连接不上服务器
# 2.远程URL不存在
# 3.无网络
# 4.触发了HTTPError：HTTPError会有相应的异常状态码和异常原因，可用HTTPError.code和HTTPError.reason分别得到