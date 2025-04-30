# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석/Model 1/Pre-COVID19')
os.getcwd()
#======================================================================================================#
# ADF.py에서 가져오기
from ADF import log_diff_df
#======================================================================================================#
log_diff_df.set_index('Date', inplace=True)
#======================================================================================================#
from statsmodels.tsa.api import VAR
# VAR 모델 초기화
model = VAR(log_diff_df)
# AIC 기준으로 최적 lag 선택
lag_selection = model.select_order(maxlags=12)
print(lag_selection.summary())
# 예: 최적 lag을 AIC 기준으로 선택
optimal_lag = lag_selection.bic
#======================================================================================================#
from statsmodels.tsa.stattools import grangercausalitytests
import itertools
import pandas as pd
max_lag = optimal_lag  # 또는 원하는 lag 수로 설정
variables = log_diff_df.columns.tolist()
results = []

# 모든 변수 쌍에 대해 검정: X → Y (X가 원인, Y가 결과)
for y, x in itertools.permutations(variables, 2):
    test_result = grangercausalitytests(log_diff_df[[y, x]], maxlag=max_lag, verbose=False)
    for lag in range(1, max_lag + 1):
        p_val = test_result[lag][0]['ssr_ftest'][1]
        results.append({
            'Cause': x,
            'Effect': y,
            'Lag': lag,
            'p-value': p_val,
            'Significant at 5%': p_val < 0.05
        })

# 결과를 데이터프레임으로 정리
granger_df = pd.DataFrame(results)
print(granger_df[granger_df['Significant at 5%'] == True].sort_values(by='p-value'))
#======================================================================================================#

