path = "C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/Exercises/심리지수 간 관계"
import os
os.chdir(path)
os.getcwd()
#=====================================================================================================#
from model1_precovid_ADF import merged_df
merged_df
#=====================================================================================================#
# 1. 최적시차선정
from statsmodels.tsa.api import VAR
data_for_var = merged_df.dropna()
data_for_var
model = VAR(data_for_var)
lag_order_results = model.select_order(maxlags=6)
print(lag_order_results.summary())
# 2. 그레인저 인과성 검정
from statsmodels.tsa.stattools import grangercausalitytests
data = merged_df.dropna()
model = VAR(data)
lag_selection = model.select_order(maxlags=6)
best_lag = lag_selection.aic
variables = data.columns.tolist()
for y in variables:
    for x in variables:
        if x != y:
            print(f'\n=== {x} Granger-causes {y}? (lag={best_lag}) ===')
            grangercausalitytests(data[[y, x]], maxlag=best_lag, verbose=True)
