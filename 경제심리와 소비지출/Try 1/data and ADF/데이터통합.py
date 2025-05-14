# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/경제심리와 소비지출/Try 1/data and ADF')
os.getcwd()
#======================================================================================================#
# 1. 앞에서 작업한 데이터 불러오기
from sentiment import df1
from consume import df2
#======================================================================================================#
import pandas as pd
dict = {
    'News': df1['News'],
    'curr_living_CSI': df1['curr_living_CSI'],
    'department_store': df2['department_store'],
    'mart': df2['mart'],
    'supermarket':df2['supermarket']
}
dates = df1['Date']
combined_df = pd.DataFrame(dict)
combined_df['Date'] = dates
combined_df.set_index('Date', inplace=True)
merge = combined_df.dropna()
merge
#======================================================================================================#
merge.to_csv('merge.csv', index=True)
