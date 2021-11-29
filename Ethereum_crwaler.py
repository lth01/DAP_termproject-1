from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import schedule
import datetime
import requests

def get_price():
    #### 모든 코인들의 코드명을 알아보자
    url = "https://api.upbit.com/v1/market/all"
    response = requests.get(url)
    market_list = response.json()
    ## 모든 코인들의 json결과
    ## {코인이름 : 코드명}을 담아낼 dictionary 그릇만들기
    market_dict = {}
    
    ## 빈 그릇에 json의 코인이름:코드명만 뽑아 dictionary 형태로 넣는다
    now=datetime.datetime.now()
    nowDatetime=now.strftime('%Y-%m-%d %H:%M')
    nowDatetime2=now.strftime('%Y-%m-%d')
    
    for i in market_list:
        if i['market'].split("-")[0] == "KRW": # KRW(한화) 가격정보의 코드명만 가져온다
            market_dict[i['korean_name']]=i['market'] #KRW 조건의 코인이름:코드명을 dictionary로 저장
    ######### 한글만 넣어도 가격이 나오는 API 처리 ###########
    coin_name = "이더리움" #여기다가 업비트에서 지원하는 코드명을 변수로 쓰면, 매칭된 코드명으로 코인정보+가격을 조회해 올 것이다.
    coin_code_name = market_dict[coin_name]
    coin_name2 = '엑시인피니티'
    coin_code_name2 = market_dict[coin_name2]
    coin_info_url = "https://api.upbit.com/v1/ticker?markets=" + str(coin_code_name)
    coin_info_url2 = "https://api.upbit.com/v1/ticker?markets=" + str(coin_code_name2)
    coin_info_response = requests.get(coin_info_url)
    coin_info_response2 = requests.get(coin_info_url2)
    coin_info_result = coin_info_response.json()[0]
    coin_info_result2 = coin_info_response2.json()[0]
    
    coin_result=coin_info_result['trade_price']
    coin_result2=coin_info_result2['trade_price']
    f = open("./Ether_axie_price/"+nowDatetime2,'a+')
    f.write(nowDatetime+" "+"이더리움 "+str(coin_result)+'\n')
    f.write(nowDatetime+" "+"엑시 "+str(coin_result2)+'\n')
    f.close()
    
    
schedule.every(1).minutes.do(get_price)



while True:
    schedule.run_pending()
    time.sleep(1)