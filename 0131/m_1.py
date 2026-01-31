
#문자열 포매팅 연습

name = "Alice"
age = 25
height = 165.5

print(f"이름: {name}, 나이: {age}, 키: {height}")





#문자열 다루기 연습


# 문자열 인덱싱
#첫 번째 문자 마지막 문자

text = "PythonProgramming"
a = len(text)

print(text[0]+text[-1])




# 문자열 슬라이싱
# 다음 문자열에서 슬라이싱만 사용해서 결과를 만들어라.

text = "HelloWorldPython"

a = text[:5]
b = text[5:10]
c = text[10:]
print(f"[{a} \n{b} \n{c}")




#문자열 메서드 (upper, lower, strip)
text = "   PyThOn Is FuN   "
#아래 결과를 순서대로 출력하시오.
print(text)


#양쪽 공백 제거

text = text.strip()
print(text)


#모두 소문자로 변환

text = text.lower()
print(text)


#모두 대문자로 변환

text = text.upper()
print(text)







#문자열 메서드 (replace, count, find)
#문제 4

#다음 문자열을 사용하시오.

text = "banana apple banana orange banana"


#"banana"가 몇 번 등장하는지 출력

a = text.count("banana")
print(a)


#"banana"를 "grape"로 모두 바꾼 문자열 출력

a = text.replace("banana","graph")
print(a)

#"apple"이 처음 등장하는 위치(index) 출력

a = text.find("apple")
print(a)





# 리스트 컴프리헨션 사용하기

words = ["Python", "java", "C++", "python", "Go", "PYTHON", "ruby"]
# 문자열의 길이가 5 이상인 것만 출력

a = [x for x in words if len(x) >=5 ]
print(a)





students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90}
]


#인덱싱
#첫 번째 학생의 이름을 출력하시오.
a = students[0]["name"]

print(a)


#슬라이싱
#앞의 두 명 학생 정보만 슬라이싱하여 새로운 리스트로 만드시오.
a = [students[0],students[1]]
print(a)



#추가
#아래 학생 정보를 리스트에 추가하시오.
#{"name": "Eve", "score": 88}
students.append({"name": "Eve", "score": 88})
print(students)

#수정
#"Charlie"의 점수를 80점으로 수정하시오.
students[2]["score"] = "80"

print(students[2]["score"])

#삭제
#점수가 90점 이상인 학생만 제거하시오.

students = [s for s in students if int(s["score"]) < 90]


print(students)