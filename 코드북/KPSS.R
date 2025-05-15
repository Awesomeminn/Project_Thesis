# 데이터 불러오기
data <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/생활형편과 경기전망/200300/200_300_6var.csv")
data

# 패키지 설치
install.packages("tseries")
library(tseries)

# KPSS 검정_생활형편CSI
## 수준_추세를 고려하지 않음
kpss.test(data$living, null = "Level")
## 수준_추세를 고려함
kpss.test(data$living, null = "Trend")
## 로그_추세를 고려하지 않음
kpss.test(data$living_log, null = "Level")
## 로그_추세를 고려함
kpss.test(data$living_lndiff, null = "Trend")
## 로그차분_추세를 고려하지 않음
kpss.test(data$living_lndiff, null = "Level")
## 로그차분_추세를 고려함
kpss.test(data$living_lndiff, null = "Trend")

# KPSS 검정_경기판단CSI
## 수준_추세를 고려하지 않음
kpss.test(data$econ, null = "Level")
## 수준_추세를 고려함
kpss.test(data$econ, null = "Trend")
## 로그_추세를 고려하지 않음
kpss.test(data$econ_log, null = "Level")
## 로그_추세를 고려함
kpss.test(data$econ_lndiff, null = "Trend")
## 로그차분_추세를 고려하지 않음
kpss.test(data$econ_lndiff, null = "Level")
## 로그차분_추세를 고려함
kpss.test(data$econ_lndiff, null = "Trend")
