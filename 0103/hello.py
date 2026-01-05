


# while문 반복 

"""TreeHit = 0

while TreeHit < 10:
    TreeHit+= 1
    
    print("횟수: %d "TreeHit)
    
    if TreeHit == 10:
        print("End")
    else: 
        continue
    """
    
    
# while문 탈출
"""
coffe = 100
money = 100

while money:
    
    money -= coffe
   
    if(money == 0):
        print("잔고 없음")
         
    
    else:
       continue
    
    
    """
        
"""# while + if + else, f 포맷

count = 0

while count <5:
        
 if count == 2:
     break
 print(f"카운트:{count}")  
 count+=1
 
else:
    print("while 문이 정상종료 되었습니다.")
"""






""" for """





"""
Test_List=['one','two','three']
for i in Test_List:
    print(i)"""
    

"""a =[(1,2),(3,4),(5,6)] # 2X3 배열인줄 알았으나 아니였음

for (first,last) in a: #각각의 변수에 숫자를 부여
    print(first +last)
"""    
    
"""    
#점수를 비교
mark = [90,25,67,45,80]

number = 0
for marks in mark:
    number = number +1
    if marks >= 60:
        print(f"{number}번째 학생은 합격 입니다.")
    else:
        print(f"{number}번째 학생은 불합격 입니다.")"""