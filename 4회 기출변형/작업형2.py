# 예측 변수 Segmentation, test.csv에 대해 ID별로 Segmentation의 클래스를 예측해서 저장후 제출, 
# 제출 데이터 컬럼은 ID와 Segmentation 두개만 존재해야함. 평가지표는 macro f1 score

import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p2_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p2_test.csv')

# print(test.head(2))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import lightgbm as lgb
from sklearn.metrics import f1_score

print(train.head(2))
print(train.isna().sum())

train.fillna(0)

x = train.drop(['ID', 'Segmentation'], axis=1)
test_x = test.drop(['ID'], axis=1)
y = train['Segmentation']

data = pd.concat([x, test_x], axis=0)
data = pd.get_dummies(data)

x = data[:len(x)]
test_x = data[len(x):]

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=77)

model = RandomForestClassifier(random_state=222)
model.fit(x_train, y_train)

y_pre = model.predict(x_val)
print('test f1_score', f1_score(y_val, y_pre, average='macro'))

y_predict = model.predict(test_x)
print(y_predict)

pd.DataFrame({'ID':test['ID'], 'Segmentation':y_predict}).to_csv('result.csv', index=False)

