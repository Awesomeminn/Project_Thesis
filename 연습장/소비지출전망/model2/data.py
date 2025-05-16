# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model2')
os.getcwd()
#======================================================================================================#
# 한국은행 Open API 패키지
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#======================================================================================================#
# 데이터 불러오기
## 한국은행 Open API에서 raw data 불러오는 코드
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y014/M/201501/202412/2050000/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 필요한 칼럼만 추출해서 Trading_Volume_KOSDAQ 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
Trading_Volume_KOSDAQ = df[columns_to_keep].copy()
Trading_Volume_KOSDAQ = Trading_Volume_KOSDAQ.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
Trading_Volume_KOSDAQ['Date'] = Trading_Volume_KOSDAQ['Date'].str[:4] + '-' + Trading_Volume_KOSDAQ['Date'].str[4:] ## 연,월 구분
Trading_Volume_KOSDAQ
## 각 칼럼 데이터 타입 변경하기
Trading_Volume_KOSDAQ['Date'] = pd.to_datetime(Trading_Volume_KOSDAQ['Date'])
Trading_Volume_KOSDAQ['Value'] = Trading_Volume_KOSDAQ['Value'].astype(float)
Trading_Volume_KOSDAQ.info() 
#======================================================================================================#
# 데이터 프레임 병합 ('Date 칼럼은 첫트에만 실행하셈')
merged_df = Trading_Volume_KOSDAQ[['Date']].copy()
merged_df['Trading_Volume_KOSDAQ'] = Trading_Volume_KOSDAQ['Value'].values
print(merged_df)
#======================================================================================================#
# R 가져가서 분석하게 csv로 저장
merged_df.to_csv('data1.csv', index=False)
