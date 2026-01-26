import numpy as np
import pandas as pd
# 패키지를 as 를 사용하여 약칭을 사용
"""

data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = dp.DataFrame(data=data,index=row,columns=col)
print(df)"""


"""# 전치  => 행과 열을 바꾸는 것
# 2 X 3 = > 3x  2


col = ['col1','col2','col3']
row = ['row1','row2','row3','row4']
data = [['A',1,2],['B',3,4],['C',5,6],['D',7,8]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)
"""




np.random.seed(0)
arr = np.random.randint(10,size=(2,2))
#  0부터 10 사이의 수로 2x2의 행렬을 만든다.
print(arr)

df1 = pd.DataFrame(arr, copy=False)
#copy true 에 값은 변하지 않는다.
df2 = pd.DataFrame(arr, copy=True)
#copy flase 에 값은 변한다.


arr[0,0] = 99
print(df1)
print(df2)

