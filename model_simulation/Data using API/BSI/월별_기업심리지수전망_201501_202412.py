# 필요한 패키지 임포트
import requests
import pandas as pd
from xml.etree import ElementTree as ET

# 내 인증키 (26년 12월까지임) : 33RX7OBHFFA28P4I07F3

# 월별 BSI_전망 (한국은행 Raw Data) (전 산업 / 기업심리지수 전망)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/512Y014/M/201501/202412/99988/BX/"
response = requests.get(url)

data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df

# 필요한 칼럼만 추출하고, 변수명 바꾸기
columns_to_keep = ['TIME', 'DATA_VALUE']
BSI_exp_m = df[columns_to_keep].copy()

BSI_exp_m = BSI_exp_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
BSI_exp_m['Date'] = BSI_exp_m['Date'].str[:4] + '-' + BSI_exp_m['Date'].str[4:] ## 연,월 구분
BSI_exp_m

#  BSI_exp_m 데이터타입 변경하기
BSI_exp_m['Date'] = pd.to_datetime(BSI_exp_m['Date'])
BSI_exp_m['Value'] = BSI_exp_m['Value'].astype(float)

# BSI_exp_m의 월별 Time path 시각화해보기
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

# 기초통계량 요약 
summary = BSI_exp_m["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
summary.round(2)