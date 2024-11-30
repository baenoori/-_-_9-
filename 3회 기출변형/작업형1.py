# 1-1
# 결측치가 하나라도 존재하는 행의 경우 경우 해당 행을 삭제하라. 
# 그후 남은 데이터의 상위 70%에 해당하는 데이터만 남겨둔 후 median_income 컬럼의 1분위수를 반올림하여 소숫점이하 2째자리까지 구하여라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p1_1.csv')
# print(df.head(5))
# print(df.isna().sum())
df = df.dropna()
# print(df.isna().sum())
df = df.iloc[:int(len(df)*0.7)]
ans = round(df['median_income'].quantile(0.25), 2)
print(ans)      # 2.51

# 1-2 
# 1990년도는 해당년도 평균 이하 GDP를 가지지만, 2010년도에는 해당년도 평균 이상 GDP를 가지는 국가의 숫자를 구하여라

import pandas as pd
df =pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p1_2.csv')
# print(df.head())
# print(df['Value'].isna().sum())   0
df_1990 = df[df.Year ==1990]
df_2010 = df[df.Year ==2010]


df_1990_filter = df_1990[df_1990.Value <= df_1990.Value.mean()]
df_2010_filter = df_2010[df_2010.Value >= df_2010.Value.mean()]

result = len(set(df_2010_filter['Country Code']) & set(df_1990_filter['Country Code']))
print(result)


# 1-3
# 데이터에서 결측치가 가장 많은 컬럼을 출력하라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p1_3.csv')
df.head()
ans = df.isna().sum()
print(type(ans))
print('Fare')

result = df.isnull().sum().sort_values().index[-1]
print(result)


