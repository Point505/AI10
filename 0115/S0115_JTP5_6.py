## 주요 개념 정리

# datetime.date : 연월일로 날짜를 표현할 때 사용하는 함수

## 💡 학습하면서 느낀 점


"""


"""

## ❓ 질문 및 궁금한 점

# 표준 라이브러리

"""
# datetime.date


# 날짜간 차를 구하는 방법

import datetime

day1 = datetime.date(2021,12,14)
day2 = datetime.date(2023,1,2)

diff = day2 - day1

print(diff)

"""


"""

import datetime

day = datetime.date(2011,11,14)

print(day.weekday()) # 해당하는 닐짜의 요일을 출력


"""

# 
import time

time.time()