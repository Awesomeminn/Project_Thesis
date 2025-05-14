# 0. 데이터 불러오기
import pandas as pd
df1 = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/경제심리와 소비지출/Try 1/data and ADF/NSI_현재생활형편_계절차분_m_201301_202412.csv")
df1
#========================================================================================================#
# 1. 데이터 자료형 변경
df1['Date'] = pd.to_datetime(df1['Date'])
df1.info()
#========================================================================================================#
# 2. 단위근 검정 _ ADF
## 2.1 News Sentiment Index
from statsmodels.tsa.stattools import adfuller
series1 = df1['News']
result = adfuller(series1,autolag='aic',regression='c')  
result[0]
result[1]
result = adfuller(series1,autolag='aic',regression='ct')  
result[0]
result[1]
## 2.2 현재생활형편 CSI
series2 = df1['curr_living_CSI']
result = adfuller(series2,autolag='aic',regression='c')  
result[0]
result[1]
result = adfuller(series2,autolag='aic',regression='ct')  
result[0]
result[1]
