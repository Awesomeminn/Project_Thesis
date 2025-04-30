# 모든 코드 맨 위에 이거 복붙하셈
import os 
os.getcwd()
os.chdir('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수와 거시변수/Model 1/Before COVID')
os.getcwd()
#=====================================================================================================#
#=====================================================================================================#
# 데이터 불러오고 패키지 임포트 
from Data_before_COVID import NSI_m, CCSI_m
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# 'Date' 칼럼 인덱스 설정
NSI_m.set_index('Date', inplace=True)
CCSI_m.set_index('Date', inplace=True)
# 시각화
plt.figure(figsize=(12, 6))
plt.plot(NSI_m.index, NSI_m['Value'], label='NSI', linewidth=2)
plt.plot(CCSI_m.index, CCSI_m['Value'], label='CCSI', linewidth=2)
plt.title('NSI and CCSI (2010-2019)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()