

import pandas as pd

"""
a = pd.DataFrame({'Yes':[50,21],'No':[131,2]})
# DataFrame은 테이블이고 개별항목들의 배열로 이루어져있다.
# 각 항목은 특정한 값을 가진다.
# 각 항목은 행이나 열에 속한다.
#({'})
print(a)

"""



"""
a = pd.DataFrame({'Bov':['I Like It','It was awful'],
                  'Sue':['Pretty good','Bland']})
# 첫번쨰 값이 열 이름, 그 다음 대괄호에 있는게 해당열에 자료
print(a)
"""



"""
a = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(a)"""