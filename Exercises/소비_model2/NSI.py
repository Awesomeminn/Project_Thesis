# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/소비_model2')
os.getcwd()
#======================================================================================================#
# 1. 데이터 사전작업
## 1.1 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 한국은행 Open API에서 Raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/100000/521Y001/M/201001/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.3 필요한 변수 추출해서 News 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
News = df[columns_to_keep].copy()
News = News.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
News['Date'] = News['Date'].str[:4] + '-' + News['Date'].str[4:] ## 연,월 구분
News
## 1.4 각 칼럼 Data type 변경하기
News['Date'] = pd.to_datetime(News['Date'])
News['Value'] = News['Value'].astype(float)
News.info()
#======================================================================================================#
# 2. 수준변수에 대해 ADF 검정
from statsmodels.tsa.stattools import adfuller
## 2.1 상수항만 포함하였을 때 
result = adfuller(News['Value'], autolag='aic', regression='c')
print(result[0])
print(result[1])
print(result[4])
## 2.2 상수항 + 추세를 가정하였을 때
result = adfuller(News['Value'], autolag='aic', regression='ct')
print(result[0])
print(result[1])
print(result[4])
#======================================================================================================#
# 3. 로그차분 변수에 대해 ADF 검정
## 3.1 로그차분 칼럼 생성
import numpy as np
News['log_diff'] = np.log(News['Value']).diff()
series = News['log_diff'].dropna()
## 3.2 상수항만
result = adfuller(series, autolag='aic', regression='c')
print(result[0])
print(result[1])
print(result[4])
## 3.3 상수항 및 추세 포함
result = adfuller(series, autolag='aic', regression='ct')
print(result[0])
print(result[1])
print(result[4])


