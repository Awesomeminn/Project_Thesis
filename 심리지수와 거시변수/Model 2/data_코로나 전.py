# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수와 거시변수/Model 2')
os.getcwd()
#======================================================================================================#
# Open API 긁어올 때 필요한 패키지
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#======================================================================================================#
# 1. CSI_취업기회전망 
## 1.1 Raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201001/201912/FMBE/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 변수들만 추출해서 CSI_job_exp 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
CSI_job_exp = df[columns_to_keep].copy()
CSI_job_exp = CSI_job_exp.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CSI_job_exp['Date'] = CSI_job_exp['Date'].str[:4] + '-' + CSI_job_exp['Date'].str[4:] ## 연,월 구분
CSI_job_exp
## 1.3 분석을 위해 자료형 변환하기
CSI_job_exp['Date'] = pd.to_datetime(CSI_job_exp['Date'])
CSI_job_exp['Value'] = CSI_job_exp['Value'].astype(float)
CSI_job_exp.info()
summary = CSI_job_exp["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
print("===취업전망CSI 기초통계량===")
print(summary)
#======================================================================================================#
