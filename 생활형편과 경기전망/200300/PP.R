# 데이터 불러오기
data <- read.csv("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/생활형편과 경기전망/200300/200_300_6var.csv")
data

# 패키지 설치
install.packages("stats")
library(stats)

# PP 검정: 생활형편CSI
pp.test(data$econ) 
pp.test(data$living) 
pp.test(data$econ_log)
pp.test(na.omit(data$econ_lndiff))
pp.test(data$living_log)
pp.test(na.omit(data$living_lndiff))
