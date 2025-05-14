# 1. 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/경제심리와 소비지출/Try 1/data and ADF/merge.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.asfreq('MS')
df.info()
#================================================================================================================#
# 2. VAR 모델 적합 및 최적시차 선정
from statsmodels.tsa.api import VAR
model = VAR(df)
lag_order_results = model.select_order(maxlags=6)
print("=== VAR Lag Order Selection ===")
print(lag_order_results.summary())
#================================================================================================================#
