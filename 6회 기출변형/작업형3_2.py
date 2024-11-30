import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/adp/28/p7.csv')
print(df.head())

# 3-2-a 
# age와 Cholesterol을 가지고 weight를 예측하는 선형 회귀 모델을 만들려고한다. age의 회귀 계수를 구하여라

import statsmodels.api as sm
X = sm.add_constant(df[['age', 'Cholesterol']]) 
model = sm.OLS(df['weight'], X)
results = model.fit()

print(results.params['age'])    # -0.0361016691438651


# 3-2-b
# age가 고정일 때 Cholesterol와 weight가 선형관계에 있다는 가설을 유의수준 0.05하에 검정하라
H = results.pvalues['Cholesterol']
if H <0.05 : 
    print('선형 관계에 있다.')
else:
    print('선형 관계에 없다.')


# 3-2-c
# age가 55, Cholesterol가 72.6일때 위 모델을 기반으로 weight값을 예측하라.
pred = results.predict([1,55,72.6]) # const , age,Cholesterol
print(pred[0])
    