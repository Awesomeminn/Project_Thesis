# 1. 데이터 불러오기
df <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/체감경기and소비/data/merge1.csv")
df
#============================================================================================#
# 2. 초기 패키지 설치
install.packages("vars")
install.packages("lmtest")
library(vars)
library(lmtest)
#============================================================================================#
# 3. 자료형 변경하기 및 VAR 모형 적합
df$date <- as.Date(df$date)
ts_df <- ts(df[, c("News", "curr_econ_CSI", "department_store")], start=c(2013, 2), frequency=12)
var_model <- VAR(ts_df, p=1, type="const")
#============================================================================================#
# 4. 최적시차 선택
lag_selection <- VARselect(ts_df, lag.max = 12, type = "const")
print(lag_selection)
#============================================================================================#
# 5. 그레인저 인과성 검정
grangertest(curr_econ_CSI ~ News, order=1, data=as.data.frame(ts_df))
grangertest(department_store ~ News, order=1, data=as.data.frame(ts_df))
grangertest(department_store ~ curr_econ_CSI, order=1, data=as.data.frame(ts_df))
grangertest(News ~ curr_econ_CSI, order=1, data=as.data.frame(ts_df))
grangertest(News ~ department_store, order=1, data=as.data.frame(ts_df))
grangertest(curr_econ_CSI ~ department_store, order=1, data=as.data.frame(ts_df))
#============================================================================================#
# 6. 충격반응함수
irf_result <- irf(var_model, impulse = NULL, response = NULL, n.ahead = 10, boot = TRUE, ci = 0.95)
plot(irf_result)
#============================================================================================#
# 7. FEVD
fevd_result <- fevd(var_model, n.ahead = 10)
print(fevd_result)
