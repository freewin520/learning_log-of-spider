# *_*coding:utf-8 *_*
import re
import json
import time

import requests

def get_one_page(url):
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; \
            Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None
def write_to_file(content):
    with open('result.text', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
def parse_on_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>'+
        '.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>'+
        '.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>'+
        '.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
        ,
        re.S
    )
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }
    #     write_to_file(content)


def main(offset):
    url = 'http://maoyan.com/board/4?offset='+ str(offset)
    html = get_one_page(url)
    for item in parse_on_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)