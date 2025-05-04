# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석/Model 1/Post-COVID19')
os.getcwd()
#======================================================================================================#
# 필요한 패키지 임포트 
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#======================================================================================================#
# 1. 뉴스심리지수 NSI
## 1.1 한국은행 Open API에서 가져오고 잘 불러왔는지 확인하기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/202001/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 칼럼만 추출해서 NSI_m 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m
## 1.3 'Date' 컬럼 연/월 구분하고, 자료형 변경하기
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)
NSI_m.info()
## 1.4 NSI_m 기초통계량 
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
#======================================================================================================#
# 2. 소비자 심리지수 CCSI
## 2.1 Open API에서 가져오고, 잘 불러왔는지 확인하기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/202001/202412/FME/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 2.2 필요한 칼럼만 추출해서 CCSI_m 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
CCSI_m = df[columns_to_keep].copy()
CCSI_m = CCSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CCSI_m['Date'] = CCSI_m['Date'].str[:4] + '-' + CCSI_m['Date'].str[4:] ## 연,월 구분
CCSI_m
## 2.3 'Date' 컬럼 연/월 구분하고, 자료형 변경하기
CCSI_m['Date'] = pd.to_datetime(CCSI_m['Date'])
CCSI_m['Value'] = CCSI_m['Value'].astype(float)
CCSI_m.info()
## 2.4 NSI_m 기초통계량 
summary = CCSI_m["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
print("===CCSI 기초통계량===")
print(summary)
#======================================================================================================#
# 3. 기업심리지수(전망) BSI_exp_m
## 3.1 Open API에서 raw data 가져오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/512Y014/M/202001/202412/99988/BX/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 3.2 필요한 칼럼 추출 및 변수명 변경하고 BSI_exp_m 데이터프레임 생성하기
columns_to_keep = ['TIME', 'DATA_VALUE']
BSI_exp_m = df[columns_to_keep].copy()
BSI_exp_m = BSI_exp_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
BSI_exp_m['Date'] = BSI_exp_m['Date'].str[:4] + '-' + BSI_exp_m['Date'].str[4:] ## 연,월 구분
BSI_exp_m
## 3.3 두 칼럼 데이터타입 변경하기
BSI_exp_m['Date'] = pd.to_datetime(BSI_exp_m['Date'])
BSI_exp_m['Value'] = BSI_exp_m['Value'].astype(float)
## 3.4 BSI_exp_m 기초통계량
summary = BSI_exp_m["Value"].agg(["mean", "median", "max", "min", "var", "std"])
summary = summary.rename({
    "mean": "평균",
    "median": "중앙값",
    "max": "최댓값",
    "min": "최솟값",
    "var": "분산",
    "std": "표준편차"
})
print("===BSI_exp 기초통계량===")
summary.round(2)
#======================================================================================================#
# 4. 기업심리지수(실적) BSI_m
## 4.1 한국은행 Open API에서 raw data 가져오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/512Y013/M/202001/202412/99988/AX/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 4.2 분석에 필요한 칼럼 추출하고, 칼럼명 변경해서 BSI_m Data frame 만들기
columns_to_keep = ['TIME', 'DATA_VALUE']
BSI_m = df[columns_to_keep].copy()
BSI_m = BSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
BSI_m['Date'] = BSI_m['Date'].str[:4] + '-' + BSI_m['Date'].str[4:] ## 연,월 구분
BSI_m
## 4.3 데이터타입 변경하기
BSI_m['Date'] = pd.to_datetime(BSI_m['Date'])
BSI_m['Value'] = BSI_m['Value'].astype(float)
BSI_m.info()
