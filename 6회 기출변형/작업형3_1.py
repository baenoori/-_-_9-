# A 도시의 남성 600명과 여성 550명이 있다. 남성들 중 흡연자 비율은 0.2이며 여성들 중 흡연자 비율은 0.26이다.
# 남성과 여성 간에 흡연 여부에 따른 인구 비율이 다른지 확인하고 싶다. 유의 수준 0.05하 귀무가설에 대해 기각 / 채택 여부와 p-value값을 각각 출력하라

import numpy as np
from scipy.stats import chi2_contingency

# 남성과 여성의 인구 수
total_male = 600
total_female = 550

# 남성과 여성 중 흡연자의 비율
smoking_ratio_male = 0.2
smoking_ratio_female = 0.26

# 흡연자와 비흡연자의 인구 수 계산
smoking_male = int(total_male * smoking_ratio_male)
non_smoking_male = int(total_male - smoking_male)

smoking_female = total_female * smoking_ratio_female
non_smoking_female = total_female - smoking_female

# 데이터 배열 생성 (빈도로 변환)
data = np.array([[smoking_male, non_smoking_male], [smoking_female, non_smoking_female]])

# 카이제곱 검정 수행
chi2_stat, p_val, dof, expected = chi2_contingency(data)

print('기각',p_val) # 기각 0.018786854975740768


