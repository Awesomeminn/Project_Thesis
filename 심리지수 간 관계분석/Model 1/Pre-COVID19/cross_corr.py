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
#=====================================================================================================#
# 패키지 임포트
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import ccf
import itertools
#=====================================================================================================#
# ---- [전처리: Date 기준 병합] ----
merged = NSI_m.rename(columns={'Value': 'NSI'}).merge(
    CCSI_m.rename(columns={'Value': 'CCSI'}), on='Date'
).merge(
    BSI_m.rename(columns={'Value': 'BSI'}), on='Date'
).merge(
    BSI_exp_m.rename(columns={'Value': 'BSI_exp'}), on='Date'
)
merged
#=====================================================================================================#
# ---- [교차상관 계산] ----
columns = ['NSI', 'CCSI', 'BSI', 'BSI_exp']
max_lag = 12
cross_corr_results = {}

for x, y in itertools.permutations(columns, 2):  # 순서 있는 쌍 (NSI → CCSI 등)
    series_x = merged[x] - merged[x].mean()
    series_y = merged[y] - merged[y].mean()
    corr_vals = ccf(series_x, series_y)[:max_lag+1]
    cross_corr_results[f'{x} → {y}'] = corr_vals

# ---- [결과 정리] ----
cross_corr_df = pd.DataFrame(cross_corr_results)
cross_corr_df['Lag'] = range(0, max_lag+1)
cross_corr_df.set_index('Lag', inplace=True)

# ---- [결과 출력] ----
print(cross_corr_df)

# 최대 상관계수 및 해당 lag을 딕셔너리로 정리
max_corr_info = {
    col: (cross_corr_df[col].max(), cross_corr_df[col].idxmax())
    for col in cross_corr_df.columns
}

# 정리된 결과를 보기 좋게 데이터프레임으로
max_corr_df = pd.DataFrame(max_corr_info, index=['Max Corr', 'At Lag']).T
print(max_corr_df.sort_values(by='Max Corr', ascending=False))
