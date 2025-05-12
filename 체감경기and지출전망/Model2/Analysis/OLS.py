# 1. 데이터 불러오기
import pandas as pd
df = pd.read_csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and지출전망/Model2/data/merge.csv")
df
# 2. 회귀분석 필요한 패키지 임포트
from statsmodels.formula.api import ols
# 3. 내구재 지출전망을 종속변수로 OLS로 회귀분석 실시
model = ols(formula = 'durable_consume_exp_CSI ~ News + curr_econ_CSI',data = df).fit()
print(model.summary())
# 4. 외식비 지출전망을 종속변수로 OLS 회귀분석 실시
model = ols(formula = 'eatout_consume_exp_CSI ~ News + curr_econ_CSI',data = df).fit()
print(model.summary())
