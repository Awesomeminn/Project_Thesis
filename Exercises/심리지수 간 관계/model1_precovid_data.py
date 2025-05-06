path = "C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/심리지수 간 관계"
import os
os.chdir(path)
os.getcwd()
#=====================================================================================================#
# 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#=====================================================================================================#
# 1. News Sentiment Index 
## 1.1 Raw data 한은 API에서 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/521Y001/M/200901/201912/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 칼럼 추출해서 NSI 데이터 프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI = df[columns_to_keep].copy()
NSI = NSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI['Date'] = NSI['Date'].str[:4] + '-' + NSI['Date'].str[4:] ## 연,월 구분
NSI
## 1.3 데이터타입 변경하기
NSI['Date'] = pd.to_datetime(NSI['Date'])
NSI['Value'] = NSI['Value'].astype(float)
NSI.info()
#=====================================================================================================#
# 2. CSI 4개 하위항목들
## 2.1 데이터 불러오기
CSI = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/data/CSI_현재생활형편_현재경기판단_향후경기전망_취업기회전망_코로나 전.csv")
CSI
## 2.2 데이터타입 변경하기
CSI["Date"] = pd.to_datetime(CSI['Date'])
CSI_columns = ["curr_living", "curr_econ", "econ_exp", "job_exp"]
for col in CSI_columns:
    CSI[col] = CSI[col].astype(float)
CSI.info()    
