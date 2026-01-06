

"""


    
"""

# 매개변수에 초깃값 미리 설정하기

"""
def say_myself(name,age,man=True): 
    print(f"나의 이름은 {name} 입니다.")
    print(f"나의 나이는 {age}입니다.")
    
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
        
say_myself("홍길동",27,True)

"""
"""
a = 1 

def vartest(a):
    a+=1 # 전역변수와 별개로 함수 내부에서만 존재하는 변수


vartest(a) # return 값이 없음으로 a의 값은 변하지 않는다.

print(a) # 결과 값은 1

# 만약 a = vartest(a) 의 방식으로 해도 리턴값이 없음으로  None 값이 저장된다.

"""



# return 과 global
"""
a = 1 

def vartest(a):
    a+=1 
    return a # 함수 내 변수를 연산 후 리턴


a = vartest(a)  # 해당 값을  번수 a 에 저장

print(a) 

"""
"""
a = 1 

def vartest(a):
    global a # 교재에는 할당 후 글로벌로 변수를 재할당하는걸 보여줬는데
            # 정책상으로 막아 놓은건지 이미 할당되었다고 사용불가
    
    a+=1 
    return a # 함수 내 변수를 연산 후 리턴


a = vartest(a)  # 해당 값을  번수 a 에 저장

print(a) 
"""


"""
# lamebda  예약어

# lambda는 함수를 생성할 때 사용하는 예약어로 Def와 동일한 역할을 한다.

add = lambda a,b:a+b

def add(a,b):
    return a+b


result = add(3,4)

print(result)

print('a')"""






#------------------------------------------------------------------------------------------------------------------

# 사용자 입출력 받기



# input을 사용하여 값을 받는다. 
# input은 문자열 형태이기 때문에 숫자를 입력한 뒤에는 문자열을 숫자 형태로 바꿔줄 필요가 있다.
# input 으로 받은 숫자를 저장한 변수가 A 라고 가정을 한다면 int(A) 형태로 바꿔주면 str이 int 로 전환된다.


# 큰 따옴표로 둘러싸인 문자열은 +와 동일하다.
"""
print("li,fe"+"is","to short")

"""


for i in range(10):

		print(i,end='')
  
  
  #------------------------------------------------------------------------------------------------------------------
  
"""

# r = > 읽기 모드
# w = > 쓰기 모드
# a = > 추가 모드 ; 파일의 마지막에  새로운 내용을 추가할때 사용한다.
  
"""