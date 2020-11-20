# coding=utf-8
import urllib.request
import re
import os
import shutil
import msvcrt
# import ssl


from lxml import etree


# ssl._create_default_https_context = ssl._create_unverified_context


def add_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }


def get_all_html(url):
    # global new_url
    global sec_url
    myrequest = urllib.request.Request(url, headers=add_header())
    html = urllib.request.urlopen(myrequest).read()
    xml = etree.HTML(html)
    regex = '//*/@href'
    all_url = xml.xpath(regex)  # 拿到所url有地址
    # print(all_url)
    new_url = []
    for x in all_url:
        if re.findall(r'^/\w+', str(x)):
            new_url.append(x)
    list(set(new_url))
    new_url = [url + x for x in new_url]
    for x in new_url:
        print(x)
    # print(new_url)
    sec_url = []
    for y in new_url:
        try:
            myrequest = urllib.request.Request(y, headers=add_header())
            html = urllib.request.urlopen(myrequest).read()
            xml = etree.HTML(html)
            regex = '//*/@href'
            url_html = xml.xpath(regex)
            for x in url_html:
                print(x)
        except:
            pass
        else:
            sec_url += url_html  #
    for i in sec_url:
        if len(i) == 0:
            sec_url.remove(i)  # 去空值
    # print(sec_url)
    sec_url = list(set(sec_url))
    sec_url = [url + x for x in sec_url]
    # print(sec_url)
    # print(len(sec_url))
    print('页面总数：%s' % len(sec_url))
    print('准备拼接并解析所有页面。。。')


def save_html_detail():
    global sec_url
    global new_url
    usefull_urls = []
    for x in sec_url:
        try:
            myrequest = urllib.request.Request(x, headers=add_header())
            response = urllib.request.urlopen(myrequest)
            html = response.read().decode('utf8', 'ignore')
            usefull_urls.append(x)
            with open(x.replace('/', '+').replace(':', '=') + '.txt', 'w', encoding='utf-8') as file:
                file.write(html)
                print("%s解析完成。" % x.replace('+', '/').replace('=', ':'))
                # print("%s解析完成。" % x)
        except:
            pass


def title_pls_getout():
    # global usefull_urls
    for x in dirs:
        try:
            with open(x, 'r', encoding='utf-8') as file:
                html = file.read()
                xml = etree.HTML(html)

                regex_title = '//head/title/text()'
                regex_keyword = "//meta[@name='keywords']/@content"
                regex_description = "//meta[@name='description']/@content"
                title = xml.xpath(regex_title)[0].replace('\n', '')
                keyword = xml.xpath(regex_keyword)[0].replace(' ', '')
                description = xml.xpath(regex_description)[0].replace('\n', '')

                print(x[:-4].replace('+', '/').replace('=', ':'))
                print("Title:%s" % title)
                print("Keywords:%s" % keyword)
                print("Description:%s" % description)
                print('\n')
        except:
            pass


def search_kw():
    os.chdir('..')
    with open('keywords.txt', 'r', encoding='utf-8') as file:
        set_kw = file.readlines()  # all user set keywords
    os.chdir('log')
    path = os.getcwd()  # 获取当前路径
    dirs = os.listdir(path)
    for x in dirs:
        with open(x, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()  # all html words
            y = x
        try:
            for kw in set_kw:
                for lines in all_lines:
                    if kw in lines:
                        print('找到关键字:%s，所在html行：%s' % (kw, lines.replace('\n', ' ')))
                        print('所在URL地址：%s' % y[:-4].replace('+', '/').replace('=', ':'))
        except:
            print('关键字不存在。')


if __name__ == '__main__':
    '''
        http://huasu56.com.cn https://www.tist.com.cn http://www.tech-sonic.net
    '''
    '''
        1、读取'keyword.txt'中的关键字（关键字之间以中文格式的逗号隔开）
        2、获取首页的所有链接
            url:www.xxx.com
            title:xxxxxxxxx
            keyword:xxxxxxx
            description:xxx
        3、将所有链接中的汉字提取
        4、将keyword.txt与汉字进行匹配
        5、print带有关键字的url,titile...
        
        所有链接以列表的形式保存
    '''
    print("注意！需要在exe执行文件的同级目录下设置keywords.txt(一行设置一个关键字或词)。")
    url = input("请输入url(非com/cn域名请加http，url最后不要加'/'):")
    print('准备获取所有链接。')
    get_all_html(url=url)  # input url最后不要加’/‘
    if not os.path.exists('log'):  # 判断创建log文件夹
        os.mkdir('log')
    os.chdir('log')
    save_html_detail()

    path = os.getcwd()  # 获取当前路径
    dirs = os.listdir(path)

    title_pls_getout()
    print('Title等标签显示完成，按任意键开始进行关键字搜索。')
    msvcrt.getch()

    # os.chdir('..')            # 路径返回
    search_kw()

    while True:
        finish = input("检索完成，按q键退出。")
        if 'q' in finish:
            os.chdir('..')
            shutil.rmtree('log')
            break
        else:
            continue
