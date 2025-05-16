# 데이터 불러오기
import pandas as pd
df = pd.read_csv('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model2/data1.csv')
df.set_index('Date', inplace=True)
df
#==========================================================================================================#
# 각 변수 별 ADF 검정 (원계열)
from statsmodels.tsa.stattools import adfuller
## 상수항만 고려했을 때
result = adfuller(df['Trading_Volume_KOSDAQ'],autolag='aic',regression='c')  
result[0]
result[1]
## 상수항, 추세 모두를 고려했을 때
result = adfuller(df['Trading_Volume_KOSDAQ'],autolag='aic',regression='ct')  
result[0]
result[1]
#==========================================================================================================#
# 각 변수 별 ADF 검정 (로그)
import numpy as np
## 상수항만 고려했을 때
df['Trading_Volume_KOSDAQ_log'] = np.log(df['Trading_Volume_KOSDAQ'])
result = adfuller(df['Trading_Volume_KOSDAQ_log'],autolag='aic',regression='c')  
result[0]
result[1]
## 상수항, 추세 모두를 고려했을 때
result = adfuller(df['Trading_Volume_KOSDAQ_log'],autolag='aic',regression='ct')  
result[0]
result[1]
#==========================================================================================================#
# 각 변수 별 ADF 검정 (로그차분) 
## 로그차분변수에 대해 검정 (상수항)
df['Trading_Volume_KOSDAQ_lndiff'] = df['Trading_Volume_KOSDAQ_log'].diff()
series = df['Trading_Volume_KOSDAQ_lndiff'].dropna()
result = adfuller(series,autolag='aic',regression='c')  
result[0]
result[1]
## 로그차분변수에 대해 검정 (상수항, 추세)
result = adfuller(series,autolag='aic',regression='ct')  
result[0]
result[1]
#==========================================================================================================#
df.to_csv('data2.csv', index=False)
