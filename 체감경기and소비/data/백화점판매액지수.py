# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and소비/data')
os.getcwd()
#======================================================================================================#
# 1. 백화점 판매액지수
## 1.1 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 raw data 불러오기 (한국은행 Open API)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/901Y098/M/201301/202412/I74B/I74C/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.3 필요한 칼럼만 가져와서 department_store라는 새로운 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
department_store = df[columns_to_keep].copy()
department_store = department_store.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
department_store['Date'] = department_store['Date'].str[:4] + '-' + department_store['Date'].str[4:] ## 연,월 구분
department_store
## 1.4 자료형태 변경
department_store['Date'] = pd.to_datetime(department_store['Date'])
department_store['Value'] = department_store['Value'].astype(float)
department_store.info()
#======================================================================================================#
# 2. 수준변수에 대해서 ADF 검정
from statsmodels.tsa.stattools import adfuller
series = department_store['Value']
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
department_store['log_diff'] = np.log(department_store['Value']).diff()
diff_series = department_store['log_diff'].dropna()
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
# 4. 합쳐서 df1 만들기
## 4.1 NSI랑 경기판단CSI 가져오기
from NSI import News
from 현재경기판단CSI import curr_econ_CSI
## 4.2 데이터 합치기
log_diff_dict = {
    'News': News['log_diff'],
    'curr_econ_CSI': curr_econ_CSI['log_diff'],
    'department_store': department_store['log_diff'],
}
dates = News['Date']
combined_df = pd.DataFrame(log_diff_dict)
combined_df['date'] = dates
combined_df.set_index('date', inplace=True)
merge = combined_df.dropna()
merge
#======================================================================================================#
merge.to_csv('merge1.csv', index=True)
