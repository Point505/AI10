### 오늘 학습한 챕터

#Bool 기초 10문제
#점프 투 파이선 날개 달기 
    # 클래스


### 주요 개념 정리


#bool 자료형
    # print 안에서 비교를 하면 True False 가 출력된다.
    # 연산자는 and or not  있다.
    






## 💡 학습하면서 느낀 점



## ❓ 질문 및 궁금한 점

"""
result = 0

def add(num):
    global result # 지역변수로 설정하면 함수가 종료될때 초기화 되므로 Global을 사용 전역변수로 사용
    result+=num 
    
    return result # return 값이 없으면 None 값이 출력됨

print(add(3)) 
print(add(4)) # 초기에 들어간 값 3과 이번에 들어간 4를 합쳐 7을 반환함


"""
"""
# 클래스가 설계도 객체가 그 설계도를 이용한 결과물


class calculator:
    
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result+=num
        return self.result
    
    
cal1 = calculator()
cal2 = calculator()


print(cal1.add(2))
print(cal1.add(4))

"""



