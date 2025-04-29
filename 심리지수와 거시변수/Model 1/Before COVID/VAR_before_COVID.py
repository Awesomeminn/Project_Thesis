# 분석을 위해 기존에 작업한 파일에서 데이터 불러오기
from Data_before_COVID import NSI, CCSI 
# 필요한 라이브러리 설치
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import grangercausalitytests
# Date 타입 맞추고 인덱스 설정
NSI['Date'] = pd.to_datetime(NSI['Date'])
CCSI['Date'] = pd.to_datetime(CCSI['Date'])
NSI.set_index('Date', inplace=True)
CCSI.set_index('Date', inplace=True)
# 두 데이터프레임 합치기 (같은 기간 기준)
data = pd.concat([NSI['Value'], CCSI['Value']], axis=1)
data.columns = ['NSI', 'CCSI']
# VAR 모델 적합 및 적정 시차 선택
model = VAR(data)
lag_selection = model.select_order(12)
print(lag_selection.summary())
optimal_lag = lag_selection.aic
# VAR 모형 재적합
var_result = model.fit(optimal_lag)
print(var_result.summary())
# Granger Causality Test
maxlag = optimal_lag
def granger_test_table(data, cause, effect, maxlag):
    """
    cause → effect 방향의 Granger causality 검정을 수행하고
    lag별 p-value를 테이블로 반환
    """
    test_result = grangercausalitytests(data[[effect, cause]], maxlag=maxlag, verbose=False)
    
    p_values = []
    for lag in range(1, maxlag + 1):
        p_val = test_result[lag][0]['ssr_ftest'][1]
        p_values.append({'Lag': lag, 'p-value': round(p_val, 4)})
    
    return pd.DataFrame(p_values)
print('▶ NSI → CCSI')
df1 = granger_test_table(data, cause='NSI', effect='CCSI', maxlag=optimal_lag)
print(df1)
print('▶ CCSI → NSI')
df2 = granger_test_table(data, cause='CCSI', effect='NSI', maxlag=optimal_lag)
print(df2)
