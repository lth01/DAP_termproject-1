from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import schedule
import datetime

def save_file(): 
    html=urlopen("https://playercounter.com/axie-infinity/")
    bsObject=BeautifulSoup(html,"html.parser")
    now=datetime.datetime.now()
    nowDatetime=now.strftime('%Y-%m-%d %H:%M:%S')
    nowDatetime2=now.strftime('%Y-%m-%d')
    
    lines=bsObject.select_one('.entry-content').get_text()
    lines=lines[1:lines.find("Players Online")-1] #? Plyaers Online전에 나오는 player수를 파싱
    
    f=open("./Player_count/"+nowDatetime2,'a+')
    f.write(nowDatetime+" "+lines+'\n')
    f.close()


schedule.every(1).minutes.do(save_file)


while True:
    schedule.run_pending()
    time.sleep(1)
#*<div class="entry-content"> 다음줄이 온라인 플레이어의 수를 나타내는 줄임.
