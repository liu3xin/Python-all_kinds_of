import requests
import re
from concurrent.futures import ThreadPoolExecutor

f = open('xigua.txt',mode = 'w',encoding='gbk')

def one_page(url):
    resp = requests.get(url)
    object1 = re.compile(r'"text":(?P<ping>.*?),',re.S)
    object2 = re.compile(r'"user_name":(?P<name>.*?),',re.S)

    result1 = object1.finditer(resp.text)
    result2 = object2.finditer(resp.text)
    ping = []
    name = []
    value1 = {}
    
    for i in result1:
        ping.append(str(i.group('ping')))
    for ii in result2:
        name.append(str(ii.group('name')))
    num = int(len(name))
    for it in range(num):
        f.write(f'{name[it]}:{ping[it]}\n')
        
if True:
    with ThreadPoolExecutor(100) as t:
        for im in range(1,2000):
            im = im*10
            t.submit(one_page,f'https://www.ixigua.com/tlb/comment/article/v5/tab_comments/?tab_index=0&count=10&offset={im}&group_id=7421465700525179429&item_id=7421465700525179429&aid=1768')

f.close()
print('over')
