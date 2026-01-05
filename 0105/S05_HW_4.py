# 리스트형
# 1.리스트 [1, 2, 3, 4, 5]의 모든 요소의 합을 출력하라.
""""
result = 0

for i in [1,2,3,4,5]:

    result += i
    
print(result)
"""


# 2.리스트 [1, 2, 3, 4, 5]에서 짝수만 담은 새 리스트를 만들어 출력하라.

""""numbers = [1,2,3,4,5]
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)""" # 리스트 컴프리헨션


# 3.리스트 [3, 1, 4, 2]를 오름차순으로 정렬하여 출력하라.

"""
a = [3,1,4,2]

for i in range(0,len(a)-1,1):
    for j in range(i,len(a)-1,1):
        
        if a[j]>a[j+1]:
            
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
        else:
            continue
    
print(a)
    
    """

# 4.리스트 [10, 20, 30, 40]에서 최댓값을 출력하라.

"""
a = [10,20,30,40]

for i in range(0,len(a)-1,1):
    for j in range(i,len(a)-1,1):
        
        if a[j]>a[j+1]:
            
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
        else:
            continue
print(a[3])
"""
# 5.리스트 [10, 20, 30, 40]에서 최솟값을 출력하라.
"""a = [10,20,30,40]

for i in range(0,len(a)-1,1):
    for j in range(i,len(a)-1,1):
        
        if a[j]>a[j+1]:
            
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            
        else:
            continue
print(a[0])"""

# 6.리스트 [1, 2, 3, 4, 5]를 역순 리스트로 만들어 출력하라.

"""a = [1,2,3,4,5]

b = len(a)
list=[]

for i in range(b-1,-1,-1):
    s =a[i]
    list.append(s)
    
print(list)"""

# 7.리스트 [1, 2, 3, 2, 2, 4]에서 숫자 2가 몇 번 등장하는지 출력하라.
"""a = [1, 2, 3, 2, 2, 4]
b = len(a)
count =0

for i in range(0,b,1):
   if a[i] == 2 :
       count +=1
    
print(count)"""

# 8.리스트 [1, 2, 3]에 숫자 4를 추가한 뒤 출력하라.
"""a = [1, 2, 3]
a.append(4)

print(a)"""

# 9.리스트 [1, 2, 3, 4, 5]에서 인덱스 1 ~ 3까지 슬라이싱하여 출력하라.

"""a =[1, 2, 3, 4, 5]
a = a[1:4]

print(a)"""
# 10.리스트 안의 숫자들을 모두 문자열로 바꾼 리스트를 만들어 출력하라.

"""a = [1,2,3,4,5]
list = []
for i in a:
    
    list.append(str(i))
    
print(list)"""

  
