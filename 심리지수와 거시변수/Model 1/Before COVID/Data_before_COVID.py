# Packages
import requests
import pandas as pd
from xml.etree import ElementTree as ET
# Getting Monthly NSI with using Open API (level)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/521Y001/M/201001/201912/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
columns_to_keep = ['TIME', 'DATA_VALUE']
NSI_m = df[columns_to_keep].copy()
NSI_m = NSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
NSI_m['Date'] = NSI_m['Date'].str[:4] + '-' + NSI_m['Date'].str[4:] ## 연,월 구분
NSI_m['Date'] = pd.to_datetime(NSI_m['Date'])
NSI_m['Value'] = NSI_m['Value'].astype(float)
# Descriptive Statistic (of NSI level variable)
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
# NSI_전년동기대비 증감률
NSI = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/data/NSI_Seasonally_diff_m_201001_201912.csv")
NSI = NSI.rename(columns={'변환': 'Date', '전년동기대비증감률': 'Value'})
NSI['Date'] = pd.to_datetime(NSI['Date'])
NSI['Value'] = NSI['Value'].astype(float)
#=====================================================================================================#
#=====================================================================================================#
# Getting Monthly CCSI with using Open API (level)
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201001/201912/FME/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
columns_to_keep = ['TIME', 'DATA_VALUE']
CCSI_m = df[columns_to_keep].copy()
CCSI_m = CCSI_m.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
CCSI_m['Date'] = CCSI_m['Date'].str[:4] + '-' + CCSI_m['Date'].str[4:] ## 연,월 구분
CCSI_m['Date'] = pd.to_datetime(CCSI_m['Date'])
CCSI_m['Value'] = CCSI_m['Value'].astype(float)
# Descriptive Statistic (of CCSI level variable)
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
# CCSI 전년동기대비 증감률
CCSI = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/data/CCSI_Seasonally_diff_m_201001_201912.csv")
CCSI = CCSI.rename(columns={'변환': 'Date', '전년동기대비증감률': 'Value'})
CCSI['Date'] = pd.to_datetime(CCSI['Date'])
CCSI['Value'] = CCSI['Value'].astype(float)
#=====================================================================================================#
#=====================================================================================================#
