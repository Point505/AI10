## 주요 개념 정리


## 💡 학습하면서 느낀 점




## ❓ 질문 및 궁금한 점



# 클로저란?
# 외부 함수의 변수를 기억하는 내부 함수
"""보통 변수는 속해있는 함수가 종료되면 사라지는데 클로저에서는
함수가 사라지더라도 해당 함수에 속해있는 변수를 사용할 수 있다



# if __name__ =" __main__ "

해당 구문이 작성된 파일을 직접 실행했을때만 아래 코드를
작동시키겠다.

요는 다른 파일을 import 해서 사용하는 경우  가져올 파일에 __name__ = __main__ 이 설정되어 있지않으면 
예상치 못한 실행이 있을 수 있다.


"""



"""
# 일반적인 함수
class Pow1:
    def __init__(self,m): # 객체 생성시 최초로 실행되는 함수
        self.m = m

    def pow1 (self,n): # 생성한 객체에 함수 호출시 사용
        return pow(self.m,n) # 결과적으로 최초 받은 값에 제곱할 수 를 입력



pow2 = Pow1(3) # 인자 3을 전달한 객체 생성

print(pow2.pow1(2)) # class Pow1 에 있는 함수 pow1 호출

"""


"""
# __ call ___
class Mul:
    def __init__(self,m):
        self.m = m
        
    def __call__(self,n):
         return self.m*n
     
     
mul3 = Mul(3)
mul5 = Mul(5)

print(mul3(10)) # __call__ 함수를 사용하면  해당 함수를 바로 호출 가능
print(mul5(10)) 
            """
            
# wrapper 함수

""" """
"""
def mul(m):
    def wrapper(n):
        return m*n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3) # 인자 3을 mul 함수에 전달
    mul5 = mul(5)
    
print(mul3(10))"""


import time

def ela