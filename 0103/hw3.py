

# 1.문자열 s가 주어질 때 문자열의 길이를 출력하라.
"""a = input()
print(len(a))""" 
# len 함수는 받은 문자열을 숫자로 변환 ( 공백도 포함 )

# 2.문자열 s가 주어질 때 첫 글자와 마지막 글자를 출력하라.
"""a = input()
print(a[0] , a[-1])"""
#받은 문자열의 첫 문자는 0번에 마지막 문자는 길이를 모르기 때문에 -1 역으로 읽음
# 3.문자열 s가 주어질 때 문자열을 모두 대문자로 변환하여 출력하라.
"""s = input()
for i in s:
    if 97<= ord(i) <=122: # 아스키 코드의 소문자 값은 97 ~ 122
         print((chr(ord(i)-32)),end="")
         
         
    else :
        print(i,end="")"""

# ord => 문자를 아스키 코드값 int 형으로 변환
#chr => int 형 숫자를 문자로 변환 

# 소문자가 대문자 보다 32가 큼으로 소문자를 아스키 코드 값으로 변환하여 32를 빼줌

# 4.문자열 s가 주어질 때 문자열을 모두 소문자로 변환하여 출력하라.
"""s = input()
for i in s:
    if 65<= ord(i) <=90:
         print((chr(ord(i)+32)),end="")
         
         
    else :
        print(i,end="")"""
        
# 5.문자열 s가 주어질 때 문자열에 'a'가 몇 개 있는지 출력하라.
""" s = input()
count = 0
for i in s:
    if i == 'a': # 같은 문자가 있는지 확인
        count+=1 # 있다면 + 1
    else: 
        continue # 없다면 패스
print(count)       """

# 6.문자열 s가 주어질 때 문자열을 거꾸로 출력하라.

"""s = input()
a = len(s) # 받은 문자열의 길이 확인
for i in range(a-1,-1,-1):# 받은 문자열의 길이를 그대로 넣으면 길이 초과 에러 발생
# range 함수는 마지막 전까지 읽음으로 -1 순방향은 + 1
# -1 씩 역순으로 읽으며 출력
    print(s[i],end ="") """

# 7.문자열 s가 주어질 때 'python'이라는 단어가 포함되어 있으면 True, 아니면 False를 출력하라.
"""s = input()
w = s.split() # 공백을 기준으로 나눠 배열에 저장
count = 0 # 마지막까지 나오지 않을 경우 비교를 위해 

for i in w:
    if i == "python":
        print('True')
        break # 있다면 True 출력 후 종료
    else:
        if count == len(w)-1: # 나눈 단어의 수를 계산
            
          print('False')
          break # 마지막까지 나오지 않는다면 False 출력 후 종료
        count+=1  
        continue"""
            
# 8.문자열 "hello world"에서 공백을 제거한 문자열을 출력하라.
"""a = "hello world"
b = a.split() # 공백을 기준으로 나눈 뒤
c = b[0]+b[1] # 두 단어를 다시 붙임

print(c)"""

# 9.문자열 s가 주어질 때 문자열이 회문인지 True / False로 출력하라.
"""
a = input()
b = len(a)
count = 0


if b%2==0:
    c = int(b/2)-1
    for i in range(0,int(len(a)/2),1):
       if a[i] == a[len(a)-i-1]:
          if c == i:
             print('True')
             continue
             
       else:
          if c == i:
             print('False')     
else:
    c = int(b/2)-1
    for i in range(0,int(len(a)/2),1):
       if a[i] == a[len(a)-i-1]:
          if c == i:
             print('True')
             continue
             
       else:
          if c == i:
             print('False')   

                    """
                    
# 10.문자열 "abc123"에서 숫자만 추출해서 출력하라.lb

"""a = 'abc123'
for i in a:
    if 48<= ord(i) <=57 :
        print(i,end="")
    else:
        continue"""