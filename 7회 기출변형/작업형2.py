# 종속변수 :이용금액 , 평가지표 : rmse
import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p2_train2.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e7_p2_test2.csv')

print(train.head())
print(test.head())

x = train.drop(['ID', '이용금액'], axis=1)
test_x = test.drop(['ID'], axis=1)
y = train['이용금액']

data = pd.concat([x, test_x], axis=0)
data = pd.get_dummies(data)
x = data[:len(x)]
test_x = data[len(x):]

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=233)
model = RandomForestRegressor(random_state=98)
model.fit(x_train, y_train)

import numpy as np
y_pre = model.predict(x_val)
rmse = np.sqrt(mean_squared_error(y_val, y_pre))
print('rmse :', rmse)

y_predict = model.predict(test_x)
print(pd.DataFrame({'ID': test['ID'], '이용금액':y_predict}))
pd.DataFrame({'ID': test['ID'], '이용금액':y_predict}).to_csv('result.csv', index=False)