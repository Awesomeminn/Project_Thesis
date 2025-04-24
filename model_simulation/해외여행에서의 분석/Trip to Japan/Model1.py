# 0. Model1: 일본여행 (Before COVID)
#========================================================================================================================#
# 1. News Sentiment Index
## 1.1 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 내 인증키 (26년 12월까지임) : 33RX7OBHFFA28P4I07F3
## 1.3 월별 NSI (한국은행 Raw Data)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/201001/201912/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.4 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분
NSI_m
## 1.5 NSI 데이터타입 변경하기
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)
NSI_m.info()
## 1.6 NSI 시각화
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(NSI_m['Date'], NSI_m['Value'], label='Monthly News Sentiment Index (2010.01 ~ 2019.12)', color='orange', marker='o', markersize=4)
ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식
ax.set_ylabel('NSI_m', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
## 1.7 기초통계량
summary = NSI_m["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
print("===NSI 기초통계량===")
print(summary.round(2))
#========================================================================================================================#
# 2. CSI_현재생활형편
## 2.1 월별 한국은행 Raw data (201501to202412)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201001/201912/FMAA/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 2.2 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
CSI_life_m = df[columns_to_keep].copy()
CSI_life_m = CSI_life_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CSI_life_m['Date'] = CSI_life_m['Date'].str[:4] + '-' + CSI_life_m['Date'].str[4:] ## 연,월 구분
CSI_life_m
## 2.3 CSI_life_m 데이터타입 변경하기
CSI_life_m['Date'] = pd.to_datetime(CSI_life_m['Date'])
CSI_life_m['Value'] = CSI_life_m['Value'].astype(float)
CSI_life_m.info()
## 2.4 CSI_life_m의 월별 Time path 시각화해보기
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(CSI_life_m['Date'], CSI_life_m['Value'], label='Consumer Sentiment Index (Currently lifestyle)', color='orange', marker='o', markersize=4)
ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식
ax.set_ylabel('CSI_life_m', fontsize=12)
ax.set_xlabel('Date', fontsize=12)
ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)
ax.legend(fontsize=10)
plt.tight_layout()
plt.show()
## 2.5 기초통계량 요약 
summary = CSI_life_m["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
print("===CSI_life_m 기초통계량===")
print(summary.round(2))
#========================================================================================================================#