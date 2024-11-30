import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p3_1.csv')
print(df)

# 3-1-a
# 55명 학생들의 키에 대한 표본 평균을 구하여라(반올림하여 소숫점 3째자리까지
mean = df['height'].mean()
print(round(mean,3))    # 169.937

# 3-1-b
# t분포 양쪽 꼬리에서의 t 값을 구하여라 (반올림하여 소수4째자리까지)
import numpy as np
from scipy.stats import t

std = np.std(df.height, ddof=1)
n = len(df.height)

# 신뢰수준, 자유도
confidence_level = 0.95
ddof = n - 1

# t 분포의 양쪽 꼬리에서의 t값
t_value = round(t.ppf((1 + confidence_level) / 2, ddof),4)
print(t_value)

# 3-1-c
# 95% 신뢰구간을 구하여라(print(lower,upper) 방식으로 출력, 각각의 값은 소숫점 이하 3째자리까지)
# 신뢰구간 계산
lower = round(mean - t_value * std / np.sqrt(n),3)
upper = round(mean + t_value * std / np.sqrt(n),3)
print(lower,upper)

