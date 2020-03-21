import requests,csv
from lxml import etree
import random
import re
import time


#ip池
def ips():
    proxys = [
        {'http': 'http://1.198.111.82:9999'},
        {'http': 'http://117.69.12.106:9999'},
        {'http': 'http://110.243.6.110:9999'},
        {'http': 'http://118.112.195.59:9999'},
        {'http': 'http://223.199.25.133:9999'}
    ]
    proxy = random.choice(proxys)  # random.choice(),从列表中随机抽取一个对象
    return proxy

# 构造url
def get_urls():
    urls=[]
    for n in range(1,71):
        url='http://hrb.ganji.com/zufang/pn{}/'.format(n)
        urls.append(url)
    return urls

#解析详细url
def get_url2(urls):
    url3=[]
    for url5 in urls:
        print(url5)
        response=requests.get(url5)
        html = etree.HTML(response.content.decode('utf-8'))
        items = html.xpath(".//div[@class='f-main-list']/div/div")
        for item in items:
            url1 = item.xpath(".//dd[@class='dd-item title']/a/@href")
            for url4 in url1:
                result = re.sub('ding.*?&end=end', "", url4)
                result1 = re.sub('.*?//hrb', "https://hrb", result)
                url3.append(result1)
    return url3

#获取详细
def parsing():
    for url in url2:
        print(url)
        response=requests.get(url)
        html = etree.HTML(response.content.decode('utf-8'))
        name = html.xpath(".//div[@class='user-info f-clear small-company']/div/div/a/text()")
        phone = html.xpath(".//div[@class='c_phone f-clear']/div[@class='phone']/a/text()")
        gs = html.xpath(".//div[@class='info']/ul[@class='service']/li[1]/span[@class='text']/text()")
        print(name,phone,gs, sep='|')
        writer.writerow((name, phone, gs))


if __name__ == '__main__':
    fp = open('赶集网经纪人.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('名字', '电话', '公司'))
    # ip = ips()
    urls=get_urls()
    url2=get_url2(urls)
    parsing()
