"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""

# (1) 인자도 없고 리턴값도 없는 함수 만들기
#       리턴값이 없으면 None이 리턴 된다.

# def func():
#     print('확인')
#     return "OK"
#
# print(func())

# (2) 리턴값이 여러 개 가능 => 튜플형으로 넘어옴
# def func(arg1, arg2):
#     return arg1+5, arg2*2
#
# print(func(5,3))
# a, b=func(2, 4)     #unpacking: 튜플형을 쪼갬 다시 공부
# print(a, b)

# (3) 위치인자 (positional argument)
# def func(greeting, name="아무개"):
#     print('{0}!!!!!{1} 님'.format(greeting, name))
# func("헬로우", "홍씨")

# (4) 키워드 인자 (keyword argument)
# func(name="김씨", greeting="반갑수다")

# (5) 매개변수의 기본값 저장하기
# func('올라')

# def func(a, b ,c=100):
#     return a+b+c
# result = func(10,20,30)
# print(result)

# result = func(10,20)    # c=100 적용
# print(result)

# result = func(10)       # 에러
# print(result)

# def buggy(arg, result=[]): #인터프린터 방식으로 함수를 정의한 49line에서 빈리스트 객체(기본값)를 생성(함수를 호출할 때 가 아님)
#     result.append(arg)
#     print(result)

# buggy('A')              # ['A']
# buggy('B')              # ['A', 'B']
# buggy('Z', [1,2,3,4])   # [1,2,3,4,'Z]z
# buggy('가')             # ['A', 'B', '가']


# (6) 위치인자 모으기(*)
'''
1번째와 2번째는 인자가 반드시 들어가고 3번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 4번째 인자부터는 정확히 모른다면?
'''
def func(a, b, c=0, *args):
    hap = a+b+c
    for i in args:  # sum(args)
        hap += i    # hap + sum(args)
    return hap

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다


# (7) 키워드 인자 모으기(**)
# 넘어오는 인자의 값들을 모두 합산하여 값을 리턴하고 출력
def func(i, j, k=100, *args, **kwargs):
    print(kwargs)  # Dictionary형태: {'a': 10, 'b': 20, 'c': 30}
    sum = i+j+k
    for ar in args:
        sum += ar
    for kwargs_val in kwargs.values():
        sum += kwargs_val
    return sum
    # print(args)         # Tuple형태


print(func(10,20))
print(func(1,2,3))
print(func(1,2,3,4,5,6))
print(func(1,2,3,4, a=10, b=20, c=30))


