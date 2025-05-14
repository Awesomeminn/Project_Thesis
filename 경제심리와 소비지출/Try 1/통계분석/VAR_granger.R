# 1. 데이터 불러오기
df <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/경제심리와 소비지출/Try 1/data and ADF/merge.csv")
df
#============================================================================================#
# 2. 초기 패키지 설치
install.packages("vars")
install.packages("lmtest")
library(vars)
library(lmtest)
#============================================================================================#
# 3. 자료형 변경하기 및 VAR 모형 적합
df$date <- as.Date(df$Date)
ts_df <- ts(df[, c("News", "curr_living_CSI", "department_store", "mart", "supermarket")], start=c(2013, 2), frequency=12)
var_model <- VAR(ts_df, p=2, type="const")
#============================================================================================#
# 4. 그레인저 인과성 검정
grangertest(curr_living_CSI ~ News, order=2, data=as.data.frame(ts_df))
grangertest(supermarket ~ News, order=2, data=as.data.frame(ts_df))
grangertest(department_store ~ News, order=2, data=as.data.frame(ts_df))
grangertest(mart ~ News, order=2, data=as.data.frame(ts_df))

grangertest(supermarket ~ curr_living_CSI, order=2, data=as.data.frame(ts_df))
grangertest(department_store ~ curr_living_CSI, order=2, data=as.data.frame(ts_df))
grangertest(News ~ curr_living_CSI, order=2, data=as.data.frame(ts_df))
grangertest(mart ~ curr_living_CSI, order=2, data=as.data.frame(ts_df))

grangertest(News ~ supermarket, order=2, data=as.data.frame(ts_df))
grangertest(curr_living_CSI ~ supermarket, order=2, data=as.data.frame(ts_df))
grangertest(department_store ~ supermarket, order=2, data=as.data.frame(ts_df))
grangertest(mart ~ supermarket, order=2, data=as.data.frame(ts_df))

grangertest(News ~ department_store, order=2, data=as.data.frame(ts_df))
grangertest(curr_living_CSI ~ department_store, order=2, data=as.data.frame(ts_df))
grangertest(supermarket ~ department_store, order=2, data=as.data.frame(ts_df))
grangertest(mart ~ department_store, order=2, data=as.data.frame(ts_df))

grangertest(News ~ mart, order=2, data=as.data.frame(ts_df))
grangertest(curr_living_CSI ~ mart, order=2, data=as.data.frame(ts_df))
grangertest(supermarket ~ mart, order=2, data=as.data.frame(ts_df))
grangertest(department_store ~ mart, order=2, data=as.data.frame(ts_df))
#============================================================================================#