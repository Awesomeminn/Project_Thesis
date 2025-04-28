# 0. Basic Setting
import os
os.chdir(r"C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석")
from Model1_data import NSI_m, CCSI_m
from Model1_data import BSI_exp_m
print(NSI_m)
print(CCSI_m)
print(BSI_exp_m)
#======================================================================================================#
# 1. ADF Test (NSI_m level)
from statsmodels.tsa.stattools import adfuller
value_series = NSI_m['Value']
adf_result = adfuller(value_series, autolag='BIC')
print(f'ADF statistics : {adf_result[0]}')
print(f'p-value {adf_result[1]}')
print('critical values: ')
for key, value in adf_result[4].items():
    print(f"\t{key} {value}")
#======================================================================================================#
# 2. ADF Test (CCSI_m level)
value_series = CCSI_m['Value']
adf_result = adfuller(value_series , autolag='BIC')
print(f'ADF statistics : {adf_result[0]}')
print(f'p-value {adf_result[1]}')
print('critical values: ')
for key, value in adf_result[4].items():
    print(f"\t{key} {value}")
#======================================================================================================#
