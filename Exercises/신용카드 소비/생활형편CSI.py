# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/working/소비심리')
os.getcwd()
#======================================================================================================#
# 1. CSI_현재생활형편
## 1.1 한국은행 Open API에서 raw data 가져오기
import requests
import pandas as pd
from xml.etree import ElementTree as ET
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/100000/511Y002/M/200901/202412/FMAA/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 현재생활형편 CSI 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
CSI_curr_living = df[columns_to_keep].copy()
CSI_curr_living = CSI_curr_living.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CSI_curr_living['Date'] = CSI_curr_living['Date'].str[:4] + '-' + CSI_curr_living['Date'].str[4:] ## 연,월 구분
CSI_curr_living
## 1.3 데이터타입 변경하기
CSI_curr_living['Date'] = pd.to_datetime(CSI_curr_living['Date'])
CSI_curr_living['Value'] = CSI_curr_living['Value'].astype(float)
CSI_curr_living.info()
#======================================================================================================#
# 2. 수준 변수에 대해서 ADF 검정
from statsmodels.tsa.stattools import adfuller
def ADF(data):
    result = adfuller(data, autolag="aic", regression='c')
    print("---- Adfuller ----")
    print('ADF Statistic: %f' % result[0])
    print('p-value: %1.10f' % result[1])
    print('Lag: %d' % result[2])
    print('observation: %d' % result[3])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

ADF(CSI_curr_living['Value'])
#======================================================================================================#
# 3. 로그차분 후 ADF 검정 수행
import numpy as np
diff_series = np.log(CSI_curr_living['Value']).diff().dropna()
ADF(diff_series)
