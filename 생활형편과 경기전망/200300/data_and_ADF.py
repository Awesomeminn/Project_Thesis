# 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/생활형편과 경기전망/200300/200_300.csv")
df

# 각 칼럼 자료형 변경하기
df['Date'] = pd.to_datetime(df['Date'])
df['living'] = df['living'].astype(float)
df['econ'] = df['econ'].astype(float)
df.info()

# ADF 검정: 생활형편CSI
from statsmodels.tsa.stattools import adfuller
## 수준변수에 대해 검정 (상수항 포함)
result = adfuller(df['living'],autolag='aic',regression='c')  
result[0]
result[1]
## 수준변수에 대해 검정 (상수항, 추세)
result = adfuller(df['living'],autolag='aic',regression='ct')  
result[0]
result[1]
## 로그변수에 대해 검정 (상수항)
import numpy as np
df['living_log'] = np.log(df['living'])
result = adfuller(df['living_log'],autolag='aic',regression='c')  
result[0]
result[1]
## 로그변수에 대해 검정 (상수항, 추세)
result = adfuller(df['living_log'],autolag='aic',regression='ct')  
result[0]
result[1]
## 로그차분변수에 대해 검정 (상수항)
df['living_lndiff'] = df['living_log'].diff()
series = df['living_lndiff'].dropna()
result = adfuller(series,autolag='aic',regression='c')  
result[0]
result[1]
## 로그차분변수에 대해 검정 (상수항, 추세)
result = adfuller(series,autolag='aic',regression='ct')  
result[0]
result[1]

# ADF 검정: 경기전망 CSI
## 수준변수에 대해 검정 (상수항 포함)
result = adfuller(df['econ'],autolag='aic',regression='c')  
result[0]
result[1]
## 수준변수에 대해 검정 (상수항, 추세)
result = adfuller(df['econ'],autolag='aic',regression='ct')  
result[0]
result[1]
## 로그변수에 대해 검정 (상수항)
import numpy as np
df['econ_log'] = np.log(df['econ'])
result = adfuller(df['econ_log'],autolag='aic',regression='c')  
result[0]
result[1]
## 로그변수에 대해 검정 (상수항, 추세)
result = adfuller(df['econ_log'],autolag='aic',regression='ct')  
result[0]
result[1]
## 로그차분변수에 대해 검정 (상수항)
df['econ_lndiff'] = df['econ_log'].diff()
series = df['econ_lndiff'].dropna()
result = adfuller(series,autolag='aic',regression='c')  
result[0]
result[1]
## 로그차분변수에 대해 검정 (상수항, 추세)
result = adfuller(series,autolag='aic',regression='ct')  
result[0]
result[1]

# 수정된 df csv로 저장하기
import os
os.chdir("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/생활형편과 경기전망/200300")
df.to_csv('200_300_6var.csv', index=False)
