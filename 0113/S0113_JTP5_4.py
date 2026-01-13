## 주요 개념 정리

"""
# 모든 오류 처리
try:

except:

# 선택한 오류만 처리
try:

except 발생오류:


# 선택한 오류가 발생할시 오류변수에 값을 넣어 출력
try:

except 발생오류 as 오류변수:

"""


## 💡 학습하면서 느낀 점


"""


"""

## ❓ 질문 및 궁금한 점


# 예외처리란

"""
구문을 실핼할떄 오류가 발생할때 처리하기 위한 방법이다.

"""

# 오류가 발생하는 경우

"""
#없는 파일을 읽기 형태로 호출할때

#f = open("a.txt",'r')
# 쓰기 형대로 호출하면 파일이 없을 경우 새로 파일을 생성하고 
# 기존에 존재하고 있다면 기존내용을 삭제한 이후 재생성한다.
#FileNotFoundError

#분모가 0인 경우
#ZeroDivisionError

#배열의 길이를 초과하는 인덱싱할 경우

#a = [1,2,3]
#a[3] # 0 ~ 2 까지 존재하는데 3을 인덱싱 한 경우
# IndexError

"""

#try-except 
"""
try:
a = [1,2]
print(a[3])
4/0

except IndexError as e:
    print(a)
    
except ZeroDivisionError as e:
    print(a)

"""
# 에러 동시 처리
"""

ry:
a = [1,2]
print(a[3])
4/0

except (IndexError,ZeroDivisionError) as e:
    print(a) # 하나로 묶어서 2개의 에러를 처리
    
    
"""


# try - else 
"""
#  추가된 else 는 except 구문이 실행되지 않을떄 동작
try:

except:

else: # except 구문이 실행되지 않을떄 동작

"""