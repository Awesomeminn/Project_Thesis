# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/data')
os.getcwd()
#======================================================================================================#
# 1. 작업한 데이터들 다 가져오기
from NSI import News
from 현재경기판단CSI import curr_econ_CSI
from 내구재지출전망CSI import durable_consume_exp_CSI
from 외식비지출전망CSI import eatout_consume_exp_CSI
#======================================================================================================#
# 2. 데이터 프레임 만들기
import pandas as pd
log_diff_dict = {
    'News': News['log_diff'],
    'curr_econ_CSI': curr_econ_CSI['log_diff'],
    'durable_consume_exp_CSI': durable_consume_exp_CSI['log_diff'],
    'eatout_consume_exp_CSI': eatout_consume_exp_CSI['log_diff'],
}
dates = News['Date']
combined_df = pd.DataFrame(log_diff_dict)
combined_df['date'] = dates
combined_df.set_index('date', inplace=True)
merge = combined_df.dropna()
merge
#======================================================================================================#
merge.to_csv('merge.csv', index=True)
