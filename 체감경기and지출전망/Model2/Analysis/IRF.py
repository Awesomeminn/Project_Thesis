# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/Analysis')
os.getcwd()
#======================================================================================================#
# 데이터 가져오기
from VAR import df
df
#======================================================================================================#
# VAR modeling
from statsmodels.tsa.api import VAR
model = VAR(df)
results = model.fit(maxlags=12, ic='bic')
print("선택된 최적 시차 (BIC 기준):", results.k_ar)
#======================================================================================================#
# IRF
import matplotlib.pyplot as plt
irf = results.irf(10)
irf.plot(orth=False)  # orth=True는 직교화된 충격
plt.tight_layout()
plt.show()
