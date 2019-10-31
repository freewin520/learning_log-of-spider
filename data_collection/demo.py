# *_*coding:utf-8 *_*
import urllib.request
import socket
import urllib.error
from urllib import request, parse


# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

#Request便于对请求进行管理
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 多参数构建请求
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent':'Mozilla/4.0(compatible; MISE 5.5; Windows NT)',
#     'Host':'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

#HTTPBasicAuthHandler 管理认证(用户名，密码)
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://portal.ecjtu.edu.cn/dcp/forward.action?path=/portal/portal&p=home'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

#代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:80',
#     'https': 'https://127.0.0.1:80'
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://www.baidu.com/')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# 获取某个网页的Cookies
# import http.cookiejar, urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# cookier 转text
# import http.cookiejar, urllib.request
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.zhihu.com')
# print(response.read().decode('utf-8'))

# from urllib import request,error
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

# from urllib.parse import urlparse
#
# result =urlparse('http://www.baidu.com',allow_fragments=False)
# print(result.scheme,result[0], result.netloc,result[1],sep='\n')

# from urllib.parse import urlunparse
# data=['http','www.baidu.com','index.hrml','user','a=6','comment']
# print(urlunparse(data))

# from urllib.parse import urlsplit
# result=urlsplit("htto://www.baidu.com/index.html;user?id=5#comment")
# print(result)

# from urllib.parse import urlunsplit
#
# data = ['http','www.baidu.com','index.html','a=6','comment']
# print(urlunsplit(data))

# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wb=abc','https://cuiqingcai.com/index.php'))
# print(urljoin('http://www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com#comment','?category=2'))

# from urllib.parse import urlencode
#
# params = {
#     'name':'germy',
#     'age':22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# from urllib.parse import parse_qs
# query = 'name=germey&age=22'
# print(parse_qs(query))


# from urllib.parse import parse_qsl
# query = 'name=germey&age=22'
# print(parse_qsl(query))

# from urllib.parse import quote
# keyword = "壁纸"
# url = "https://www.baidu.com/s?wd=" + quote(keyword)
# print(url)

# from urllib.parse import unquote
# url='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*',"http://www.jianshu.com/search?q=python&page=1&type=collection"))


# import requests
#
# r=requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# import requests
#
# data = {
#     'name':'germey',
#     'age':22
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# import requests
# import re
#
# headers ={
#     'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)\
#         Chrome/52.0.2743.116 Safari/537.36'
# }
# r =requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>',re.S")
# titles = re.findall(pattern,r.text)
# print(titles)

# import requests
#
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)
# print(r.text)
# print(r.content)

# import requests
# headers ={
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML,like Gecko)\
#                  Chrome/52.0.2743.116 Safari/537.36"
# }
# r=requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)

# import requests
# data = {'name':'germy', 'age':'22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

# import requests
#
# r=requests.get('http://www.jianshu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')



# files ={'file':open('favicon.ico','rb')}
# r = requests.post('http://httpbin.org/post',files=files)
# print(r.text)
# r = requests.get("https://baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+ value)

# headers = {
#     'Cookie': '_xsrf = i4WCit4A9f4unvdGDPpMIzd7tO2JLpab;\
#     z_c0 = "2|1:0|10:1569280384|4:z_c0|92:Mi4xVFhMRUF3QUFBQUFBOEtJOXFOWEhEeVlBQUFCZ0FsVk5nSjkyWGdDWndoRXdWaHNZSElHS0YzdzJiejJVcW1mNFV3|a47cc0c4e69c3be63811972de7399af9626782605c5a52cf4385ed9d107e6b91";\
#     tst = r;\
#     d_c0 = "APCiPajVxw-PTvaipqVXQo2nVmdIYqFTvQk=|1563888710";\
#     Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49 = 1569414392, 1569808108, 1570530185, 1570530204;\
#     capsion_ticket = "2|1:0|10:1569280354|14:capsion_ticket|44:ZDQyYzA3YjlkOWE1NDNhYmEwZWRkN2UwZTA0M2JjOGU=|888533bd8ee038fed18234522cadc71d32b9e7cd00a5c1091d45b30f576937c8";\
#     _zap = c891b6bd - 9471 - 4\
#     abe - 8042 - 20\
#     ab9ff5a359;\
#     Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49 = 1570530204;\
#     tgw_l7_route = 80\
#     f350dcd7c650b07bd7b485fcab5bf7',
#     'Host':'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
# }
# r = requests.get('http://www.zhihu.com',headers=headers)
# print(r.text)

# cookies = '_xsrf = i4WCit4A9f4unvdGDPpMIzd7tO2JLpab;\
#     z_c0 = "2|1:0|10:1569280384|4:z_c0|92:Mi4xVFhMRUF3QUFBQUFBOEtJOXFOWEhEeVlBQUFCZ0FsVk5nSjkyWGdDWndoRXdWaHNZSElHS0YzdzJiejJVcW1mNFV3|a47cc0c4e69c3be63811972de7399af9626782605c5a52cf4385ed9d107e6b91";\
#     tst = r;\
#     d_c0 = "APCiPajVxw-PTvaipqVXQo2nVmdIYqFTvQk=|1563888710";\
#     Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49 = 1569414392, 1569808108, 1570530185, 1570530204;\
#     capsion_ticket = "2|1:0|10:1569280354|14:capsion_ticket|44:ZDQyYzA3YjlkOWE1NDNhYmEwZWRkN2UwZTA0M2JjOGU=|888533bd8ee038fed18234522cadc71d32b9e7cd00a5c1091d45b30f576937c8";\
#     _zap = c891b6bd - 9471 - 4\
#     abe - 8042 - 20\
#     ab9ff5a359;\
#     Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49 = 1570530204;\
#     tgw_l7_route = 80\
#     f350dcd7c650b07bd7b485fcab5bf7'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host':'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
# }
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=',1)
# r = requests.get('http://www.zhihu.com', cookies=jar,headers=headers)
# print(r.text)


# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:80',
#     'https': 'https://127.0.0.1:80'
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://www.taobao.com/',timeout=1)
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

#4.1
# from lxml import etree
# text = '''
# <div>
# <ul>
# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactivate"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html = etree.parse('./demo.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# from lxml import etree
# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//*')
# print(result)

from lxml import etree

# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)

# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)

# html = etree.parse('./demo.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">foutth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/ancestor::*')
# print(result)
# result = html.xpath('//li[1]/ancestor::div')
# print(result)
# result = html.xpath('//li[1]/attribute::*')
# print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result)
# result = html.xpath('//li[1]/descendant::span')
# print(result)
# result = html.xpath('//li[1]/following::*[2]')
# print(result)
# result = html.xpath('//li[1]/following-sibling::*')
# print(result)

#4.2
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# #按html缩进
# # print(soup.prettify())
# # print(soup.title.string)
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)
# print(soup.p.attrs)
# print(soup.p.attrs['name'])

# import re
# html='''
# <div class="panel">
# <div class="panel-body">
# <a>Hello, this is a link</a>
# <a>Hello, this is a link, too</a>
# </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))

# html='''
# <div class="panel">
# <div class="panel-heading">
# <h4>Hello</h4>
# </div>
# <div class="panel-body">
# <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>
# </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))

html = """
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
"""
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))
# html = '''
# <div class="wrap">
# <div id = "container"
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 activate"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 activate"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('li:first-child')
# print(li)
# li = doc('li:last-child')
# print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li = doc('li:contains(second)')
# print(li)

# 5.3.1
# import pymongo
# from bson.objectid import ObjectId
# client = pymongo.MongoClient(host='localhost',port=27017)
# #client = pymongo.MongoClient('mongodb://locallhost:27017/')
# db = client.test
# #db = client['test']
# collection = db.students
# #collection = db['students']
# student = {
#     'id':'20170101',
#     'name':'Cat',
#     'age':20,
#     'gender':'male'
# }
# result = collection.insert_one(student)
# print(result.inserted_id)
# result = collection.find_one({'name':'Cat'})
# print(type(result))
# print(result)
# result = collection.find_one({'_id':ObjectId('5dad942b595c6da9a690beaf')})
# print(result)
# results = collection.find({'age':20})
# results = collection.find({'age':{'$gt':19}})#大于
# results = collection.find({'name':{'$regex':'^M.*'}})#匹配以M开头的字符
# print(results)
# for result in results:
#     print(result)

#5.3.2
from redis import StrictRedis,ConnectionPool


# redis = StrictRedis(host='localhost', port=6379, db=0)
# redis.set('name','Bob')
# print(redis.get('name'))
pool=ConnectionPool(host='localhost',port=6379,db=0)
redis = StrictRedis(connection_pool=pool)
#通过url构建连接池
url="redis://@localhost:6379/0"
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)