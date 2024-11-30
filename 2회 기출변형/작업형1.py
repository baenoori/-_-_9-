import pandas as pd
df = pd.read_csv('C:/Users/noori/Documents/빅분기/_data/2회 기출변형/Boston-house-price-data.csv')

# 1-1 
# 주어진 dataset 에서 CRIM 값이 가장 큰 10개의 지역을 구하고 
# 10개의 지역의 CRIM값을 그중 가장 작은 값으로 대체 
# AGE 컬럼값이 80이상인 대체된 CRIM 평균값

print(df.columns)
# Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
    #    'PTRATIO', 'B', 'LSTAT', 'MEDV']

print(df.head())
#       CRIM    ZN  INDUS  CHAS    NOX     RM   AGE     DIS  RAD    TAX  PTRATIO       B  LSTAT  MEDV
# 0  0.00632  18.0   2.31     0  0.538  6.575  65.2  4.0900    1  296.0     15.3  396.90   4.98  24.0
# 1  0.02731   0.0   7.07     0  0.469  6.421  78.9  4.9671    2  242.0     17.8  396.90   9.14  21.6
# 2  0.02729   0.0   7.07     0  0.469  7.185  61.1  4.9671    2  242.0     17.8  392.83   4.03  34.7
# 3  0.03237   0.0   2.18     0  0.458  6.998  45.8  6.0622    3  222.0     18.7  394.63   2.94  33.4
# 4  0.06905   0.0   2.18     0  0.458  7.147  54.2  6.0622    3  222.0     18.7  396.90   5.33  36.2
total_mean = df[df['AGE']>=80].CRIM.mean()
print(total_mean)

df = df.sort_values(by='CRIM', ascending=False).reset_index(drop=True)
print(df.head(10))

df.loc[:9,'CRIM'] = df.loc[9,'CRIM']
print(df)

total_mean1 = df[df['AGE']>=80].CRIM.mean()
print(total_mean1)
print("---------------------------")

# 1-2 
# 1-1에서 사용한 데이터에서 RM 중앙값으로 해당 컬럼의 결측치를 대체
# 해당 컬럼의 결측치 대치 전후의 표준편차 차이의 절대값을 소수점 이하 3쨰자리까지 구하기
first = df['RM'].std()
df['RM'] = df['RM'].fillna(df['RM'].median())
end = df['RM'].std()
results = abs(round(first-end,3))
print(results)

# 1-3 
# 주어진 Dataset의 DIS 평균으로부터 1.5*표준편차를 벗어나는 영역을 이상치라고 판단하고 DIS 컬럼의 이상치들의 합을 구하라
mean = df['DIS'].mean()
std = df['DIS'].std()
result = df[(df['DIS'] > mean + 1.5*std) | (df['DIS'] < mean - 1.5*std)].DIS.sum()
print(result)


