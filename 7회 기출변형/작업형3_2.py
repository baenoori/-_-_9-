#  train 데이터는 앞의 210개 행을, test데이터는 나머지 부분을 사용한다
import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p3_t.csv')
df.head()

# 3-4
# train 데이터로 target을 종속변수로 로지스틱 회귀를 진행할 때 age 컬럼의 오즈비를 구하여라
import pandas as pd
import numpy as np
import statsmodels.api as sm

train = df.iloc[:210].reset_index(drop=True)
test = df.iloc[210:].reset_index(drop=True)

# 종속변수와 독립변수 설정
X = train.drop('target', axis=1)
y = train['target']

# 로지스틱 회귀모형 적합
model = sm.Logit(y, X).fit()

# age의 weight 오즈비 계산
odds_ratios = np.exp(model.params['age'])
print(odds_ratios)  # 0.9562078844664191



# 3-5
# train으로 로지스틱 회귀 진행했을 경우 잔차 이탈도 (residual deviance)를 계산하라
# 로지스틱 회귀모형 적합 (GLM 사용) -> 이항분포시 로지스틱회귀
model2 = sm.GLM(y, X, family=sm.families.Binomial()).fit()

# 잔차 이탈도(residual deviance) 계산
residual_deviance = model2.deviance
print(residual_deviance)     # 144.205620063278

# 3-6
# test 데이터의 독립변수로 target 예측 후 오류율을 구하여라
pred = (model.predict(test.drop(columns=['target'])) >0.5).astype('int')

from sklearn.metrics import accuracy_score

error_rate = 1- accuracy_score(test['target'],pred)
print(error_rate)   # 0.1954022988505747

