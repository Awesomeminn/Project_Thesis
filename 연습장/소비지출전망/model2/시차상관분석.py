# 0. 데이터 불러오기
import pandas as pd
df = pd.read_csv('C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model2/data2.csv')
df
#=====================================================================================================#
# 시차 상관분석 실시
## 분석에 사용할 변수 설정
x = df['curr_living_CSI_lndiff']       
y_candidates = [col for col in df.columns if col != 'curr_living_CSI_lndiff'] 
## 시차 범위 설정
lags = range(-6, 7)
result = {}
for y_name in y_candidates:
    y = df[y_name]
    correlations = []
    for lag in lags:
        y_lagged = y.shift(lag)
        # 결측치 제거 후 상관계수 계산
        valid_idx = x.notna() & y_lagged.notna()
        corr = x[valid_idx].corr(y_lagged[valid_idx])
        correlations.append(round(corr, 3) if pd.notna(corr) else None)
    result[y_name] = correlations
lag_labels = [f"t{l:+}" for l in lags]
corr_df = pd.DataFrame(result, index=lag_labels).T
corr_df
