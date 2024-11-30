# 예측 변수 price, test.csv에 대해 ID별로 price 값을 예측하여 제출, 
# 제출 데이터 컬럼은 ID와 price 두개만 존재해야함. 평가지표는 rmse
import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_train_.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p2_test_.csv')

print(train.head(5))
print(test.head(5))

x = train.drop(['ID','price'], axis=1)
y = train['price']
test_x = test.drop(['ID'], axis=1)

print(x.isna().sum())
print(x.info())
print(x.head())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error

data = pd.concat([x, test_x], axis=0)
data = pd.get_dummies(data)
x = data[:len(x)]
test_x = data[len(x):]

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=111)

model = RandomForestClassifier(random_state=22)
model.fit(x_train, y_train)

import numpy as np
y_pre = model.predict(x_val)
rmse = np.sqrt(mean_squared_error(y_val, y_pre))
print('test_rmse :', rmse)

y_predict = model.predict(test_x)
pd.DataFrame({'ID' : test['ID'], 'price':y_predict}).to_csv('result.csv', index=False)

