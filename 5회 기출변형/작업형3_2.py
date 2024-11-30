import pandas as pd 
df= pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e5_p3_2.csv')
print(df.head())
    
# 3-2-a
# 3 그룹의 데이터에 대해 크루스칼-왈리스 검정을 사용하여 검정 통계량을 반올림하여 소숫점 이하 3자리까지 구하여라
from scipy.stats import kruskal
# print(help(kruskal))
s, p = kruskal(df[df['ID']=='A'].value, df[df['ID']=='B'].value, df[df['ID']=='C'].value)
print(round(s,3))   # 6.521


# 3-2-b
# 3 그룹의 데이터에 대해 크루스칼-왈리스 검정을 사용하여 p-value를 반올림하여 소숫점 이하 3자리까지 구하여라. 
# \귀무가설과 대립가설중 0.05 유의수준에서 유의한 가설을 출력하라
print(round(p,3))   # 0.038
print('대립가설')  

