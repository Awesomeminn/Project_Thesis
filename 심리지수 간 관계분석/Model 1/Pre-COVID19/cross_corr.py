# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수 간 관계분석/Model 1/Pre-COVID19')
os.getcwd()
#=====================================================================================================#
# data.py에서 작업했던 거 가져오기
from data import NSI_m, CCSI_m, BSI_m, BSI_exp_m
#=====================================================================================================#
# 시각화
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 6))
plt.plot(NSI_m['Date'], NSI_m['Value'], label='NSI', linewidth=2)
plt.plot(CCSI_m['Date'], CCSI_m['Value'], label='CCSI', linewidth=2)
plt.plot(BSI_m['Date'], BSI_m['Value'], label='BSI', linewidth=2)
plt.plot(BSI_exp_m['Date'], BSI_exp_m['Value'], label='BSI_exp', linewidth=2)
plt.title('Sentiment Indices Over Time (2010-2019)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
