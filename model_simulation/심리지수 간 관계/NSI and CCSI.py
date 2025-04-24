# 0. 201501부터 202412까지 120개 관측치임
#===================================================================================================================#
# 1. NSI 불러오기 

## 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET

## 내 인증키 (26년 12월까지임) : 33RX7OBHFFA28P4I07F3

## 월별 NSI (한국은행 Raw Data)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/201501/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df

## 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분

## NSI 데이터타입 변경하기
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)

## 데이터 최종 확인
print(NSI_m)
print(NSI_m.info())
#===================================================================================================================#
# 2. CCSI 불러오기 

## 월별 NSI (한국은행 Raw Data)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201501/202412/FME/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df

## 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
CCSI_m = df[columns_to_keep].copy()
CCSI_m = CCSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CCSI_m['Date'] = CCSI_m['Date'].str[:4] + '-' + CCSI_m['Date'].str[4:] ## 연,월 구분

## CCSI 데이터타입 변경하기
CCSI_m['Date'] = pd.to_datetime(CCSI_m['Date'])
CCSI_m['Value'] = CCSI_m['Value'].astype(float)

## 데이터 최종 확인
print(CCSI_m)
print(CCSI_m.info())
#===================================================================================================================#
# 3. 데이터 시각화
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))

## Plot Consumer Confidence Index (CCSI)
plt.plot(CCSI_m['Date'], CCSI_m['Value'], label='CCSI (Consumer Confidence Index)', linewidth=2)

## Plot News Sentiment Index (NSI)
plt.plot(NSI_m['Date'], NSI_m['Value'], label='NSI (News Sentiment Index)', linewidth=2, linestyle='--')

## Formatting the plot
plt.title('Consumer Confidence vs News Sentiment (2015–2024)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Index Value', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
#===================================================================================================================#
# 4. 시계열 안정성 검정 (ADF, PP, KPSS)
