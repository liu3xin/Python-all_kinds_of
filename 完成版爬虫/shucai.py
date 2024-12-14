#1. 提取单页数据
#2. 利用线程池提取全部数据
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

f = open('shuicia.txt',mode='w',encoding='utf-8')
def one_page_pa(url,data):
    resp = requests.post(url,data = data)
    tree = etree.HTML(resp.text)
    table = tree.xpath('//*[@id="bbs"]/div/div/div/div[4]/div[1]/div/table')

    trs = table.xpath('./tr')
    for tr in trs:
        txt = tr.xpath('./td/text()')
        f.write(txt)

if True:
    with ThreadPoolExecutor(100) as t:
        for i in range(1,2000):
            t.submit(one_page_pa,'http://www.xinfadi.com.cn/getPriceData.html',{'limit: 20',f'current:{i}','pubDateStartTime: ','pubDateEndTime: ','podPcatid: ','prodCatid: ','prodName: '})
f.close()
print('all over')

