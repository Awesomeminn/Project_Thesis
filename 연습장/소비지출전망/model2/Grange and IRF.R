# 데이터 불러오기
data <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model2/data2.csv")
data
#========================================================================================================#
# 초기 패키지 설치
install.packages("vars")
install.packages("lmtest")
library(vars)
library(lmtest)
#==========================================================================================================#
# VAR 모형 적합
df<- na.omit(data[, c("curr_living_CSI_lndiff", "Trading_Volume_KOSPI_lndiff", "Trading_Volume_KOSDAQ_lndiff")])
p <- 1
var_model <- VAR(df, p = p, type = "const")
#==========================================================================================================#
# 그레인저 인과성 검정 수행
grangertest(Trading_Volume_KOSPI_lndiff ~ curr_living_CSI_lndiff, order=p, data=df)