# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/working/소비심리')
os.getcwd()
#======================================================================================================#
# 1. 병합한 데이터 프레임 가져오기
from Data_Integration import df
df
#======================================================================================================#
# 2. 최적시차 선정 (bic 기준)
import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import grangercausalitytests
df = df.set_index('Date')
model = VAR(df)
lag_selection = model.select_order(maxlags=12)
selected_lag = lag_selection.selected_orders['bic']
print(f"최적 시차 (BIC 기준): {selected_lag}")
results = model.fit(selected_lag)
#======================================================================================================#
# 3. 그레인저 인과검정 실시
variables = df.columns.tolist()
for caused in variables:
    for causing in variables:
        if caused != causing:
            print(f"\n=== {causing} → {caused} (lag={selected_lag}) ===")
            grangercausalitytests(df[[caused, causing]], maxlag=selected_lag, verbose=True)