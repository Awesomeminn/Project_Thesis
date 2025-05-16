# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model1')
os.getcwd()
#======================================================================================================#
# 한국은행 Open API 패키지
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#======================================================================================================#
# 1. 내구재 소비지출전망 CSI
## 1.1 한국은행 Open API에서 raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/511Y002/M/201501/202412/FMCCA/99988/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 1.2 필요한 칼럼만 추출해서 durable_consume_exp_CSI 데이터프레임 생성
columns_to_keep = ['TIME', 'DATA_VALUE']
durable_consume_exp_CSI = df[columns_to_keep].copy()
durable_consume_exp_CSI = durable_consume_exp_CSI.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
durable_consume_exp_CSI['Date'] = durable_consume_exp_CSI['Date'].str[:4] + '-' + durable_consume_exp_CSI['Date'].str[4:] ## 연,월 구분
durable_consume_exp_CSI
## 1.3 각 칼럼 데이터 타입 변경하기
durable_consume_exp_CSI['Date'] = pd.to_datetime(durable_consume_exp_CSI['Date'])
durable_consume_exp_CSI['Value'] = durable_consume_exp_CSI['Value'].astype(float)
durable_consume_exp_CSI.info() 
#======================================================================================================#
# 2. 국산 승용차 판매액지수
## 2.1 한국은행 Open API에서 raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y100/M/201501/202412/G111/T2/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 2.2 필요한 칼럼만 추출해서 kor_car_sell 데이터 프레임 생성
kor_car_sell = df[columns_to_keep].copy()
kor_car_sell = kor_car_sell.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
kor_car_sell['Date'] = kor_car_sell['Date'].str[:4] + '-' + kor_car_sell['Date'].str[4:] ## 연,월 구분
kor_car_sell
## 2.3 각 칼럼 데이터타입 변경하기
kor_car_sell['Date'] = pd.to_datetime(kor_car_sell['Date'])
kor_car_sell['Value'] = kor_car_sell['Value'].astype(float)
kor_car_sell.info()
#======================================================================================================#
# 3. 수입 승용차 판매액지수
## 3.1 한국은행 Open API에서 raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y100/M/201501/202412/G112/T2/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 3.2 필요한 칼럼만 추출해서 import_car_sell 데이터 프레임 생성
import_car_sell = df[columns_to_keep].copy()
import_car_sell = import_car_sell.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
import_car_sell['Date'] = import_car_sell['Date'].str[:4] + '-' + import_car_sell['Date'].str[4:] ## 연,월 구분
import_car_sell
## 3.3 각 칼럼 데이터타입 변경하기
import_car_sell['Date'] = pd.to_datetime(import_car_sell['Date'])
import_car_sell['Value'] = import_car_sell['Value'].astype(float)
import_car_sell.info()
#======================================================================================================#
# 4. 가전제품 판매액지수
## 4.1 한국은행 Open API에서 raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y100/M/201501/202412/G12/T2/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 4.2 필요한 칼럼만 추출해서 home_appliances 데이터 프레임 생성
home_appliances = df[columns_to_keep].copy()
home_appliances = home_appliances.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
home_appliances['Date'] = home_appliances['Date'].str[:4] + '-' + home_appliances['Date'].str[4:] ## 연,월 구분
home_appliances
## 4.3 각 칼럼 데이터타입 변경하기
home_appliances['Date'] = pd.to_datetime(home_appliances['Date'])
home_appliances['Value'] = home_appliances['Value'].astype(float)
home_appliances.info()
#======================================================================================================#
# 5. 가구 판매액지수
## 5.1 한국은행 Open API에서 raw data 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/901Y100/M/201501/202412/G14/T2/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df
## 5.2 필요한 칼럼만 추출해서 furniture라는 데이터프레임 생성하기
furniture = df[columns_to_keep].copy()
furniture = furniture.rename(columns={'TIME': 'Date', 'DATA_VALUE': 'Value'})
furniture['Date'] = furniture['Date'].str[:4] + '-' + furniture['Date'].str[4:] ## 연,월 구분
furniture
## 5.3 각 칼럼 데이터타입 변경하기
furniture['Date'] = pd.to_datetime(furniture['Date'])
furniture['Value'] = furniture['Value'].astype(float)
furniture.info()
#======================================================================================================#
# 6. 데이터프레임 병합
merged_df = durable_consume_exp_CSI[['Date']].copy()
merged_df['durable_consume_exp_CSI'] = durable_consume_exp_CSI['Value'].values
merged_df['furniture'] = furniture['Value'].values
merged_df['home_appliances'] = home_appliances['Value'].values
merged_df['import_car_sell'] = import_car_sell['Value'].values
merged_df['kor_car_sell'] = kor_car_sell['Value'].values
print(merged_df)
#======================================================================================================#
# 7. R 가져가서 분석하게 csv로 저장
merged_df.to_csv('data1.csv', index=False)
