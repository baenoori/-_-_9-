# 종속 변수 : TravelInsurance , TravelInsurance가 1일 확률을 구해서 제출하라. 평가지표 : auc
# 제출 파일의 컬럼은 ID, proba 두개만 존재해야한다.

import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p2_train_.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p2_test_.csv')
print(train.head())

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

# print(train.isna().sum())
# print(test.isna().sum())

x = train.drop(['ID', 'TravelInsurance'], axis=1)
test_x = test.drop(['ID'], axis=1)
y = train['TravelInsurance']

data = pd.concat([x, test_x], axis=0)
data = pd.get_dummies(data)
x = data[:len(x)]
test_x = data[len(x):]

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=777)

model = RandomForestClassifier(random_state=444)
model.fit(x_train, y_train)

y_preba = model.predict_proba(x_val)[:,1]
print('test auc', roc_auc_score(y_val, y_preba))

y_predict_proba = model.predict_proba(test_x)[:,1]

pd.DataFrame({'ID': test['ID'], 'proba':y_predict_proba}).to_csv('result.csv', index=False)