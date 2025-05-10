# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/소비_model2')
os.getcwd()
#======================================================================================================#
# 1. merge 가져오기
from Data_Integration import merge
#======================================================================================================#
# 2. VAR 모델적합
from statsmodels.tsa.api import VAR
model = VAR(merge)
var_result = model.fit(1)  
#======================================================================================================#
# 3. 분산분해
fevd = var_result.fevd(10)
#======================================================================================================#
# 4. 분산분해 행렬
fevd.plot()
#======================================================================================================#
import pandas as pd

horizon = 3  # 가능한 최대 horizon
target_var = 'CPI_durable_log_diff'
target_idx = merge.columns.get_loc(target_var)

# 분산기여율 추출
contrib = fevd.decomp[horizon, target_idx, :] * 100  # 백분율로 변환

# DataFrame 생성
fevd_table = pd.DataFrame({
    'Shock from': merge.columns,
    f'Contribution to {target_var} at t+{horizon} (%)': contrib
})
print(fevd_table.round(2))
