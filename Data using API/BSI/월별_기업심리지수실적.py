# 필요한 패키지 임포트 
import requests
import pandas as pd
from xml.etree import ElementTree as ET
# 한은 Open API에서 Raw data 가져오기
url = "http://ecos.bok.or.kr/api/StatisticSearch/33RX7OBHFFA28P4I07F3/json/kr/1/120/512Y013/M/201001/201912/99988//"
response = requests.get(url)
data = response.json()
rdata = data['StatisticSearch']["row"]
df = pd.DataFrame(rdata)
df