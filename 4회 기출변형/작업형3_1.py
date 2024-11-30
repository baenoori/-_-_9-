# 이 데이터를 바탕으로, 학생들의 학과와 성별이 서로 독립적인지 여부를 확인하기 위해 카이제곱 독립성 검정을 실시

import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p3_1_.csv')
print(df.head())

# 3-1-a 
# 학과 평균 인원에 대한 값을 소숫점 이하 3자리까지 구하여라
data = df.groupby('학과').nunique()
print(round(data['학번'].mean(),3))     # 170.333

# 3-1-b
# 카이제곱검정 독립성 검정 통계량을 소숫점 이하 3자리까지 구하여라
from scipy.stats import chi2_contingency
data = pd.crosstab(df['학과'], df['성별'])
result = chi2_contingency(data)
print(result)
print(result[0])
print(round(result[0], 3))      # 5.646

# 3-1-c
# 카이제곱검정 독립성 검정의 pvalue를 소숫점 이하 3자리까지 구하여라. 유의수준 0.05하에서 귀무가설과 대립가설중 유의한 것을 출력하라
from scipy.stats import chi2_contingency
data = pd.crosstab(df['학과'], df['성별'])
result = chi2_contingency(data)
print(result)
print(result[1])
print(round(result[1],3))   # 0.342
print('귀무')           # 귀무
