import requests
url = 'https://pan.baidu.com/share/streaming?channel=chunlei&uk=4503602831802115&fid=228979580419604&sign=f6b7fc4b8fcf6c6c5c2c37c68562eea9a27c2dbc&timestamp=1725693724&shareid=52671674350&type=M3U8_AUTO_720&vip=0&jsToken=624BFB0B0FCB982BEC6632AD7A7FF1B22F380918448C683C1EAA9BC94C9ABA80C3CEC30F8446FB47FAA57913E8DCD5FF498CDECCD7A18B169E9E66F2A981778D&isplayer=1&check_blue=1&adToken='
resp = requests.get(url)
rest = resp.text
ress = rest.split('#EXTINF:')
for i in ress:
    for r in range(1,8):
        r = str(r)
        resv = i.strip('{r},')
        if resv.startswith('http'):
            print(resv)
 
