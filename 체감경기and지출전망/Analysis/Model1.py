# 1. 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/data/merge1.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
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
# 3. 충격반응함수