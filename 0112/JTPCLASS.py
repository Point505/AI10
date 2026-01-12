
"""
### 오늘 학습한 챕터

1. 파이썬 날개 달기
   - 클래스

### 주요 개념 정리
    
- 클래스
     - 클래스란 틀을 의미하며 안에 함수를 만들어 놓고
        객체를 생성하여 개별적인 값을 얻을 수 있음
        
     - 클래스 내에 있는 함수는 메소드 변수는 속성   
     
     - 메서드에 할당된 매개변수는 3개인데
        전달할 값은 2개인 이유
        a.setdata(4,2) 이런식으로 실행할 경우
        setdata에 첫번째 매개변수 self에 객체 a가 전달된다.

그러므로 메서드를 호출할때 달리 값을 넣지 않아도 객체를 전달해야 하므로
메소드에 self 는 필수이다
메서드를 호출하는 방법은
a=foulcal() # 객체생성
a.setdata(4,2) # 객체.메서드(값1,값2)
a=foulcal() # 객체생성
foulcal.setdata(a,4,2)#클래스,메서드(객체, 값1,값2)
#어차피 객체를 생성해야 되면 굳이 클래스와 객체를 한번더 작성할
#필요는 없을 듯 하다.


    #속성 호출 #
        #개별적으로 속성 호출도 가능하다.
#객체 속성(변수 self는 붙이지 않아도됨)





## 💡 학습하면서 느낀 점
    - 클래스가 없으면 개별적인 값을얻으려 할때 기존 함수를 초기화 시켜야되었으나
        클래스 안에 함수를 만들어 두면 객체를 생성하여 서로 값에 영향을 받지않고 계산할 수 있다.
  
    - 공부를 할때 메소들와 함수의 차이가 궁금했는데 클래스 안에 있냐 밖에 있냐 차이

## ❓ 질문 및 궁금한 점

"""



"""
class Person:
    def __init__(self, name, age): # 객체 생성 시 name과 age를 받아 초기화
        self.name = name
        self.age = age
        
    def intro(self):# 반드시 하나 이상의 매개변수 필요
        print(self.name,self.age) # 입력받은 값을 출력
        
        
# 객체 생성 (자동으로 __init__ 호출됨)
p1 = Person("홍길동", 30)
p1.intro() # 출력: 홍길동


"""
"""
class Calculator:

    def_init__(self): # 클래스안에 함수를 정의할때 반드시 첫번째 매개변수를 지정해야됨

        self.result = 0 #최초 호출시 init은 자동호출

    def add (self,num):

        self.result+=num # 받은 값을 result에 저장

        return self.result # add 호출시 깂 반환

cal1 = Calculator()

cal2 = Calculator()

print(cal1.add(3))

print(cal1.add(4))


"""
"""
class Calculator:

    def __init__(self): # 클래스안에 함수를 정의할때 반드시 첫번째 매개변수를 지정해야됨

        self.result = 0 #최초 호출시 init은 자동호출

    def add(self,num):

        self.result+=num # 받은 값을 result에 저장

        print(self.result)

cal1 = Calculator()

cal2 = Calculator()

cal1.add(3) # print를 함수에 넣어 놓으면 추가로 print를 사용할 필요 없음

cal1.add(4)

"""

"""
class Fourcal:

    def setdata(self,num1, num2): # 계산할 값을 입력

        self.num1 = num1
        self.num2 = num2 # self는 객체안에 자신을 가리키는 것

    def add(self):

        print(self.num1+self.num2) # 받은 값으로 계산하여 출력

    def sub(self):

        print(self.num1-self.num2)

    def mul(self):

        print(self.num1*self.num2)

    def div(self):

        print(self.num1/self.num2)
        
a = Fourcal()

a.setdata(4,2)
a.add()
a.sub()
a.mul()
a.div()
"""
"""
class Calculator:

    def __init__(self,num1,num2):

        self.num1 =num1

        self.num2 =num2
        
    def add(self):

        print(self.num1+self.num2)   
        

class MoreCalculator(Calculator): # Calculator 클래스 상속 #class 클래스

        pass

a = MoreCalculator(4,2)

a.add()
"""

#상속을 받을 경우 상속받은 클래스안에 있는 메서드와 속성을 사용가능

#상속 받은 클래스에 메서드 외에도 자체적으로 메서드를 작성하여 사용가능
"""
# 클래스 상속 후 자식 클래스 내에 메서드를 재정의하여 출력
class Calculator():

    def __init__ (self,num1, num2):

        self.num1 = num1
        self.num2 = num2

    def add(self):

        print(self.num1+self.num2)

class MoreCalculator(Calculator): # Calculator 클래스 상속 #class 클래스

    def pow(self):

        result = self.num1** self.num2
        print(result)

a = MoreCalculator(4,2)

a.pow()

"""
"""
class FoulCal:

    def __init__ (self,first,second): # init 함수는 무조건 언더비가 양쪽에 2개씩 있어야 한다.

        self.first = first
        self.second = second

class SafeFoulCal(FoulCal):

    def Div(self):

        if self.second == 0: # 분모가 0일 경우 에러가 발생하여 0일경우 0을 출력하도록 처리
            print("0")

        else:
            print(self.first/self.second)# 그 외에는 정상적으로 계산

a=SafeFoulCal(4,0)

a.Div()
"""
"""
class Family:
    
    lastname = "김"
    
    
a=Family()    
b=Family()

print(a.lastname)

Family.lastname="박" # 기존에 클래스 속성을 김으로 설정하더라도 
# 뒤에 속성을 박으로 바꾸면 객체에도 똑같이 적용이 된다.

print(a.lastname)

"""
"""
class Family:
    
    lastname = "김"
    
    
a=Family()    

a.lastname="박" # 반대 상황으로 객체의 속성을 바꿔도 클래스의 속성은 바뀌지 않는다.

print(a.lastname)# 객체
print(Family.lastname)# 클래스

"""

