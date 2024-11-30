# 1-1 
# 국어,수학,영어,과학 과목 중 가장 많은 학생들이 응시한 시험을 선택하고 해당과목의 점수를 표준화 했을 때 가장 큰 표준화 점수를 구하여라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p1.csv')
# print(df.head(5))
# print(df.describe())
# print(df.isna().sum())  #   국어를 가장 많이 응시

sub = df.iloc[:,1:].count().idxmax()
std = df[sub]

r = ((df[sub] - df[sub].mean()) / df[sub].std(ddof=0)).max()  # 모표준편차 ddof=0
# print(r)    # 1.713855688712825

# 1-2
# 32개의 변수간 상관관계를 확인 했을 때, var_11 컬럼과 상관계수의 절댓값이 가장 큰 변수를 찾아 해당 변수의 평균값을 구하여라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p2_.csv')
df.head(5)

max_v = df.corr()['var_11'].abs().sort_values().index[-2]
r = df[max_v].mean()
print(r)        # -0.06289356546077182

# 1-3
# var_6 컬럼의 1,3사분위수 각각 IQR의 1.5배 벗어난 이상치의 숫자를 구하라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p3.csv')
df.head(5)
q1 = df['var_6'].quantile(0.25)
q3 = df['var_6'].quantile(0.75)
iqr = q3-q1

min_ = q1 - 1.5 * iqr
max_ = q3 + 1.5 * iqr

r= df[(df['var_6'] <min_) | (df['var_6'] >max_)].shape[0]
print(r)    # 8







