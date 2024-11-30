# 0. 습관처럼
import pandas as pd
import numpy as np
df = pd.read_csv(path)
print(df.shape())
print(df.isnull().sum())
df.head()

# 1. 이상치 => "quantile"
q1 = df[col].quantile(0.25) # 1사분위 값
q3 = df[col].quantile(0.75) # 3사분위 값
iqr = q3 - q1
v1 = q1 - 1.5 * iqr
v3 = q3 + 1.5 * iqr

# 2. 반올림 / 올림 / 버림
## 2-1. 데이터프레임으로 받는경우 (넘파이 필수)
c = np.ceil(df)
f = np.floor(df) # 내림 -5.5 => -6
t = np.trunc(df) # 버림(절삭) -5.5 => -5
r = np.round(df,자릿수)
r_mean = r.mean() # 이런식으로 array, df는 끝에 '.함수()' 가 많음.
## 2-2. 그냥
import math
math.round(value, 자릿수)

# 3. 값 삭제 => 특정 행/열 drop, 결측치 포함 행/열 drop'na' *loc,iloc 쓸수있으면 쓰는게 젤 낫다
df = df.drop('지울칼럼명', axis = 1) # axis = 1 해줘야함.'1' 세로방향 모양
df = df.drop('지울행 인덱스값 : 행이름이 없으니') # 디폴트가 axis = 0
df = df.dropna() # 결측치 하나라도 있는 행 다 삭제

# 4. 결측치채우기 => df[열].fillna(값)
df['col'] = df['col'].fillna(df['col'].median()) # 중앙값으로 결측치 다 채우는경우
# 이게 이런걸 주의해야함 drop이랑 비슷한건데 1) df['f1'].fillna(variance)라고 해서 반영되지 않음 저거 자체의 결과값은 데이터프레임에 바로 반영이 아니라 값 자체같은거임
# 2) df = df['f1'].fillna(variance) 이것도 잘못된거지 값 자체를 전체 데이터프레임으로 대입하려 했으니까
# 3) ★ df['f1'] = df['f1'].fillna(median_num) 이렇게해줘야 반영이됨!! 즉 pandas에서 잘 안되는거있으면 이런식의 사고를 해보기 ★

# 5. 왜도와첨도
v1 = df['col'].skew()
v2 = df['col'].kurt()

# 6. df1의 누적합 df2 구하기 => cumsum()
df2 = df1.cumsum()
df2 = df2.fillna(method = 'bfill') # 이 때 발생하는 결측치를 뒤의 값 채우기
df2 = df2.fillna(method = 'ffill') # 앞의값으로

# 7. 표준화 => 암기 ★sklearn ~ StandardScaler ~ fit_transform★
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['col'] = scaler.fit_transform(df[['col]]) # df['f5'] 이렇게하면 오류남!!! 인자를 시리즈가 아닌 데이터프레임으로 받아야하기 떄문!!
df.head()
'''
* 기본 외워야함 : from sklearn.preprocessing import StandardScaler, scaler(), fit_transform
* fit_transform은 인자를 series가 아닌 dataframe으로 받는다
* 가장 쉬운거는 []말고 [[]]로 하면 dataframe이 된다!
* seires, dataframe 차이 : series는 dataframe의 구성요소로 열 한개임. df도 열이 한개일 수는 있지만 series는 무조건 한개겠지
위에처럼 그냥 []하면 series로 나오고 [[]]로 하면 df로 나옴..!!
'''

# 8. 특정 칼럼 기준 데이터프레임 정렬하기
df = df.sort_values('col', ascending=False) # 내림차순
df.head()

# 8-2. 특정 칼럼의 개수(빈도) 세기
df[col].value_counts() # type이 series임!

# 9. 표준편차 => .std()
# 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
# 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
std = df['age'].std()*1.5
mean = df['age'].mean()

option = (df['age'] > mean + std) | (df['age'] < mean - std) 
df.loc[option]['age'].sum()
'''
암기 : .sum(), std(), mean(), max(), min()
특이사항 : 전부 다 df.~~ 이다 평균이든 칼럼삭제든 정렬이든 전부!!!
'''

# 10. 시계열 datetime (시계열 나오면 먼저 바꾸고 시작 일단 바꾸고!)
'''
- 문자열로 접근해도 되지만 datetime 쓰는게 훨씬 정신건강에 낫다!
- df[col] = pd.to_datetime(df[col]) 이 시작! df[col] = df[col].to_datetime 아님! 이것만 조금 다르단거 꼭 암기!
'''
# 날짜가 2018년 1월인 데이터 개수 구하기
df['date_added'] = pd.to_datetime(df['date_added']) # "September 25, 2021" 이런걸 인식해서 "2021-09-25" 이렇게 바꿔주는거임
con1 = (df['date_added'].dt.year == 2018) # 주의1) df[col].year이 아니라 df[col].dt.year이다!! 
con2 = (df['date_added'].dt.month == 1) # 주의2) '2018'이 아니라 2018임!
# 아래처럼 연산하듯이 비교도 가능 이럴땐 dt.year이런걸 안쓰는거고 문자열로 감싸줘야
cond2 = df['date_added'] >= '2018-1-1'
cond3 = df['date_added'] <= '2018-1-31'
len(df.loc[con1&con2])