# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수와 거시변수/Model 1/Before COVID')
os.getcwd()
#=====================================================================================================#
# 데이터 불러오고 패키지 임포트 
from Data_before_COVID import NSI_m, CCSI_m, NSI, CCSI
# pip install statsmodels 먼저 콘솔에 실행하고 아래코드 실행할 것
from statsmodels.tsa.stattools import adfuller
#===============================================================================================#
# NSI 수준 변수에 대한 ADF 검정
result = adfuller(NSI_m["Value"])
print("ADF - NSI level")
print(f'통계량: {result[0]}')
print(f'p-value: {result[1]}')
print(f'유의수준 및 기각역: {result[4]}')
# CCSI 수준 변수에 대한 ADF 검정
result = adfuller(CCSI_m["Value"])
print("ADF - CCSI level")
print(f'통계량: {result[0]}')
print(f'p-value: {result[1]}')
print(f'유의수준 및 기각역: {result[4]}')
#===============================================================================================#
# NSI 계절 차분 변수에 대한 ADF 검정
result = adfuller(NSI["Value"])
print("ADF - NSI Seasonally differenced")
print(f'통계량: {result[0]}')
print(f'p-value: {result[1]}')
print(f'유의수준 및 기각역: {result[4]}')
# CCSI 계절 차분 변수에 대한 ADF 검정
result = adfuller(CCSI["Value"])
print("ADF - CCSI Seasonally differenced")
print(f'통계량: {result[0]}')
print(f'p-value: {result[1]}')
print(f'유의수준 및 기각역: {result[4]}')