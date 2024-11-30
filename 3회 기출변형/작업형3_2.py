import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/krdatacertificate/e3_p3_2_.csv')
df.head()

from scipy.stats import shapiro

# 10-1 a,b 상황 각각 정규성을 가지는지 샤피로 검정을 통해 확인하라.
a = df[df['group']=='A'].rpm
b =  df[df['group']=='B'].rpm
print(shapiro(a)) #pvalue=0.397     # ShapiroResult(statistic=0.9863896921013734, pvalue=0.3979080924239819)
print(shapiro(b)) #pvalue=0.956     # ShapiroResult(statistic=0.9943944976838186, pvalue=0.9562843067714429)

# A,B 공장 생산 제품의 rpm은 각각 정규성을 가지는지 샤피로 검정을 통해 확인하라. (각 공장의 pvalue 출력할 것)
from scipy.stats import levene
s , p =levene(a,b)
round_p = round(p,3)
print(round_p)  # 0.904

# 대응 표본 t 검정을 통해 B공장 제품들의 rpm이 A 공장 제품의 rpm보다 크다고 말할 수 있는지 검정하라. 
# pvalue를 소숫점 이하 3자리까지 출력하고 귀무가설, 대립가설 중 하나를 출력하라
from scipy.stats import ttest_rel
s , p =ttest_rel(b,a,alternative='greater')
round_p = round(p,3)
print(round_p)  # 0.009
print('대립')