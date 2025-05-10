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
# 3. 충격반응함수
import matplotlib.pyplot as plt
irf = var_result.irf(10)
irf.plot(orth=False)
plt.tight_layout()
plt.show()
