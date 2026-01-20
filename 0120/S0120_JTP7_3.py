## 주요 개념 정리
"""

이터레이터

- 데이터를 하나씩 가져올 수 있는 객체

- next 함수를 사용하여 하나씩 가져올 수 있다

- 끝까지 출력하면 Stopiteration 에러를 발생시키며 For 구문이나 try except 구문을 사용하여 방지할 수 있다.

- 반복가능 하다고 이터레이터는 아니지만 반복가능하면 이터레이터로 만들 수 있다.

- 한번 호출하고 나면 다시 가져올 수 없다.



제너레리터란


- 이터레이트를 클래스로 만들려면 _iter_ _next_ 메서드를 구현 해야하지만

   제너레이터를 사용하면 함수 하나만으로 이터레이터를 만들 수 있음

"""

## 💡 학습하면서 느낀 점




## ❓ 질문 및 궁금한 점


"""

# 반복가능 하다고 이터레이터는 아니지만

# 반복가능하면 이터레이터로 만들 수 있다.

a =[1,2,3]

ia = iter(a)

print(type)

=> <class 'list_iterator>

print(next(ia))를 사용하면 한칸씩 밀어내면서 출력함 여기서 배열크기를 넘어가면 Stopiteration 
에러가 발생


"""


"""

StopIterateration 에러를 방지 하기위해 for 구문을 사용
자동적으로 처리해준다.

a =[1,2,3]

ia = iter(a)

for i in ia:
       print(i) # 를 사용한다

"""



"""
# 메서드 체이닝

#연속적인 코드줄에서 메서드를 반복적으로 호출하는 것을 의미

string = string.upper() # 문자열을 대문자로 변환

string = string.strip() # 문자열 양쪽의 공백을 제거

length = len(stirng)

#위 3개를 밑에 한줄로 요약할 수 있다.

length = len(string.upper().strip())

"""






"""
# 한번 출력된 값은 다시 출력이 안된다는 예시

a = [1,2,3]

ia = iter(a)

for i in ia:

print(i) #1회 수행

#>> 정상 출력

for i in ia:

print(i)# 2회 수행

#>> 출력 없음


"""



"""
# return self 예제
이터레이터를 리스트 형 변환이 아닌 직접 만들기

_iter_ 메서드: 이터레이터 객체 자신을 반환한다.

_next_ 메서드: 다음 값을 반환하고 더이상 값이 없으면

Stopiteration 에러를 발생시킨다.
class Counter:

    def __init__(self,start=1):
        
        self.val = start

    def increment(self):

        self.val +=1

    def decrease(self):

        self.val -=1

        return self

    count = Counter()

    retult = coount().increment().increment().decrease()

    print(result.val)

"""



class Myiterator:

    def __init_(self,data): #호출시 최초 실행

        self.data = data #

        self.position = 0

    def __iter__(self): # self 반환

        return self #줄 메서드 체이닝을 하기위한 함수호출시

                    #자신을 재호출 하면서 연쇄적으로 다른 함수를 사용할 수 있다..

    def __next__(self):

        if self.position >= len(self.data): # 받은 문자열의 길이와 값을 비교

            raise Stopiteration # 만약 문자열보다 값이 크다면 에러를 방생

        result = self.data[self.position] # 아니라면 값에 해당하는 위치의 문자를

        self.position +=1# 그 다음 위치로 이동

        return result

if __name__ == "__main__":

    i = Myiterator([1,2,3])

    for item in i:

        print(item)





"""
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1 # 길이가 3인 배열

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < 0:
            raise StopIteration # position이 0보다 작으면
                                # 에러를 발생
        result = self.data[self.position] # 아니면 해당하는 문자 반환
        self.position -= 1 # 호출할때 마다 1씩 감소
        return result

if __name__ == "__main__": # 해당 문구가 있는 파일에서만 수행
    i = ReverseIterator([1, 2, 3]) # 인스턴스 생성
    for item in i:
        print(item)


"""



"""
제너레리터란


이터레이트를 클래스로 만들려면

_iter_

_next_ 메서드를 구현 해야하지만

제너레이터를 사용하면 함수 하나만으로

이터레이터를 만들 수 있음
"""

"""
def mygen():

    yield 'a'

    yield 'b'

    yield 'c'

g = mygen()

next(g)= > a

next(g)= > b

next(g)= > c

#next를 실행할때 마다 알아서 한칸씩 뒤로 밀려감

# 이터레이터와 마찬가지로 길이를 초과하면

#Stoplteration error가 발생한다.

"""


"""

def mygen():
    for i in range(1, 1000): # 1,4,9,16,25
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))

gen = (i * i for i in range(1, 1000))
# 리스트 대신 튜플을 사용

import time

def long_time_job():
    print("job start")
    time.sleep(1) # 1초 지연
    return "done"

# list job
list_job = [long_time_job() for i in range(5)]
print(list_job)

"""

