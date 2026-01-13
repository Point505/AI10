### 주요 개념 정리

# 패키지란 
"""

모듈의 집합 (모튤: 클래스 함수 메서드 속성을 모아 놓은 집합 )

파이선에서 모듈은 하나의 .py 파일이다.

"""
# 디렉터리

"""
디렉토리는 여러 파일이나 하위 디렉토리를 담는 집합체이며, 

윈도우에서는 폴더라고 부름

각 디렉토리의 고유한 위치는 Path

"""
# 모듈안에 다른 모듈을 미리  import 하는 경우

"""
미리 import 해놓으면  디렉터리 하나만 호출해도 다른 곳에 있는 함수를 사용할 수 있음

"""

## 💡 학습하면서 느낀 점


"""


"""

## ❓ 질문 및 궁금한 점








"""
game/ 
    __init__.py
    
    sound/
        __init__.py
        echo.py
        wav.py
        
    graphic/
        __init__.py
        screen.py
        render.py
        
    play/
        __init__.py
        run.py
        test.py
        
        
        
game은 루트 디렉토라
sound, graphic,play 는 서브 디렉토리

"""

# 예외처리 실습


"""
"""

"""
# render.py , render 모듈에 들어있는 echo_test  함수
def echo_test():
    print("render")

"""

#디렉터리에서 모듈 호출
"""
import game.sound.echo
game.sound.ehco.echo_test()
# game 하위 디렉터리 sound 안에 있는 echo 모듈안에 있는 echo_test() 함수 호출


from game.sound import echo
echo.echo_test()
#game.sound 디렉터리에서 echo 모듈호춣

from game.souned.echo import echo_test
echo_test()
# import 에 들어간 단계부터 사용할 함수까지 사용

"""

# __init__.py의 용도

"""
__init__.py는 디렉터리가 패키지의 일부임을 알려주는 역활을 한다.
만약 없다면 패키지로 인식하지 않는다.

"""



#패키지 변수 및 함수 정의

"""

# __init__.py // game 디렉터리 에 들어있는 모듈

VERSION = 3.5

def print_version_info():

    print(f"The Version of this game is {VERSION}.")
    
import game

print(game.VERSION) # __init__.py 안에 있는 변수를 호출
game.print_version_info()# 안에 있는 함수를 호출

"""

# 모듈안에 다른 모듈을 미리  import 하는 경우
"""
# game에 모듈 __init__.py

from .graphic.render import renfer_test

VERSION =3.5

def print_version_info():

    print(f"The version of this game is {VERSION}.")


import game # game 모듈 하나만 가져와도 미리 import를 했기 때문에  graphic 디렉터리 안에 있는 render 모듈에 render_test() 함수를 사용할 수 있다.

game.render_test()


"""


