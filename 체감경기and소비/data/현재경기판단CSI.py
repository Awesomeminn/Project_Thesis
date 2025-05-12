# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and소비/data')
os.getcwd()
#======================================================================================================#
# 1. 현재생활형편 CSI
## 1.1 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 raw data 불러오기 (한국은행 Open API)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/511Y002/M/201301/202412/FMAB/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.3 필요한 칼럼만 가져와서 curr_econ_CSI라는 새로운 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
curr_econ_CSI = df[columns_to_keep].copy()
curr_econ_CSI = curr_econ_CSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
curr_econ_CSI['Date'] = curr_econ_CSI['Date'].str[:4] + '-' + curr_econ_CSI['Date'].str[4:] ## 연,월 구분
curr_econ_CSI
## 1.4 자료형태 변경
curr_econ_CSI['Date'] = pd.to_datetime(curr_econ_CSI['Date'])
curr_econ_CSI['Value'] = curr_econ_CSI['Value'].astype(float)
curr_econ_CSI.info()
#======================================================================================================#
# 2. 수준변수에 대해서 ADF 검정
from statsmodels.tsa.stattools import adfuller
series = curr_econ_CSI['Value']
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
curr_econ_CSI['log_diff'] = np.log(curr_econ_CSI['Value']).diff()
diff_series = curr_econ_CSI['log_diff'].dropna()
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
