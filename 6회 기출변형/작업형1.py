# 1-1
# 각 구급 보고서 별 출동시각과 신고시각의 차이를 ‘소요시간’ 컬럼을 만들고 초(sec)단위로 구하고
# 소방서명 별 소요시간의 평균을 오름차순으로 정렬 했을때 3번째로 작은 소요시간의 값과 소방서명을 출력하라

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e6_p1_1.csv')
# print(df.head(5))

df['소요시각'] = (
                pd.to_datetime(
                    df['출동일자'].astype('str') + df['출동시각'].astype('str').str.zfill(6)
                )
                - 
                pd.to_datetime(
                    df['신고일자'].astype('str') + df['신고시각'].astype('str').str.zfill(6)
                )
                ).dt.total_seconds()
# print(df['소요시각'].head())
ans = df.groupby('소방서명')['소요시각'].mean().sort_values(ascending=False).reset_index()
print(ans.iloc[2].values)   # ['동대문소방서' 228.14851485148515]


# 1-2 
# 학교 세부유형이 일반중학교인 학교들 중 일반중학교 숫자가 2번째로 많은 시도의 일반중학교 데이터만 필터하여 
# 해당 시도의 교원 한명 당 맡은 학생수가 가장 많은 학교를 찾아서 해당 학교의 교원수를 출력하라
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e6_p1_2.csv')
# print(df.head(5))

ans = df[df['학교세부유형'] == '일반중학교']
# print(ans)
# print(ans['학교명'].groupby(df['시도']).size().sort_values())   # 서울
# print(ans[ans['시도']=='서울'])
ans = ans[ans['시도']=='서울']
ans['total'] = ans['일반학급_학생수_계']/ans['교원수_총계_계']
ans = ans.sort_values('total', ascending=False).reset_index()
print(ans.iloc[0]['교원수_총계_계'])    # 33

# 1-3
# 5대 범죄(절도, 사기, 배임, 방화, 폭행)의 월별 총 발생건수를 총범죄수라고 표현하자. 
# 18,19년의 각각 분기별 총범죄수의 월평균 값을 구했을때 최대값을 가지는 년도와 분기를 구하고 
# 해당 분기의 최댓값의 사기가 발생한 월의 사기 발생건수를 출력하라
# (1분기:1,2,3월 / 2분기 : 4,5,6월 / 3분기 7,8,9월 / 4분기 10,11,12월 , 1분기 월평균 : 1,2,3월의 총범죄수 평균)
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e6_p1_3.csv')
print(df.head(5))
df['총범죄수'] = df['절도'] + df['사기'] + df['배임'] + df['방화'] + df['폭행']

분기_2018_1 = df['총범죄수'][:3].mean()
분기_2018_2 = df['총범죄수'][3:6].mean()
분기_2018_3 = df['총범죄수'][6:9].mean()
분기_2018_4 = df['총범죄수'][9:12].mean()
분기_2019_1 = df['총범죄수'][12:15].mean()
분기_2019_2 = df['총범죄수'][15:18].mean()
분기_2019_3 = df['총범죄수'][18:21].mean()
분기_2019_4 = df['총범죄수'][21:24].mean()
# print(분기_2018_1, 분기_2018_2, 분기_2018_3, 분기_2018_4, 분기_2019_1, 분기_2019_2, 분기_2019_3, 분기_2019_4)
# print(max(분기_2018_1, 분기_2018_2, 분기_2018_3, 분기_2018_4, 분기_2019_1, 분기_2019_2, 분기_2019_3, 분기_2019_4))
# print(분기_2019_2)

print(df['사기'][15:18].max())  # 27766




