# 내가 오해했던 것: cd코드는 change directory를 의미하는거지 current directory가 아님

# 자 그러면 경로를 바꾸기 위해서는 어떻게 해야 하는가?
import os ## os package 설치
os.getcwd() ## 지금 작업경로 뱉는 코드임
os.chdir("C:/Users/Awesomemin/Desktop/연구아카이브/Project_Thesis/심리지수와 거시변수/Model 1/Before COVID")
## 위에 처럼 괄호 안에 경로 넣으면 됨
os.getcwd() ## getcwd() 메서드 다시 입력해서 잘 변경되었는지 check하기

# 모든 코드 맨 위에 이거 복붙하셈
import os 
## os.chdir('경로는 상황에 따라 맞춰서 쓰셈')
os.getcwd()
#======================================================================================================#
