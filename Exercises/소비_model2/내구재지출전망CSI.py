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
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/100000/511Y002/M/201001/202412/FMCCA/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df 
## 1.3 필요한 칼럼 추출해서 CSI_durable_exp 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
CSI_durable_exp = df[columns_to_keep].copy()
CSI_durable_exp = CSI_durable_exp.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CSI_durable_exp['Date'] = CSI_durable_exp['Date'].str[:4] + '-' + CSI_durable_exp['Date'].str[4:] ## 연,월 구분
CSI_durable_exp
## 1.4 각 칼럼 Data type 변경하기
CSI_durable_exp['Date'] = pd.to_datetime(CSI_durable_exp['Date'])
CSI_durable_exp['Value'] = CSI_durable_exp['Value'].astype(float)
CSI_durable_exp.info()
#======================================================================================================#
# 2. 수준변수에 대해 ADF 검정
from statsmodels.tsa.stattools import adfuller
## 2.1 상수항만 포함하였을 때 
result = adfuller(CSI_durable_exp['Value'], autolag='aic', regression='c')
print(result[0])
print(result[1])
print(result[4])
## 2.2 상수항 + 추세를 가정하였을 때
result = adfuller(CSI_durable_exp['Value'], autolag='aic', regression='ct')
print(result[0])
print(result[1])
print(result[4])
#======================================================================================================#
# 3. 로그차분 변수에 대해 ADF 검정
## 3.1 로그차분 칼럼 생성
import numpy as np
CSI_durable_exp['log_diff'] = np.log(CSI_durable_exp['Value']).diff()
series = CSI_durable_exp['log_diff'].dropna()
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










