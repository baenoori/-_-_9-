# 1-1 
# 20L가격과 5L가격이 모두 0원이 아닌 데이터만 필터를 한 후, 각 row별로 20L가격과 5L가격의 차이를 ‘차이가격’ 이라 부른다고 하자. 
# 시도명 별 차이가격의 평균가격을 비교할때 그 값이 가장 큰 금액을 반올림하여 소숫점 이하 1자리까지 구하여라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_1_.csv')
# print(df.head(5))

ans = df[(df['20L가격'] != 0) & (df['5L가격'] != 0)]
ans['차이가격'] = ans['20L가격'] - ans['5L가격']
# print(ans['가격차이'])

a = ans['차이가격'].groupby(ans['시도명']).mean()
# print(a)
print(round(max(a),1))  # 619.0


# 1-2 
# BMI는 몸무게(kg) / (키(M) * 키(M)) 로 정의 된다.
# 초고도 비만은 BMI 25이상 , 고도 비반은 BMI 25미만 - 23이상 , 정상은 23미만 - 18.5이상 저체중은 18.5미만으로 정의 된다. 
# 주어진 데이터에서 초고도비만 인원 + 저체중 인원 의 숫자는?

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_2_.csv')
# print(df.head(5))

def BMI(bmi):
    if bmi >= 25:
        return '초고도비만'
    elif bmi >= 23:
        return '고도비만'
    elif bmi >= 18.5:
        return '정상'
    else:
        return '저체중'
df['BMI'] = df['weight(kg)'] / (df['height(cm)']/100 * df['height(cm)']/100)
df['BMI'] = df["BMI"].apply(BMI)
# print(df.head(3))
# print(df['BMI'].value_counts())
a = len(df[df['BMI']=='초고도비만']) + len(df[df['BMI']=='저체중'])
print(a)    # 8998


# 1-3
# 순유입인원은 초중고 도내,도외 전입인원에서 초중고 도내, 도외 전출인원을 뺀값이다. 
# 각년도별로 가장 큰 순유입인원을 가진 지역구의 순유입인원을 구하고 전체 기간의 해당 순유입인원들의 합을 구하여라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p1_3.csv')
print(df.head(5))
print(df.columns)   # Index(['지역', '초등학교_전출_도내', '초등학교_전출_도외', '초등학교_전입_도내', '초등학교_전입_도외',
    #    '중학교_전출_도내', '중학교_전출_도외', '중학교_전입_도내', '중학교_전입_도외', '고등학교_전출_도내',
    #    '고등학교_전출_도외', '고등학교_전입_도내', '고등학교_전입_도외', '년도'],
    #   dtype='object')
df['순유입인원'] = (df['초등학교_전입_도내'] + df['초등학교_전입_도외'] + df['중학교_전입_도내'] + df['중학교_전입_도외'] + \
    df['고등학교_전입_도내'] + df['고등학교_전입_도외']) - (df['초등학교_전출_도내'] + df['초등학교_전출_도외'] + df['중학교_전출_도내'] + \
         df['중학교_전출_도외'] +  df['고등학교_전출_도내'] + df['고등학교_전출_도외'])

ans = df.groupby('년도')['순유입인원'].max().sum().sum()
print(ans)  # 13853


