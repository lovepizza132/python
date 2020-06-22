"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

# class Simple:
#     data = "Hello"              # 멤버변수 선언1
#     def __init__(self):         # 파이썬의 생성자 함수
#         self.age = 38           # 멤버변수 선언2 (나중에 1, 2번은 차이가 발생)
#         self.name = '홍길동'
#         print('__init__ 호출')
#
#     def __del__(self):          # 소멸자(생성자의 반대개념) : 제일 마지막에 호출 or 직접 호출할 때
#         print('__del__ 호출')
#
# s = Simple()
# print(s.data)
# print(s.age)
# print(s.name)
# print(dir(s))

class Book:
    cnt=0                         # 클래스 변수
    title=''
    def __init__(self, title):
        self.title= title         # 인스턴스 변수

    def output(self):
        print('제목: ', self.title)
        self.cnt += 1
        print('1> 총 갯수 ', self.cnt)

    @staticmethod
    def output2():
        pass    # 아무런 일도 하지 않겠다는 의미
        # print('제목: ', self.title)
        # self.cnt += 1
        # print('2> 총 갯수 ', self.cnt)

    @classmethod    #self 사용 불가능 대신 cls 사용 가능
    def output3(cls):
        print('제목: ', cls.title)
        cls.cnt += 1
        print('1> 총 갯수 ', cls.cnt)
#
b = Book('자바란 무엇인가?')
z = Book('파이썬 만만세!')
#
# Book.output2()
#
b.output()
z.output()
b.output3()
z.output3()
Book.output3()

class Animal:
    def move(self):
        print('동물은 움직인다')

class Wolf(Animal):     # 부모 클래스 상속
    def move(self):     # overload
        print('늑대는 4발로 달린다')

class Human(Animal):
    def move(self):
        print('사람은 2발로 걷는다')

class WareWolf(Wolf, Human):    # 다중 상속 가능(부모 중 앞에 있는 애의 메소드를 찾아감)
    def move(self):             # overload Wolf, Human(상속받는) 클래스에서 동일한 메소드가 있어도 에러x
        super().move()          # 1) 에러 2) Wolf 3) Human 4) Animal -> 먼저 상속받은 클래스의 메소드를 오버로딩 함 답: 2번
        print("늑대인간은 2발+4발로 달린다")

w = WareWolf()  # 파이썬의 클래스 생성 new를 안쓰는 참신함
w.move()






"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""







'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''


