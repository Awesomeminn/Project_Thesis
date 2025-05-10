# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/소비_model2')
os.getcwd()
#======================================================================================================#
# 1. 작업한 데이터들 가져오기
from NSI import News
from 내구재지출전망CSI import CSI_durable_exp
from 내구재판매액지수 import durable_sales
from 내구재CPI import CPI_durable
#======================================================================================================#
# 2. 하나로 병합하기
import pandas as pd
## 2.1 pd.concat
news_logdiff = News[['Date', 'log_diff']].rename(columns={'log_diff': 'NSI_log_diff'})
cpi_logdiff = CPI_durable[['log_diff']].rename(columns={'log_diff': 'CPI_durable_log_diff'})
csi_logdiff = CSI_durable_exp[['log_diff']].rename(columns={'log_diff': 'CSI_durable_exp_log_diff'})
sales_logdiff = durable_sales[['log_diff']].rename(columns={'log_diff': 'durable_sales_log_diff'})
news_logdiff = news_logdiff.set_index('Date')
cpi_logdiff.index = news_logdiff.index
csi_logdiff.index = news_logdiff.index
sales_logdiff.index = news_logdiff.index
merge = pd.concat([news_logdiff, cpi_logdiff, csi_logdiff, sales_logdiff], axis=1)
merge = merge.dropna()
merge
