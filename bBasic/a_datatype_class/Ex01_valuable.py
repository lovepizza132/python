"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 shift + alt + F10

    [도움말] ctrl + q

"""

""" 여러줄 
    주석 """
# 한줄 주석

# print("헬로우")
# print('hello')
#
# print("""안
#          녕""")   # 3개짜리는 개행을 포함
# print('''올
# 라''')
# 실행 : shift + alt + F10
# 주석은 ctrl + /

'''
변수란
    파이션의 모든 자료형은 객체로 취급한다
    a = 7
            7객체를 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# a = 777
# b = 777
# print(a is 777) #True
# print(a is b)   #777


"""
    파이썬 내부적으로 숫자 0~256까지를 미리 메모리에 상주하고 시작해서 
    257 이후의 숫자는 그 이후에 만든다고 함
"""

# 여러개의 변수 선언 용이
a, b = 10, 20
print('a+b=', a+b)  # print에서 문장 연결시 "," 사용 (자바는 '+')

# 변수 값 swap이 매우 간단
b, a = a, b
print('A=', a , 'B=', b)

# del 변수 삭제
del b
print(b)
