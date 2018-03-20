# -*- coding: utf-8 -*-
import requests
import ssl
from lxml import etree
# import urllib2
import urllib.request
from bs4 import BeautifulSoup

# http://lanbing510.info/2016/03/15/Lianjia-Spider.html
# https://github.com/lanbing510/LianJiaSpider

ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()


            

#  headers =  {
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, sdch, br',
# 'Accept-Language': 'zh-CN,zh;q=0.8',
# 'Connection': 'keep-alive',
# 'Host': 'suzhou.anjuke.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#  }  


# url = 'https://suzhou.anjuke.com/sale/gushuqu/?from=SearchBar'
# # url = 'http://m.anjuke.com/qd/xiaoqu/'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Host': 'https://suzhou.anjuke.com/',
#     'Pragma': 'no-cache',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
# }


url_page = 'https://suzhou.anjuke.com/sale/wuzhong/?from=SearchBar'

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]


req = urllib.request.Request(url_page,headers=hds[0])
source_code =  urllib.request.urlopen(req,timeout=10).read()
soup = BeautifulSoup(source_code)

### tip1:python3 use urllib.request instance of urllib2

# list-item

# print('soup......',soup)

xiaoqu_list=soup.findAll('li',{'class':'list-item'})

list_info = []

for xq in xiaoqu_list:
    info_dict={}

     # 图片
    item_img = xq.find('img')['src']
    info_dict['item_img'] = item_img
   

    
    # 标题
    aa = xq.find('div',{'class':'house-details'})
    bb = aa.find('div',{'class':'house-title'})
    cc = bb.find('a').text
    url = bb.find('a')['href'] # tips
    info_dict['title'] = cc
    info_dict['url'] = url

    # 楼层 等信息

    ff = aa.find('div',{'class':'details-item'})
    gg = ff.findAll('span')
    info_dict['type'] = gg[0].text
    info_dict['size'] = gg[1].text
    info_dict['creat_year'] = gg[3].text

     # address comm-address

    jj = xq.find('span',{'class':'comm-address'})
    info_dict['address'] = jj.text

    # price
    pp = xq.find('div',{'class':'pro-price'})
    price = pp.find('strong').text
    price_mei = pp.find('span',{'class':'unit-price'}).text

    info_dict['price'] = price
    info_dict['price_mei'] = price_mei

    list_info.append(info_dict)

    print('info_dict...',info_dict)

# for item in list_info:
#             for key in item:
#                 print('key...',key)
#                 print('item...',item[key])


with open("test.txt","w") as f:
        for item in list_info:
            for key in item:
                f.write(item[key])
                f.write('\n')

            
            














# readerme ==================
# 1. 302  header  = req.headers['Location']
