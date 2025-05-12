# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/Analysis')
os.getcwd()
#======================================================================================================#
# 데이터 가져오기
from VAR import df
df
#======================================================================================================#
# 그레인저 인과성 검정
import pandas as pd
import numpy as np
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import grangercausalitytests
model = VAR(df)
results = model.fit(maxlags=12, ic='bic')
granger_results = results.test_causality('durable_consume_exp_CSI', 'eatout_consume_exp_CSI', kind='f')
print(granger_results.summary())
