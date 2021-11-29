import numpy as np
import pandas as pd
import datetime

time_series=pd.date_range("16/11/2021","23/11/2021",freq="min")

time_series=time_series[1000:] #*내가 parsing하기 시작한 곳부터 측정해야함.

SLP_file=open("./SLP_price/2021-11-16-2",'r')
Ether_file=open("./Ether_axie_price/2021-11-16-ether",'r')
axie_file=open("./Ether_axie_price/2021-11-16-axie")
Player_count_file=open("./Player_count/2021-11-16-2",'r')

SLP_time_line=[]
SLP_price=[]
SLP={}
while(True):
    line=SLP_file.readline()
    if(line==''):
        break
    else:
        line_list=line.split()
        SLP_time_line.append(line_list[0]+" "+line_list[1])
        SLP_price.append(line_list[2])
        SLP[pd.to_datetime(line_list[0]+" "+line_list[1])]=line_list[2]




#여기까지가 timeline과 price분리
# count=0
SLP_series=pd.Series(SLP,index=time_series)


player_count_dict={}
while(True):
    line=Player_count_file.readline()
    if(line==''):
        break
    else:
        line_list=line.split()
        player_count_dict[pd.to_datetime(line_list[0]+" "+line_list[1][:5])]=line_list[2]
    
Player_series=pd.Series(player_count_dict,index=time_series)


axie_dict={}
while(True):
    line=axie_file.readline()
    if(line==''):
        break
    else:
        line_list=line.split()
        axie_dict[pd.to_datetime(line_list[0]+" "+line_list[1])]=str(line_list[2])

Axie_series=pd.Series(axie_dict,index=time_series)

Ether_dict={}
while(True):
    line=Ether_file.readline()
    if(line==''):
        break
    else:
        line_list=line.split()
        Ether_dict[pd.to_datetime(line_list[0]+" "+line_list[1])]=str(line_list[2])

Etehr_series=pd.Series(Ether_dict,index=time_series)        


print(SLP_series)
print(Axie_series)
print(Etehr_series)
print(Player_series)




SLP_file.close()
Ether_file.close()
axie_file.close()
Player_count_file.close();