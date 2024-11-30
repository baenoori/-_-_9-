# 예측 변수 General_Health, test.csv에 대해 ID별로 General_Health 값을 예측하여 제출,
# 제출 데이터 컬럼은 ID와 General_Health 두개만 존재해야함. 평가지표는 f1score

import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/ep6_p2_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/ep6_p2_test.csv')

print(train.head(2))
print(test.head(2))
print(train.info())
print(train.isna().sum())

x = train.drop(['ID','General_Health'], axis=1)
test_x = test.drop(['ID'], axis=1)
y = train['General_Health']
data = pd.concat([x, test_x], axis=0)
data = pd.get_dummies(data)
x = data[:len(x)]
test_x = data[len(x):]

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=333)

model = RandomForestClassifier(random_state=444)
model.fit(x_train, y_train)

y_pre = model.predict(x_val)
print('f1_score :', f1_score(y_val, y_pre, average='macro'))

y_predict = model.predict(test_x)
print(y_predict)
print(pd.DataFrame({'ID':test['ID'], 'General_Health':y_predict}))
pd.DataFrame({'ID':test['ID'], 'General_Health':y_predict}).to_csv('result.csv', index=False)
