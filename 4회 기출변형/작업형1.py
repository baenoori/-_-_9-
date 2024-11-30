# 1-1
# Temperature컬럼에서 숫자가 아닌 문자들을 제거후 숫자 타입으로 바꾸고 3분위수에서 1분위수의 차이를 소숫점 이하 2자리까지 구하여라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_1.csv')
# print(df.head(5))
# print(df.info())

df['Temperature'] = df['Temperature'].str.replace('*','').astype(float)
a = df['Temperature'].quantile(0.75)
b = df['Temperature'].quantile(0.25)

print(round(a-b, 2))    # 27.48


# 1-2 
# Likes를 Comments로 나눈 비율이 20이상이면서 Keyword값이 minecraft인 영상들의 Views값의 평균을 정수로 구하여라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_2.csv')
print(df.head(5))

cond1 = df['Likes'] / df['Comments'] >= 20
cond2 = df['Keyword'] == 'minecraft'
ans = int(df[cond1 & cond2]['Views'].mean())
print(ans)  # 1789084


# 1-3
# date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e4_p1_3.csv')
print(df.head(5))
print(df['date_added'])
print(df['country'])
cond1 = (df['date_added'].str.contains('2018')) & (df['date_added'].str.contains('January'))
cond2 = df['country'] == 'United Kingdom'
ans = len(df[cond1 & cond2])
print(ans)      # 6