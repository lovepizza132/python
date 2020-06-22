"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None


# (1) 숫자에 의한 조건------------------------
a = -1
if a:
    print('True') #
else:
    print('False')

if not i:
    print('True2') #
else:
    print('False2')

# (2) 논리 연산자 이용한 조건-------------------------------
a = 10
b = -1
if a and b:
    print('True3')
if a or b:
    print('True4')

# 정리필요
# short-circuit logic 적용??
print(a and b)  # -1 and는 a가 False면 a를 반환하고, a가 True면 b값을 반환
                # 뒤에 변수까지 확인해야하고 뒤에 값에 따라 결과값이 달라진다 즉 뒤에 것이 중요하다 판단

print(a or b)   # 10 or는 a가 True면 a가 반환되고, a가 False면 b값을 반환
                # 앞에것만 취급해도 문제 음슴ㅋ


# (3) find(): 찾으면 해당하는 인덱스를 반환하고 못 찾으면 -1을 반환

word='korea'
if word.find('k'):         # 0 -> False
    print('1>'+ word)      # False라 출력 안됨

if word.find('k')>-1:      # >-1이라는 연산을 넣어준다. find는 해당하는 인덱스를 못찾으면 -1을 반환하기 때문
    print('1>'+ word)      # True라 출력 됨

if word.find('z'):         # -1 -> True
    print('2>'+word)       # True라 출력 됨

if word.find('z')>-1:      # >-1이라는 연산을 넣어준다. find는 해당하는 인덱스를 못찾으면 -1을 반환하기 때문
    print('2>'+word)       # False라 출력 안됨


#-----------------------------------------------------------------------------