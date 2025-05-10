# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/working/소비심리')
os.getcwd()
#======================================================================================================#
# 1. 각 파일에서 데이터프레임들 불러오기!
## 1.1 from ~ import
from NSI import NSI_df
from 개인일반구매이용 import card_use_general
from 개인할부구매이용 import card_use_installment
from 생활형편CSI import CSI_curr_living
## 1.2 차분계열 만들어놓기
import numpy as np
NSI_df['log_diff'] = np.log(NSI_df['Value']).diff()
card_use_general['log_diff'] = np.log(card_use_general['Value']).diff()
card_use_installment['log_diff'] = np.log(card_use_installment['Value']).diff()
CSI_curr_living['log_diff'] = np.log(CSI_curr_living['Value']).diff()
## 1.3 로그차분 칼럼들 하나의 데이터 프레임으로 병합 with NaN 제거
import pandas as pd
df = pd.DataFrame({
    'Date':NSI_df['Date'],
    'NSI_df_log_diff':NSI_df['log_diff'],
    'card_use_general_log_diff': card_use_general['log_diff'],
    'card_use_installment_log_diff': card_use_installment['log_diff'],
    'CSI_curr_living_log_diff': CSI_curr_living['log_diff']
})
df = df.dropna()
df
