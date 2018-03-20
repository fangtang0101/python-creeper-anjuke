# -*- coding: utf-8 -*-
import requests
import ssl
from lxml import etree
# import urllib2
import urllib.request
from bs4 import BeautifulSoup
import path

# http://lanbing510.info/2016/03/15/Lianjia-Spider.html
# https://github.com/lanbing510/LianJiaSpider

ssl._create_default_https_context = ssl._create_unverified_context
session = requests.Session()
# url_page = 'https://suzhou.anjuke.com/sale/wuzhong/?from=SearchBar'
# url_page = 'https://suzhou.anjuke.com/sale/wuzhong/p1/#filtersort'
list_area = ['gongyeyuanqu','gaoxinqusuzhou','wuzhong','xiangcheng','wujiang','gushuqu','huqius','changshua','zhangjiagang','taicang']



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

def dealData(area,page):
    url_page = 'https://suzhou.anjuke.com/sale/'+area+'/p'+str(page)+'/#filtersort'
    print('url_page...',url_page)
    req = urllib.request.Request(url_page,headers=hds[0])
    source_code =  urllib.request.urlopen(req,timeout=10).read()
    soup = BeautifulSoup(source_code)
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
        # print('info_dict...',info_dict)

    # for item in list_info:
    #             for key in item:
    #                 print('key...',key)
    #                 print('item...',item[key])

    print('写入数据....'+area+str(page))
    with open("test.txt","a+") as f:
        f.write('写入数据....'+area+str(page))

        for item in list_info:
            for key in item:
                f.write(item[key])
                f.write('\n')


if __name__=="__main__":
    # path.clear_file('test.txt')
    for area in list_area:
        for page in range(1, 11):
            dealData(area,page)




            
            














# readerme ==================
# 1. 302  header  = req.headers['Location']
# 2. open("test.txt","a+")  a+ 代表续写，不会覆盖原来的内容  w+ 会覆盖原来的内容  http://blog.csdn.net/zhangweiguo_717/article/details/52960636
