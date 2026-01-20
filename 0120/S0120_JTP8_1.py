## 주요 개념 정리
# 게시판의 페이지 수를 구하는 것이 페이징
# 총 페이지수 = ( 총 게시물 수 / 한 페이지당 보여줄 개수) + 1
# 아스키 코드로는 해결이 되지 않아 유니코드를 만듬
# 유니코드 문자열은 인코딩 하지 않고는 파일에 적거나 다른 시스템으로 전송할 수 없다.


## 💡 학습하면서 느낀 점




## ❓ 질문 및 궁금한 점

"""

# 게시판 페이징 하기 


def get_total_page(m,n):
    return m//n+1


print(get_total_page(5,10))
# m = 게시물 수 , n = 한 페이지에 들어갈 게시물 수





def get_total_page(m,n):
    
    if m%n==0:
        return m//n
    else:
        return m//n + 1
    

print(get_total_page(10,10)) # 1



"""