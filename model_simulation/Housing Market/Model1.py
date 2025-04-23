# Model 1: 아파트매매 실거래 가격지수(전국), NSI, CCSI

# 패키지 임포트
import numpy as np
from statsmodels.tsa.stattools import adfuller

# 1. NSI_수준값에 대한 ADF 검정
result_level = adfuller(NSI_m['Value'], autolag='AIC')
print("== 수준값 (Level) ADF 검정 결과 ==")
print(f"ADF Statistic: {result_level[0]}")
print(f"p-value: {result_level[1]}")
print(f"# Lags Used: {result_level[2]}")
print(f"# Observations Used: {result_level[3]}")
for key, value in result_level[4].items():
    print(f"Critical Value ({key}): {value}")
print("=> 정체성 여부:", "정상 (Stationary)" if result_level[1] <= 0.05 else "비정상 (Non-stationary)")
print()

# 2. NSI_로그차분에 대한 ADF 검정
log_diff = np.log(NSI_m['Value']).diff().dropna()
result_logdiff = adfuller(log_diff, autolag='AIC')
print("== 로그차분 (Log Difference) ADF 검정 결과 ==")
print(f"ADF Statistic: {result_logdiff[0]}")
print(f"p-value: {result_logdiff[1]}")
print(f"# Lags Used: {result_logdiff[2]}")
print(f"# Observations Used: {result_logdiff[3]}")
for key, value in result_logdiff[4].items():
    print(f"Critical Value ({key}): {value}")
print("=> 정체성 여부:", "정상 (Stationary)" if result_logdiff[1] <= 0.05 else "비정상 (Non-stationary)")
