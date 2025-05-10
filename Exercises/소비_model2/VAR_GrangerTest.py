# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/소비_model2')
os.getcwd()
#======================================================================================================#
from Data_Integration import merge
merge
#======================================================================================================#
# 1. 필요한 패키지 임포트 및 VAR 적합
import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import grangercausalitytests
model = VAR(merge)
# 2. 최적시차 선택
lag_selection = model.select_order(maxlags=12)
print("각 기준별 최적 시차:")
print(f"AIC   : {lag_selection.aic}")
print(f"BIC   : {lag_selection.bic}")
print(f"FPE   : {lag_selection.fpe}")
print(f"HQIC  : {lag_selection.hqic}")
# 3. 그레인저 인과관계 검정 (이거 코드 바꿔서 돌려보기)
grangercausalitytests(
    merge[['durable_sales_log_diff', 'CSI_durable_exp_log_diff']],  ## 뒤에가 앞에 변수를 선행하는가?
    maxlag=1,
    verbose=True
)
