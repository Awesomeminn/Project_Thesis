# 1. 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/data/merge.csv")
df
#======================================================================================================#
# 2. 날짜 인덱싱
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df = df.asfreq('MS')
#======================================================================================================#
# 3. VAR 모형 적합 및 최적시차 선정
from statsmodels.tsa.api import VAR
model = VAR(df)
lag_selection = model.select_order(maxlags=6)
print("AIC :", lag_selection.aic)
print("BIC :", lag_selection.bic)
print("FPE :", lag_selection.fpe)
print("HQIC:", lag_selection.hqic)
#======================================================================================================#
