import urllib.request
import re
import os
import ssl


from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context


def add_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }


def save_all_html(url):
    global new_url
    myrequest = urllib.request.Request(url, headers=add_header())
    html = urllib.request.urlopen(myrequest).read()
    xml = etree.HTML(html)
    regex = '//*/@href'
    all_url = xml.xpath(regex)                      # 拿到所url有地址
    new_url = url.replace('/', '_')
    with open('{0}.txt'.format(new_url), 'w') as file:
        for x in range(len(all_url)):
            file.write(all_url[x])
            file.write('\n')
        print('%s保存成功。' % '{0}.txt'.format(new_url))


def for_merge_every_url():
    global new_url
    # f = open('{0}.txt'.format(new_url))
    # fw = open('fullurl' + '{0}.txt'.format(new_url), "w")
    # for line in f.readlines():
    #     if line.
    with open('{0}.txt'.format(new_url), "r+") as f:
        line = f.readlines()        # 将原来文件的每一行内容进行保存，记录到列表里面
        f.seek(0)
        f.truncate()                # 先将原来文件进行清空
        for line_list in line:      # 对于原来文件的内容每一行进行添加的操作
            line_new = url + line_list
            f.write(line_new)
# 首页分支页面完工


def get_url_detail():
    with open('{0}.txt'.format(new_url), 'r') as file:
        lines = file.readlines()
        usefull_lines = []
        for line in lines:
            usefull_lines.append(line)
            # print(usefull_lines)  有效的地址全部添加到列表
    new_usefull_url = []
    # 去n
    for x in usefull_lines:
        newx = x[:-1]
        new_usefull_url.append(newx)
        # print(new_usefull_url)    拿到了所有的有效html地址，准备开始干活了！
    for y in new_usefull_url:
        try:
            myrequest = urllib.request.Request(y, headers=add_header())
            response = urllib.request.urlopen(myrequest)
            html = response.read().decode('utf8', 'ignore')
            every_html = y.replace('/', '-')
        except:
            pass
        else:

            with open('{0}.txt'.format(every_html), 'w') as file:
                file.write(html)
                print('%s的页面都记好了。' % every_html)        # Every html file saved!


def to_ch_words():
    # 找到log位置
    # os.chdir('log')
    path = os.getcwd()
    dirs = os.listdir(path)
    pchinese = re.compile('([\u4e00-\u9fa5]+)+?')  # 判断是否为中文的正则表达式
    for x in dirs:
        f = open(x)  # 打开要提取的文件
        fw = open('ch_' + x, "w")  # 打开要写入的文件
        try:
            for line in f.readlines():  # 循环读取要读取文件的每一行
                m = pchinese.findall(str(line))  # 使用正则表达获取中文
                if m:
                    str1 = '|'.join(m)  # 同行的中文用竖杠区分
                    str2 = str(str1)
                    fw.write(str2)  # 写入文件
                    fw.write("\n")  # 不同行的要换行
        except:
            pass
            f.close()
            fw.close()
        print('%s汉字都检索好了。' % x)


def get_out_ch():
    global kw
    path = os.getcwd()
    dirs = os.listdir(path)
    for x in dirs:
        f = open(x, "r")
        address = x.replace('-', '/')[:-4]
        for line in f.readlines():
            if kw in line:
                print(line)
                print(address)
                break
    else:
        print('搜索结果不存在。')



if __name__ == '__main__':
    global new_url
    global line

    url = input('请输入url地址(地址格式：以.com/.cn结尾)：')
    if not os.path.exists('log'):
        os.mkdir('log')
    os.chdir('log')
    add_header()
    save_all_html(url=url)
    # for循环准备将所有url拼接。
    for_merge_every_url()       # 完成每一个首页上的链接
    print('首页链接获取完毕。')
    get_url_detail()
    to_ch_words()
    # os.chdir('log')
    while True:
        kw = input('请输入需要检索的关键字：')
        get_out_ch()










