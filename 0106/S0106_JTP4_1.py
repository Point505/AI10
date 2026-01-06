

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



# lame