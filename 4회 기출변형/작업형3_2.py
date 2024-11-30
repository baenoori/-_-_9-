# 어느 학교에서 수학 시험을 본 학생 100명 중 60명이 60점 이상을 받았다.
# 이 학교의 수학 시험의 평균 점수가 50점 이상인지 95%의 신뢰 수준에서 검정하려한다


# 3-2-a 
# 검정 통계량을 소숫점 이하 3자리에서 구하시오
import numpy as np
n = 100
p_hat = 0.6
p = 0.5
alpha = 0.05

# 검정 통계량 계산
z = round((p_hat - p) / np.sqrt(p * (1 - p) / n),5)
print(z)    # 2.0


# 3-2-b
# pvalue를 소숫점 이하 3자리까지 구하고 귀무가설과 대립가설중 유의한 것을 출력하라
from scipy.stats import norm
p_value = round(1 - norm.cdf(z),3)      # 0.023

print(p_value)
print('대립')

    