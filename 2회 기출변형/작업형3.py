import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e2_p3_1.csv')

# 3-1-a
# 122마리의 height 평균값을 m(미터) 단위로 소숫점 이하 5자리까지 실수 값만 출력하라
ans = round(df['height'].str.replace('cm','').astype(float).mean()/100, 5)
print(ans)


# 3-1-b
# 모집단의 평균 길이가 30cm 인지 확인하려 일표본 t 검정을 시행하여 확인하려한다. 검정통계량을 소숫점 이하 3째자리까지 구하여라
from scipy.stats import ttest_1samp

s ,p = ttest_1samp(df['height_raw'],30)
result = round(s,3)
print(result)


# 3-1-c
# 위의 통계량에 대한 p-값을 구하고 (반올림하여 소숫점 이하 3째자리), 유의수준 0.05하에서
# 귀무가설과 대립가설중 유의한 가설을 하나를 선택하시오(귀무/대립)
p_result =round(p,3)
result = '귀무'
print(p_result)
print(result)


# 3-2-a
# 21명 중 16명 미만이 치과를 찾았을 확률(반올림하여 소숫점 이하 3자리)
from scipy.stats import binom

n = 21
p = 0.7
k = 16

# P(X < k) 계산
prob = binom.cdf(k-1, n, p)
print(round(prob, 3))


# 3-2-b
# 적어도 19명이 치과를 찾았을 확률(반올림하여 소숫점 이하 3자리)
from scipy.stats import binom

n = 21
p = 0.7
k = 19

# P(X >= k) 계산
prob = 1 - binom.cdf(k-1, n, p)
print(round(prob, 3))


