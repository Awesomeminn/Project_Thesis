# 경로설정
import os
path = "C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/서울 아파트/model 1"
os.chdir(path)
os.getcwd()
#==================================================================================================#
# API 가져올 패키지 
import requests
import pandas as pd
from xml.etree import ElementTree as ET
#==================================================================================================#
# 1. News Sentiment Index
## 1.1 Raw data 한은 API에서 불러오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/1000/521Y001/M/201501/202412/A001/"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df