# 클래스


# 쿨래스란 무엇인가?
"""  

클래스가 없어도 만들 수 있다.  ( 필수요소는 아니다. )

클래스로 만들어진 객체는 고유한 성격을 가진다. ( 서로 영향을 주지 않는다. )


 A = Cookie()로 만든 A는 객체이다.
 
 A는 Cookie의 인스턴스다.
 
 
 
 





"""


"""
result = 0


def add(num):
    global result
    result+=num
    
    return result

print(add(3))
print(add(4))

"""




"""
# 계산할때마다 다른 값을 저장하기위해 새로운 함수를 만들 필요없이
객채룰 생성하여 대체한다.
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result+=num
        return self.result
    
    
cal1 = Calculator() # 객체 생성
cal2 = Calculator()


 """
 
 
 
class Foulcal:
 
 
 
a = Foulcal()

a.setdata(4,2)

a.add()
  