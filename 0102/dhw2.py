
# 1.정수 a = 10, b = 3이 주어질 때 *사칙연산 결과(+, -, , /) 를 한 줄씩 출력하라.

a=10
b=3
print(a+b) # 더하기
print(a-b) # 뺴기
print(a*b) # 곱하기
print(a/b) # 나누기





# 2.정수 n이 주어질 때 n이 짝수면 “even”, 홀수면 "odd"를 출력하라.

a = input()
if (int(a)%2) == 0: # input 으로는 문자형으로 인식함으로 자료형을 입혀서 숫자형으로 바꿔준다.
    print("even")
else:
    print("odd")





# 3.정수 n이 주어질 때 n의 제곱을 출력하라.

a = input()

print(int(a)**2)





# 4.정수 n이 주어질 때 n의 절댓값을 출력하라.

a = input()
b = int(a)
if b < 0 :
    print(b*-1) # 만약 숫자가 0 보다 작다면 음수 이므로 -1을 곱하여 양수로 바꿔준다.
else:
    print(b)





# 5.정수 a, b가 주어질 때 큰 수를 출력하라.

a= int(input())
b= int(input())

if (a > b):
    print(a)
elif(b > a):
    print(b)
else:
    print("=") # 같은 값인 경우





# 6.실수 x = 3.14159가 주어질 때 소수 둘째 자리까지 반올림하여 출력하라.

x = 3.14159

print(round(x,2))





# 7.정수 n이 주어질 때 1부터 n까지의 합을 출력하라.

n = int(input())
sum = 0 # 0으로 초기화를 하지 않으면 에러가 발생

for i in range(1, n + 1): # 1부터 입력한 수까지 ( 마지막 수는 카운트에서 제외됨으로 +1 처리 )
    sum += i

print(sum)





# 8.정수 n이 주어질 때 n의 자릿수 개수를 출력하라.

a = int(input())
count = 0

while 1 :
    if a >= 1:
        count+=1
        a=a/10


    else:
        break

print(count)





# 9.정수 n이 주어질 때 n이 3의 배수이면서 5의 배수인지 True / False로 출력하라.

a = int(input())

if ((a%3==0)&(a%5==0)): # 3의 나머지 값과 5의 나머지 값이 0일때 True 를 출력
    print("true")
else:
    print("false")




# 10.정수 n이 주어질 때 n의 일의 자리 숫자를 출력하라.

a = int(input())
a = a % 10 # 10으로 나누었을때 나오는 나머지

print(a)