# 다이어트약의 전후 체중 변화 기록이다. 
# 투약 후 체중에서 투약 전 체중을 뺏을 때 값은 일반 적으로 세가지 등급으로 나눈다. 
# -3이하 : A등급, -3초과 0이하 : B등급, 0 초과 : C등급. 약 실험에서 A,B,C 그룹간의 인원 수 비율은 2:1:1로 알려져 있다. 
# 위 데이터 표본은 각 범주의 비율에 적합한지 카이제곱 검정하려한다.

import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p3_1.csv')
df.head()

# 3-1-a
# A등급에 해당하는 유저는 몇명인지 확인하라
df['dels'] = df['투약후'] - df['투약전']

def groupby_filter(x):
    if x <=-3:
        return 'A'
    elif x <=0:
        return 'B'
    else:
        return 'C'
    
df['groupby'] = df['dels'].apply(groupby_filter)
result = df['groupby'].value_counts().sort_index()['A']
print(result)       # 121

# 3-1-b
# 카이제곱검정 통계량을 반올림하여 소숫점 이하 3째자리까지 구하여라

target = df['groupby'].value_counts().sort_index().to_frame()
target['expected'] = [target['groupby'].sum()*0.5,target['groupby'].sum()*0.25,target['groupby'].sum()*0.25]

from scipy.stats import chisquare
s,p = chisquare(target['groupby'],target['expected'])

round_s = round(s,3)
print(round_s)

# 3-1-c
# 카이제곱 검정 p값을 반올림하여 소숫점 이하 3자리까지 구하고, 유의수준 0.05하에서 귀무가설과 대립가설중 유의한 가설을 하나를 선택하시오(귀무/대립)
round_p = round(p,3)
print(round_p)
print('귀무')


