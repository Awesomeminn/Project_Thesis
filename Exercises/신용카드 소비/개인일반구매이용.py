# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/working/소비심리')
os.getcwd()
#======================================================================================================#
# 1. 개인 일반구매 이용금액 데이터
## 1.1 한국은행 Open API에서 Raw data 끌어오기
import requests
import pandas as pd
from xml.etree import ElementTree as ET
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/100000/601Y003/M/200901/202412/201010/00/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 칼럼들 추출해서 데이터프레임 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
card_use_general = df[columns_to_keep].copy()
card_use_general = card_use_general.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
card_use_general['Date'] = card_use_general['Date'].str[:4] + '-' + card_use_general['Date'].str[4:] ## 연,월 구분
card_use_general
## 1.3 자료형 변환하기
card_use_general['Date'] = pd.to_datetime(card_use_general['Date'])
card_use_general['Value'] = card_use_general['Value'].astype(float)
card_use_general.info()
#======================================================================================================#
# 2. 수준 변수에 대해서 ADF 검정
from statsmodels.tsa.stattools import adfuller
def ADF(data):
    result = adfuller(data, autolag="bic", regression='c')
    print("---- Adfuller ----")
    print('ADF Statistic: %f' % result[0])
    print('p-value: %1.10f' % result[1])
    print('Lag: %d' % result[2])
    print('observation: %d' % result[3])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

ADF(card_use_general['Value'])
#======================================================================================================#
# 3. 로그 차분 후 ADF 검정
import numpy as np
diff_series = np.log(card_use_general['Value']).diff().dropna()
ADF(diff_series)
