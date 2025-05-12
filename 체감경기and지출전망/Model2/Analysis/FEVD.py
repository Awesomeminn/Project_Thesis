# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/Analysis')
os.getcwd()
#======================================================================================================#
# 1. 데이터 불러오기 
from VAR import df
#======================================================================================================#
import pandas as pd
from statsmodels.tsa.api import VAR
model = VAR(df)
results = model.fit(maxlags=12, ic='bic')  # BIC 기준 최적 시차
H = 10  
fevd = results.fevd(H)
for i in range(H):
    print(f"\n=== Forecast Error Variance Decomposition at t+{i+1} ===")
    print(fevd.summary())
