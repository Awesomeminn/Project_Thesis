# Model 1: NSI, CCSI, BSI_제조업전망 (Before COVID-19)
#==============================================================================================#
# 0. 필요한 패키지들 설치하기
import requests
import pandas as pd
from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#==============================================================================================#
# 1. News Sentiment Index
## 1.1 Raw data 불러오고, 잘 불러왔는지 확인하기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/201001/201912/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 칼럼 추출 및 날짜 열의 값들 연/월 구분하고, 변수명 변경하기
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분
NSI_m
## 1.3 NSI_m 데이터 타입 변경하고, 칼럼 별 자료형 확인
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)
NSI_m.info()
## 1.4 NSI_m Time Path 시각화  
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(NSI_m['Date'], NSI_m['Value'], label='Monthly News Sentiment Index (NSI)', color='orange', marker='o', markersize=4)
ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식
ax.set_ylabel('NSI', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
#==============================================================================================#
# 2. Composite Consumer Sentiment Index
## 2.1 Raw data 불러오고, 잘 불러왔는지 확인하기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201001/201912/FME/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 2.2 필요한 칼럼만 추출하고, 변수명 바꾸기 및 날짜 칼럼 연/월 구분
columns_to_keep = ['TIME', 'DATA_VALUE']
CCSI_m = df[columns_to_keep].copy()
CCSI_m = CCSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CCSI_m['Date'] = CCSI_m['Date'].str[:4] + '-' + CCSI_m['Date'].str[4:] ## 연,월 구분
CCSI_m
## 2.3 Data Types 변경 및 자료형 확인
CCSI_m['Date'] = pd.to_datetime(CCSI_m['Date'])
CCSI_m['Value'] = CCSI_m['Value'].astype(float)
CCSI_m.info()
## 2.4 CCSI_m Time Path 시각화
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(CCSI_m['Date'], CCSI_m['Value'], label='Composite Consumer Sentiment Index (CCSI)', color='orange', marker='o', markersize=4)
ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식
ax.set_ylabel('CCSI', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
#==============================================================================================#
# 3. BSI_기업심리지수(전망)
## 3.1 Raw data 불러와서 확인하기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/512Y014/M/201001/201912/99988/BX/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 3.2 필요한 칼럼 추출 및 변수명 변경 + 날짜 값 연/월 구분하기
columns_to_keep = ['TIME', 'DATA_VALUE']
BSI_exp_m = df[columns_to_keep].copy()
BSI_exp_m = BSI_exp_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
BSI_exp_m['Date'] = BSI_exp_m['Date'].str[:4] + '-' + BSI_exp_m['Date'].str[4:] ## 연,월 구분
BSI_exp_m
## 3.3 Data types 변경하고, 확인하기
BSI_exp_m['Date'] = pd.to_datetime(BSI_exp_m['Date'])
BSI_exp_m['Value'] = BSI_exp_m['Value'].astype(float)
BSI_exp_m.info()
## 3.4 BSI_exp_m Time Path 시각화 하기
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(BSI_exp_m['Date'], BSI_exp_m['Value'], label='Expected Business Sentiment Index (BSI_exp_m)', color='orange', marker='o', markersize=4)
ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식
ax.set_ylabel('BSI_exp_m', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()