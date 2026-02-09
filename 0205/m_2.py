#try–except 문으로 예외 처리하기

# ZeroDivisionError 처리
try:
    a = int(input("1번째 수:"))
    b = int(input("2번째 수: "))
    result = a / b
    print("결과:", result)

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

except ValueError:
    print("정수만 입력하세요.")




# ValueError 처리
try:
    num = int(input("정수 입력: "))
    print("제곱:", num ** 2)

except ValueError:
    print("정수만 입력하세요.")




# 여러 예외 처리 (IndexError, ValueError, Exception)
nums = [10, 20, 30]

try:
    index = int(input("인덱스 입력: "))
    print("값:", nums[index])

except ValueError:
    print("인덱스는 정수여야 합니다.")

except IndexError:
    print("인덱스 범위를 벗어났습니다.")

except Exception as e:
    print("알 수 없는 오류 발생:", e)




# try–except–else–finally (파일 처리)
try:
    name = input("파일 이름: ")
    f = open(name, "r")
    content = f.read()
    print(content)

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

else:
    print("파일 읽기 성공")

finally:
    try:
        f.close()
    except:
        pass
    print("프로그램 종료")