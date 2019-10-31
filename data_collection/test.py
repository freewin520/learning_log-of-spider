# # *_*coding:utf-8 *_*
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(),"html.parser")
# print(bsObj)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html = urlopen("http://books.toscrape.com")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# # print(bsObj.html) ，
# books = bsObj.findAll("div", {"class":"image_container"})
# for book in books:
#     print(book)



from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href=
            re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    #编辑历史URL链接的格式是：
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+historyUrl)
    html=urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    #找出class属性是"mw-anonuserlink"的链接
    #他们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a",{"class":"mw-annouserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("----------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)