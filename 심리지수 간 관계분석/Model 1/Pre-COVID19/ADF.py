# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석/Model 1/Pre-COVID19')
os.getcwd()
#======================================================================================================#
# cross_corr.py에서 merged 가져오기
from cross_corr import merged
merged
#=======================================================================================================#
import pandas as pd
from statsmodels.tsa.stattools import adfuller

regression_types = {
    'n': 'No Constant',
    'c': 'Constant Only',
    'ct': 'Constant + Trend'
}

results = []

for col in ['NSI', 'CCSI', 'BSI', 'BSI_exp']:
    series = merged[col].dropna()
    for reg in regression_types:
        adf_result = adfuller(series, regression=reg)
        results.append({
            'Variable': col,
            'Regression': regression_types[reg],
            'Test Statistic': adf_result[0],
            'p-value': adf_result[1],
            'Lags Used': adf_result[2],
            'Observations': adf_result[3],
            '1% Critical Value': adf_result[4].get('1%'),
            '5% Critical Value': adf_result[4].get('5%'),
            '10% Critical Value': adf_result[4].get('10%')
        })

adf_all_cases = pd.DataFrame(results)
print(adf_all_cases)
#====================================================================================================#
import numpy as np
regression_types = {
    'n': 'No Constant',
    'c': 'Constant Only',
    'ct': 'Constant + Trend'
}

results = []

# 로그차분
log_diff_df = merged[['NSI', 'CCSI', 'BSI', 'BSI_exp']].apply(lambda x: np.log(x).diff().dropna())

for col in log_diff_df.columns:
    series = log_diff_df[col]
    for reg in regression_types:
        adf_result = adfuller(series, regression=reg)
        results.append({
            'Variable': col,
            'Regression': regression_types[reg],
            'Test Statistic': adf_result[0],
            'p-value': adf_result[1],
            'Lags Used': adf_result[2],
            'Observations': adf_result[3],
            '1% Critical Value': adf_result[4].get('1%'),
            '5% Critical Value': adf_result[4].get('5%'),
            '10% Critical Value': adf_result[4].get('10%')
        })

logdiff_adf_df = pd.DataFrame(results)
print(logdiff_adf_df)
#=====================================================================================================#
log_diff_df = merged[['NSI', 'CCSI', 'BSI', 'BSI_exp']].apply(lambda x: np.log(x).diff())
# 날짜 컬럼 추가
log_diff_df['Date'] = merged['Date']
# NA 제거 및 인덱스 초기화
log_diff_df = log_diff_df.dropna().reset_index(drop=True)
# 결과 출력
print(log_diff_df.head())