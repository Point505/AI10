# dx = [['idx1','idx1','idx2','idx2','idx2'],['row1','row2','row1','row2','row3']]
# 2차원 리스트 형태

import numpy as np
import pandas as pd
import matplotlib as plt


""" 

ewm:
오래된 데이터에 지수감쇠를 적용하여 최근 
데이터가 더 큰 영향을 끼지도록 가중치를 주는 함수입니다.

최근에 나온 데이터에 가중치를 주기위해 과거일수록 
감쇠를 주는 함수


시계열 데이터를 다룰때 사용


지수가중함수는 알파값을 봐야됨 = 감쇠함수

com 질량중심
span 계산 기간으로 평활계수를 계산합니다.
halflife = 반감기를 이용하여 평활계수를 계산합니다.

min_periods: 계산을 위한 최소기간


adjust  상대적 가중치의 불균혈을 

해소하기위해 조정계수로 나눈지의 여부입니다.

"""


"""

지수가중함수 ewm 
axis 계산을 수행할 축 입니다.
times 관찰에 해당하는 시간입니다. 단조증가 형태의 datetime64
형태여야 합니다.


"""
"""# numpy 2.0 버전 부터는 NaN 이 아닌 nan로 사용해야됨
data = {'val':[1,4,2,3,2,5,13,10,12,14,np.nan,16,12,20,22]}
df = pd.DataFrame(data).reset_index()
print(df)
"""

val = np.linspace(0,100,101)
sin = np.sin(np.pi/25*val)
tan = np.tan(np.pi/25*val)
df = pd.DataFrame(data={'val':val,'sin':sin,'tan':tan})


df2 = df.loc[:,['sin','tan']]

df2.plot()
plt.show()