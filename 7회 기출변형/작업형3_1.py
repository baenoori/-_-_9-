import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p3_1.csv')
print(df.head())

# 3-1 
# 선형관계 가장 큰 변수를 찾아 상관계수 구하기
print(df.corr()['Target'].sort_values()[-2])    # 0.6270251925517436

# 3-2
# Target 변수를 종속변수로 하여 다중선형회귀모델링을 진행했을 때 v2 컬럼의 회귀 계수는?
import numpy as np
import pandas as pd
import statsmodels.api as sm

X = df.drop('Target', axis=1)
X = sm.add_constant(X)  # 상수항 추가
y = df['Target']

model = sm.OLS(y, X).fit()
print(model.params['v2'])

# 3-3
# 회귀 계수들이 가지는 p값들 중 최대 값은?
print(model.pvalues.max())  # 0.9265545986907169
