import urllib
import urllib.request as req
from bs4 import BeautifulSoup

"""
第一篇使用python自身的urllib库爬取页面并解析，旨在熟悉urllib以及beautifulSoup相关方法的使用
目标爬取当当网书籍的第一第二第三级分类
"""
url = 'http://book.dangdang.com/'

# 设置header
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Host': 'book.dangdang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#构建request
reqeuest = req.Request(url=url,headers=headers)
"""
request= urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
"""
#发起请求获取页面
response = req.urlopen(reqeuest,timeout=60)
#创建BeautifulSoup实例
soup = BeautifulSoup(response.read(),from_encoding='gbk',features='html.parser')

div_lists = soup.find_all('div',attrs={'class':'level_one'})
#print(div_lists)
a_lists = []
for div_list in div_lists:
    for item in div_list.descendants:
        if item.name =='a':
            a_lists.append(item)

book_lists=[]

for a in a_lists:
    href = 'title:'+ a.attrs['title']+'|'+'nname:'+a.attrs['nname']+'|'+'href:'+a.attrs['href']
    book_lists.append(href)


for i in book_lists:
    print(i)





