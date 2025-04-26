# 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET

# 내 인증키 (26년 12월까지임) : 33RX7OBHFFA28P4I07F3

# 원/일본엔(100엔) (한국은행 Raw Data / 월평균) 
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/731Y004/M/201001/201912/0000002/0000100/"
response = requests.get(url)

data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df

# 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
KRWper100Yen = df[columns_to_keep].copy()

KRWper100Yen = KRWper100Yen.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
KRWper100Yen['Date'] = KRWper100Yen['Date'].str[:4] + '-' + KRWper100Yen['Date'].str[4:] ## 연,월 구분
KRWper100Yen

#  KRWper100Yen 데이터타입 변경하기
KRWper100Yen['Date'] = pd.to_datetime(KRWper100Yen['Date'])
KRWper100Yen['Value'] = KRWper100Yen['Value'].astype(float)

# KRWper100Yen의 월별 Time path 시각화해보기
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(KRWper100Yen['Date'], KRWper100Yen['Value'], label='KRW per 100 JPY', color='orange', marker='o', markersize=4)

ax.xaxis.set_major_locator(mdates.YearLocator())  ## 1년 간격
ax.xaxis.set_minor_locator(mdates.MonthLocator())  ## 월별 보조 눈금
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  ## 연도 형식

ax.set_ylabel('KRWper100Yen', fontsize=12)
ax.set_xlabel('Date', fontsize=12)

ax.grid(which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.5)

ax.legend(fontsize=10)

plt.tight_layout()
plt.show()

# 기초통계량 요약 
summary = KRWper100Yen["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
summary.round(2)
