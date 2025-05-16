# 데이터 불러오기
data <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/연습장/소비지출전망/model1/data2.csv")
data
#========================================================================================================#
# 초기 패키지 설치
install.packages("vars")
install.packages("lmtest")
library(vars)
library(lmtest)
#==========================================================================================================#
df<- na.omit(data[, c("durable_consume_exp_CSI_lndiff", "import_car_sell_lndiff")])
p <- 1
var_model <- VAR(df, p = p, type = "const")
grangertest(import_car_sell_lndiff ~ durable_consume_exp_CSI_lndiff, order=p, data=df)
grangertest(durable_consume_exp_CSI_lndiff ~ import_car_sell_lndiff, order=p, data=df)
