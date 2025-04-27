# 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET

# 내 인증키 (26년 12월까지임) : 33RX7OBHFFA28P4I07F3

# 아파트 매매 실거래 가격지수 (전국) (한국은행 Raw Data) 
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y089/M/201501/202412/100/"
response = requests.get(url)

data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df

# 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
APT_N = df[columns_to_keep].copy()

APT_N = APT_N.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
APT_N['Date'] = APT_N['Date'].str[:4] + '-' + APT_N['Date'].str[4:] ## 연,월 구분
APT_N

#  APT_N 데이터타입 변경하기
APT_N['Date'] = pd.to_datetime(APT_N['Date'])
APT_N['Value'] = APT_N['Value'].astype(float)

# APT_N의 월별 Time path 시각화해보기
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(APT_N['Date'], APT_N['Value'], label='Monthly Nationalwide Apartment Price Index (APT_N)', color='orange', marker='o', markersize=4)

ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식

ax.set_ylabel('APT_N', fontsize=12)
ax.set_xlabel('Date', fontsize=12)

ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)

ax.legend(fontsize=10)

plt.tight_layout()
plt.show()

# 기초통계량 요약 
summary = APT_N["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
summary.round(2)
