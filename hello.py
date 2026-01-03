


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
        
# while + if + else, f 포맷

count = 0

while count <5:
        
 if count == 2:
     break
 print(f"카운트:{count}")  
 count+=1
 
else:
    print("while 문이 정상종료 되었습니다.")
