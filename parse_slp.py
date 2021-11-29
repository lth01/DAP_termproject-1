from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import schedule
import datetime
import requests

def get_price_usdt():
    url="https://www.coingecko.com/ko/코인/smooth-love-potion"
    response =requests.get(url)
    lines=response.text
    pos0=lines.find('no-wrap')
    pos1=lines.find('>',pos0,len(lines))
    pos2=lines.find('<',pos0,len(lines))
    now=datetime.datetime.now()
    nowDatetime=now.strftime('%Y-%m-%d %H:%M')
    nowDatetime2=now.strftime('%Y-%m-%d')
    
    f = open("./SLP_price/"+nowDatetime2,'a+')
    f.write(nowDatetime+" "+lines[pos1:pos2]+'\n')
    f.close()

    
schedule.every(1).minutes.do(get_price_usdt)



while True:
    schedule.run_pending()
    time.sleep(1)

