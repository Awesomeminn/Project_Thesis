# 0. 데이터 불러오기
import pandas as pd
df2 = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/경제심리와 소비지출/Try 1/data and ADF/소매업태별 판매액지수_14161707.csv")
df2
#========================================================================================================#
# 1. 데이터 자료형 변경
df2['Date'] = pd.to_datetime(df2['Date'])
df2.info()
#========================================================================================================#
# 2. 단위근 검정 _ ADF
## 2.1 백화점 소비판매액 지수
from statsmodels.tsa.stattools import adfuller
series1 = df2['department_store']
result = adfuller(series1,autolag='aic',regression='c')  
result[0]
result[1]
result = adfuller(series1,autolag='aic',regression='ct')  
result[0]
result[1]
## 2.2 대형마트 소비판매액 지수
series2 = df2['mart']
result = adfuller(series2,autolag='aic',regression='c')  
result[0]
result[1]
result = adfuller(series2,autolag='aic',regression='ct')  
result[0]
result[1]
## 2.3 슈퍼마켓 소비판매액 지수
series3 = df2['supermarket']
result = adfuller(series3,autolag='aic',regression='c')  
result[0]
result[1]
result = adfuller(series3,autolag='aic',regression='ct')  
result[0]
result[1]
