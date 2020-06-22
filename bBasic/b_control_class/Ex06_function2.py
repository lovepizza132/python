
# [추가] 함수도 객체이다
def case1():
    print('case-1가')

def case2():
    print('case-2나')

def case3():
    print('case-3다')

f={'case1' : case1, 'case2' : case2, 'case3' : case3}
a = 'case1'
f[a]()

#---------------------------------------
# 글로벌 변수와 지역변수

# if문 while문 제어문 안쪽에 있는 변수는 글로벌 변수이다.
# if 10000:
#     r =10
# print(r)

temp ='글로벌'

def funtc():
    # print('0>', temp)     #에러: 변수가 함수 안에 있으면 그 변수를 따른다. 그렇기에 변수보다 앞서 있으면 참조를 못해서 에러 발생
    global temp             #global 선언 시 함수 안이라도 밖의 글로벌 변수를 참조 함
    temp = '지역'
    print('1>', temp)       #지역

funtc()
print('2>', temp)           #글로벌

'''
#----------------------------------------------
# 람다함수 - 한번 사용하고 버리는 함수
# 파이션에서는 람다함수를 한 줄로 작성???

    파이썬 3.x부터는 람다를 권장하지 않는다고.
    몇몇 개발자들이 람다함수 사용시 직관적이지 않다는 이유라는데
    
    종종 사용됨
'''

def f(x,y):
    return  x+y
print(f(2,3))

la = lambda x, y : x+y      #lamda 함수: lamda 매개변수 : return값
print(la(2,3))

#-----------------------------------------------------------
"""  맵리듀스
    (1) map()
         ` 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
         ` 형식 : map(함수명, 리스트형식의 입력값)
         ` 파이썬 3.x에서는 list(map(calc, ex)) 반드시 list를 붙여야 리스트 형식으로 반환된다
           파이썬 2.x에서는 list 없이도 리스트 형식으로 반환
    (2) reduce()
         ` 리스트 같은 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수    
    
    파이썬 2.x에서는 많이 사용하던 함수이지만, 최근 문법의 복잡성으로 권장하지 않는 추세란다.
"""

def calc(x):
    return x*2

ex=[1,2,3,4,5]
# ex 리스트의 각각의 요소를 뽑아서 calc()의 인자로 보낸 리턴값들을 다시 리스트로 저장하기
# result = [2,4,6,8,10]
result =[]
for n in ex:
    re = calc(n)
    result.append(re)
print(result)


result = list(map(calc, ex))
print(result)
# print('calc(ex)= ', calc(ex))     # 틀린 답: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]



# 차례대로(1) 함수를 적용(2)하여 모든 값을 통합(3)
from functools import reduce

ex = range(1, 5)        #ex = [1,2,3,4]
def f(x, y):
    print('x=', x)
    print('y=', y)
    print(x*y)
    return x*y
print(reduce(f, ex))    # 1*2*3*4 = 24

# f 함수 = lambda x,y : x*y 이걸 대입
print(reduce(lambda x,y  : x*y , range(1,5)))



