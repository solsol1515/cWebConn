"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

''' 자바인 경우
class Sample{
    String data = "Hello";          # 고정적으로 초기화 (초기값 지정)
    String name;
    Sample(String name){            # 생성자 함수 생성
        this.name = name;
    }  
}
Sample s = new Sample("홍길동");
'''

class Sample:
    data = 'Hello'
    def __init__(self, name, age):        # 다른 랭귀지에서의 생성자 함수
        self.name = name                  # this.name = name
        self.age  = age                   # this.age = age
        print('__init__ 호출')
    def __del__(self):                    # 객체 닫기 close
        print('__del__호출')

s = Sample('홍길동', 55)
print(s.data)                             # Hello
print(s.name)                             # 홍길동
print(s.age)                              # 55
del s                                     # s의 메모리 삭제
print('-'*20)



"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
    
 [자바인 경우]
 class Sample{
    int a; static int b;
 }
 Sample s1= new Sample'()
 Sample s2 = new Sample()'
 Sample s3 = new Sample()'
 
 
"""
class Book:
    cnt = 0
    def __init__(self, title):
        self.title = title
        self.cnt += 1

    def output(self):
        pass

    @classmethod
    def output2(cls):           # static?
        cls.cnt += 1

b1 = Book('행복?')
b2 = Book('먹고 살자')
Book.output2()
Book.output2()
print(Book.cnt)




'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:
    def move(self):
        print('동물은 움직인다')

class Human(Animal):    # Animal class : 부모클래스 Human : 자식 클래스
    def move(self):
        print('인간은 두 발로 걷는다')

class Wolf(Animal):
    def move(self):     # move() 오버라이딩
        print('늑대는 네 발로 달린다')

class Werewolf(Human, Wolf):
    pass

ww = Werewolf()         # Werewolf 객체 생성
ww.move()               # 다중 상속일 경우, 에러 발생하지는 않지만, 먼저 상속받은 것으로 처리함
                        # (Human, Wolf) 인간은 두 발로 걷는다 출력

h = Human()             # Human 객체 생성
h.move()                # 동물은 움직인다 출력됨
w = Wolf()              # Wolf 객체 생성
w.move()                # 늑대는 네 발로 달린다 출력됨
