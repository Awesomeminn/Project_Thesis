# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석/Model 2')
os.getcwd()
#=======================================================================================================#
# 1. News Sentiment Index
## 1.1 필요한 패키지 임포트 
import requests
import pandas as pd
from xml.etree import ElementTree as ET
## 1.2 한국은행 Open API에서 Raw data 불러와서 확인
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/521Y001/M/201001/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df 
## 1.3 필요한 칼럼만 추출해서 NSI_m 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m
## 1.4 'Date' 컬럼 연/월 구분하고, 자료형 변경하기
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)
NSI_m.info()
## 1.5 NSI_m 기초통계량 
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
print(summary)
#=======================================================================================================#
