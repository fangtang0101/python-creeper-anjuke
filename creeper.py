# -*- coding: utf-8 -*-
import requests
import ssl
from lxml import etree

# http://lanbing510.info/2016/03/15/Lianjia-Spider.html
# https://github.com/lanbing510/LianJiaSpider

ssl._create_default_https_context = ssl._create_unverified_context

session = requests.Session()


for id in range(0, 251, 25):
    URL = 'https://movie.douban.com/top250/?start=' + str(id)
    req = session.get(URL)
    # 设置网页编码格式
    req.encoding = 'utf8'
    # 将request.content 转化为 Element
    root = etree.HTML(req.content)
    print('root...',root)
    # 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
    items = root.xpath('//ol/li/div[@class="item"]')
    print('items...',items)
    for item in items:
        # 注意可能只有中文名，没有英文名；可能没有quote简评
        rank, name, alias, rating_num, quote, url = "", "", "", "", "", ""
        try:
            url = item.xpath('./div[@class="pic"]/a/@href')[0]
            print('url...',url)
            rank = item.xpath('./div[@class="pic"]/em/text()')[0]
            title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
            name = title[0].encode('gb2312', 'ignore').decode('gb2312')
            alias = title[1].encode('gb2312', 'ignore').decode('gb2312') if len(title) == 2 else ""
            rating_num = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
            quote_tag = item.xpath('.//div[@class="bd"]//span[@class="inq"]')
            if len(quote_tag) is not 0:
                quote = quote_tag[0].text.encode('gb2312', 'ignore').decode('gb2312').replace('\xa0', '')
            # 输出 排名，评分，简介
            print('排名',rank,'评分', rating_num,'简介',quote)
            # 输出 中文名，英文名
            print('中文名',name.encode('gb2312', 'ignore').decode('gb2312'),'英文名',
                  alias.encode('gb2312', 'ignore').decode('gb2312').replace('/', ','))
        except:
            print('faild!')
            

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
# req = session.get(url,headers=headers,allow_redirects=False)
# req.encoding = 'utf8'
# # print('requesr...',req)
# # header  = req.headers['Location']
# # print('header...',header)
# root = etree.HTML(req.content)
# print('root...',root)

# # items = root.xpath('//ul/li[@class="list-item"]')
# items = root.xpath('//text()')

# print('items.....',items)









# readerme ==================
# 1. 302  header  = req.headers['Location']
