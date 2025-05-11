# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/40세미만/data')
os.getcwd()
#======================================================================================================#
# 1. 현재생활형편 CSI
## 1.1 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 raw data 불러오기 (한국은행 Open API)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/511Y002/M/201001/202412/FMCCD/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.3 필요한 칼럼만 가져와서 travel_consume_exp_CSI라는 새로운 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
travel_consume_exp_CSI = df[columns_to_keep].copy()
travel_consume_exp_CSI = travel_consume_exp_CSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
travel_consume_exp_CSI['Date'] = travel_consume_exp_CSI['Date'].str[:4] + '-' + travel_consume_exp_CSI['Date'].str[4:] ## 연,월 구분
travel_consume_exp_CSI
## 1.4 자료형태 변경
travel_consume_exp_CSI['Date'] = pd.to_datetime(travel_consume_exp_CSI['Date'])
travel_consume_exp_CSI['Value'] = travel_consume_exp_CSI['Value'].astype(float)
travel_consume_exp_CSI.info()
#======================================================================================================#
# 2. 수준변수에 대해서 ADF 검정
from statsmodels.tsa.stattools import adfuller
series = travel_consume_exp_CSI['Value']
## 2.1 aic 기준 / 상수항만 포함
result = adfuller(series,autolag='aic',regression='c')  
result[0]
result[1]
## 2.2 aic 기준 / 상수항 + 추세포함
result = adfuller(series,autolag='aic',regression='ct')  
result[0]
result[1]
## 2.3 bic 기준 / 상수항만 포함
result = adfuller(series,autolag='bic',regression='c')  
result[0]
result[1]
## 2.4 bic 기준 / 상수항 + 추세포함
result = adfuller(series,autolag='bic',regression='ct')  
result[0]
result[1]
#======================================================================================================#
# 3. 로그차분 변수에 대해서 ADF 검정
import numpy as np
travel_consume_exp_CSI['log_diff'] = np.log(travel_consume_exp_CSI['Value']).diff()
diff_series = travel_consume_exp_CSI['log_diff'].dropna()
## 3.1 aic 기준 / 상수항만 포함
result = adfuller(diff_series,autolag='aic',regression='c')  
result[0]
result[1]
## 3.2 aic 기준 / 상수항 + 추세포함
result = adfuller(diff_series,autolag='aic',regression='ct')  
result[0]
result[1]
## 3.3 bic 기준 / 상수항만 포함
result = adfuller(diff_series,autolag='bic',regression='c')  
result[0]
result[1]
## 3.4 bic 기준 / 상수항 + 추세포함
result = adfuller(diff_series,autolag='bic',regression='ct')  
result[0]
result[1]
#======================================================================================================#
