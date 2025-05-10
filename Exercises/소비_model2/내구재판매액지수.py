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
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/100000/901Y100/M/201001/202412/G1/T3/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df 
## 1.3 필요한 칼럼 추출해서 durable_sales 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
durable_sales = df[columns_to_keep].copy()
durable_sales = durable_sales.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
durable_sales['Date'] = durable_sales['Date'].str[:4] + '-' + durable_sales['Date'].str[4:] ## 연,월 구분
durable_sales
## 1.4 각 칼럼 Data type 변경하기
durable_sales['Date'] = pd.to_datetime(durable_sales['Date'])
durable_sales['Value'] = durable_sales['Value'].astype(float)
durable_sales.info()
#======================================================================================================#
# 2. 수준변수에 대해 ADF 검정
from statsmodels.tsa.stattools import adfuller
## 2.1 상수항만 포함하였을 때 
result = adfuller(durable_sales['Value'], autolag='aic', regression='c')
print(result[0])
print(result[1])
print(result[4])
## 2.2 상수항 + 추세를 가정하였을 때
result = adfuller(durable_sales['Value'], autolag='aic', regression='ct')
print(result[0])
print(result[1])
print(result[4])
#======================================================================================================#
# 3. 로그차분 변수에 대해 ADF 검정
## 3.1 로그차분 칼럼 생성
import numpy as np
durable_sales['log_diff'] = np.log(durable_sales['Value']).diff()
series = durable_sales['log_diff'].dropna()
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