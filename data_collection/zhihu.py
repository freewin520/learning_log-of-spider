import requests
from pyquery import PyQuery as pq

url = 'http://www.zhihu.com/collection/hot'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
html1 = requests.get(url, headers=headers).text
doc = pq(html1)

items = doc('.CollectionHotListPage-body .CollectionListCard.CollectionHotListPage-collectionCard ').items()
for item in items:
    doc = pq(item)
    question = doc('.CollectionListCard-contentTitle').text()
    text = doc('.CollectionListCard-contentExcerpt').text()
    text = text.split('：',1)
    author = text[0]
    answer = text[1]
    file = open('explore.text', 'a', encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n' + '=' *50 +'\n')
    file.close()

