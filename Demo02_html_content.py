import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://cn.made-in-china.com/etyzwj-chanpin-1.html'
url_cut = re.split('https://', url)[1]


# def ungzip(data):
#     try:
#         data = gzip.decompress(data)
# except:
#         pass
#     return data


def add_header():
    return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }


myrequest = urllib.request.Request(url, headers=add_header())
response = urllib.request.urlopen(myrequest)
html = response.read().decode('gbk', 'ignore')  #decode gbk编码格式
# print(html)

str_url = str(url_cut) + '.txt'
new_url = url.replace('/', '_')
with open('/Users/suikasann/PycharmProjects/PythonSpider/Spider/{0}.txt'.format(new_url), 'w') as file:
    file.write(html)
