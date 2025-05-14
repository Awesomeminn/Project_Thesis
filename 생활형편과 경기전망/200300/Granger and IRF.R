# 데이터 불러오기
data <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/생활형편과 경기전망/200300/200_300_6var.csv")
data
#========================================================================================================#
# 초기 패키지 설치
install.packages("vars")
install.packages("lmtest")
library(vars)
library(lmtest)
#==========================================================================================================#
# 자료형 변경 
data$Date <- as.Date(data$Date)
#==========================================================================================================#
# 수준변수 간 그레인저 인과관계 분석
## 두 변수만 추출
df_level <- data[, c("econ", "living")]
## 시차 수는 수동으로 설정해서 계속 해보기
p <- 1
## VAR 모형 적합
var_model <- VAR(df_level, p = p, type = "const")
## 양 방향 그레인저 인과검정 수행
grangertest(econ ~ living, order=p, data=df_level)
grangertest(living ~ econ, order=p, data=df_level)
#==========================================================================================================#
# 로그변수 간 그레인저 인과관계 분석
## 두 변수만 추출
df_log <- data[,c("econ_log", "living_log")]
## VAR 모형 적합
var_model <- VAR(df_log, p = p, type = "const")
## 양 방향 그레인저 인과검정 수행
grangertest(econ_log ~ living_log, order=p, data=df_log)
grangertest(living_log ~ econ_log, order=p, data=df_log)
#==========================================================================================================#
# 로그차분변수 간 그레인저 인과관계 분석
## 두 변수만 추출
df_lndiff <- na.omit(data[, c("econ_lndiff", "living_lndiff")])
## VAR 모형 적합
var_model <- VAR(df_lndiff, p = p, type = "const")
## 양 방향 그레인저 인과검정 수행
grangertest(econ_log ~ living_log, order=p, data=df_log)
grangertest(living_log ~ econ_log, order=p, data=df_log)
#==========================================================================================================#
# 충격반응함수 시각화 (먼저 위에서 시차랑 VAR모형 적합 시키고 실행해야함)
## 현재경기판단 충격에 대한 현재생활형편 반응
irf_result <- irf(var_model,
  impulse = "econ_lndiff",
  response = "living_lndiff",
  n.ahead = 12,     # 12개월까지 반응
  boot = TRUE,      # 부트스트랩 신뢰구간
  ci = 0.95)        # 95% 신뢰수준
plot(irf_result)
## 현재생활형편 충격에 대한 현재경기판단 반응
irf_result <- irf(var_model,
  impulse = "living_lndiff",
  response = "econ_lndiff",
  n.ahead = 12,     # 12개월까지 반응
  boot = TRUE,      # 부트스트랩 신뢰구간
  ci = 0.95)        # 95% 신뢰수준
plot(irf_result)
