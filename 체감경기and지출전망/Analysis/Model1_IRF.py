# 1. 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/data/merge1.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.info()
#================================================================================================================#
# 2. VAR 모형 적합
