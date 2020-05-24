#-*-coding:utf-8-*-
import urllib
import urllib.request as req
import urllib.error as err
from bs4 import BeautifulSoup

"""
第一篇使用python自身的urllib库爬取页面并解析，旨在熟悉urllib以及beautifulSoup相关方法的使用
目标爬取当当网书籍的第一第二第三级分类
"""

def get_request(url):
    """传入url获取urllib.request.Request"""
    # 设置header
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Host': 'book.dangdang.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    #构建request
    request = req.Request(url=url,headers=headers)
    """
    request= urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
    """
    return  request

def get_response(Request):

    #发起请求获取页面
    try :
        response = req.urlopen(Request,timeout=60)

    except err.HTTPError as e1:
        print('=======================')
    except err.URLError as e:
        print('异常++++++++++++++++++++++++++++++=')
        print(e.ecode)
        print(e.reason)

    soup = BeautifulSoup(response.read(), from_encoding='gbk', features='html.parser')
    return soup



def get_tag(soup):
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

    return book_lists



if __name__ == '__main__':
    url = 'http://book.dangdang.com/'
    request = get_request(url)
    soup = get_response(request)
    book_lists = get_tag(soup)

    for i in book_lists:
        print(i)





