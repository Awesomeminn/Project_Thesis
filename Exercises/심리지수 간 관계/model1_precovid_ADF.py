path = "C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/심리지수 간 관계"
import os
os.chdir(path)
os.getcwd()
#=====================================================================================================#
# 인수인계
from model1_precovid_data import NSI, CSI
#=====================================================================================================#
# 데이터 잘 왔는지 확인
NSI
CSI
#=====================================================================================================#
# 1. NSI_수준변수 ADF 검정
from statsmodels.tsa.stattools import adfuller
def ADF(data):

    result = adfuller(data, autolag="AIC")

    print("---- Adfuller ----")
    print('ADF Statistic: %f' % result[0])
    print('p-value: %1.10f' % result[1])
    print('Lag: %d' % result[2])
    print('observation: %d' % result[3])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

ADF(NSI['Value'])
# 2. CSI 각 항목 별 수준변수 ADF 검정 실시 
ADF(CSI['curr_econ'])
ADF(CSI['curr_living'])
ADF(CSI['econ_exp'])
ADF(CSI['job_exp'])
#=====================================================================================================#
# 3. NSI 로그차분 후 ADF 검정
import numpy as np
NSI['log_diff'] = np.log(NSI['Value']).diff()
result = adfuller(NSI['log_diff'].dropna())
print('ADF Test Statistic:', result[0])
print('p-value:', result[1])
print('Used lag:', result[2])
print('Number of observations:', result[3])
print('Critical Values:')
for key, value in result[4].items():
    print(f'   {key}: {value}')
# 4. CSI 로그차분 후 ADF 검정
variables = ['curr_living', 'curr_econ', 'econ_exp', 'job_exp']

for var in variables:
    CSI[f'{var}_logdiff'] = np.log(CSI[var]).diff()
    print(f'\n--- ADF Test for {var}_logdiff ---')
    result = adfuller(CSI[f'{var}_logdiff'].dropna())
    print(f'ADF Test Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print(f'Used lag: {result[2]}')
    print(f'Number of observations: {result[3]}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'   {key}: {value:.4f}')
#=====================================================================================================#
# 5. log_diff 합치기
CSI_logdiff = CSI[[
    'curr_living_logdiff',
    'curr_econ_logdiff',
    'econ_exp_logdiff',
    'job_exp_logdiff'
]].copy()
NSI_logdiff = NSI[['log_diff']].copy()
NSI_logdiff.rename(columns={'log_diff': 'NSI_logdiff'}, inplace=True)
import pandas as pd
CSI_logdiff.index = pd.to_datetime(CSI_logdiff.index)
NSI_logdiff.index = pd.to_datetime(NSI_logdiff.index)
merged_df = pd.merge(NSI_logdiff, CSI_logdiff, left_index=True, right_index=True, how='inner')
merged_df
