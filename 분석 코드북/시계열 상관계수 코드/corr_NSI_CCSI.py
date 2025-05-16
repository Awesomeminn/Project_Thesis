# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/250515')
os.getcwd()
#======================================================================================================#
# 1. News Sentiment Index
import requests
import pandas as pd
from xml.etree import ElementTree as ET
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/201501/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI = df[columns_to_keep].copy()
NSI = NSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI['Date'] = NSI['Date'].str[:4] + '-' + NSI['Date'].str[4:] ## 연,월 구분
NSI
NSI['Date'] = pd.to_datetime(NSI['Date'])
NSI['Value'] = NSI['Value'].astype(float)
NSI.info()
#======================================================================================================#
# 2. Composite Consumer Survey Index
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201501/202412/FME/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
CCSI = df[columns_to_keep].copy()
CCSI = CCSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CCSI['Date'] = CCSI['Date'].str[:4] + '-' + CCSI['Date'].str[4:] ## 연,월 구분
CCSI
CCSI['Date'] = pd.to_datetime(CCSI['Date'])
CCSI['Value'] = CCSI['Value'].astype(float)
CCSI.info()
#======================================================================================================#
# 3. 뉴스심리지수와 소비자심리지수의 산포도 (원계열)
import matplotlib.pyplot as plt
merged = pd.merge(NSI[['Date', 'Value']], CCSI[['Date', 'Value']], on='Date', suffixes=('_NSI', '_CCSI'))
plt.figure(figsize=(8, 6))
plt.scatter(merged['Value_NSI'], merged['Value_CCSI'], alpha=0.7)
plt.title('Scatter Plot of NSI vs. CCSI')
plt.xlabel('NSI Value')
plt.ylabel('CCSI Value')
plt.grid(True)
plt.tight_layout()
plt.show()
#======================================================================================================#
# 4. 뉴스심리지수와 소비자심리지수의 산포도 (로그차분변수)
## 4.1 로그차분 칼럼 생성
import numpy as np
NSI['ln_diff'] = np.log(NSI['Value']).diff()
CCSI['ln_diff'] = np.log(CCSI['Value']).diff()
NSI_lndiff = NSI[['Date', 'ln_diff']].dropna()
CCSI_lndiff = CCSI[['Date', 'ln_diff']].dropna()
## 4.2 시각화 
merged = pd.merge(NSI_lndiff, CCSI_lndiff, on='Date', suffixes=('_NSI', '_CCSI'))
plt.figure(figsize=(8, 6))
plt.scatter(merged['ln_diff_NSI'], merged['ln_diff_CCSI'], alpha=0.7)
plt.title('Scatter Plot of log-diff(NSI) vs. log-diff(CCSI)')
plt.xlabel('log-diff(NSI)')
plt.ylabel('log-diff(CCSI)')
plt.grid(True)
plt.tight_layout()
plt.show()
