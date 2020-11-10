import urllib.request
import re

from lxml import etree

url = 'https://qizhiwanju.cn.made-in-china.com'
url_cut = re.split('https://', url)[1]
# def random_ip():
#     a=random.randint(1,255)
#     b=random.randint(1,255)
#     c=random.randint(1,255)
#     d=random.randint(1,255)
#     return(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d))
def add_header():
    return {
            # 'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            # 'Cookie': 'Hm_lvt_cd8bc3d2d8aeb37ddec2181e06fe9ea3 = 1604631822;Hm_lpvt_cd8bc3d2d8aeb37ddec2181e06fe9ea3 = 1604639445',
            # 'Host': 'img01.b2bkk.com',
            # 'Proxy-Connection': 'keep-alive',
            # 'Referer': 'http://zhi0123.b2bkk.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
myrequest = urllib.request.Request(url, headers=add_header())
html = urllib.request.urlopen(myrequest).read()
# print(html)
xml = etree.HTML(html)
regex = '//*/@href'
all_url = xml.xpath(regex)
# print(all_url)
str_url = str(url_cut) + '.txt'
with open(str_url, 'w') as file:
    for x in range(len(all_url)):
        file.write(all_url[x])
        file.write('\n')


