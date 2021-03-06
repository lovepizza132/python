"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')
# 리스트 t = []
# 셋 t = {}
t = (1,2,3)
print(t[0])

# t = 1,2,3 # 권장하지 않음 나중에 이게 튜플인지 모름
# print(t)

# 빈 튜플 생성
# t = ()
# t = tuple()

# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0;  # 블럭이 생기면서 실행 안됨
# del t[1]   # 에러 발생
# del t      # 정상: 객체는 삭제 가능(튜플의 요소 삭제, 수정 불가)
print('------------------- 2 -----------------')

# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')
t3 =(1)     # ******* 튜플이 아님
print(t3)   # 연산자 우선순위 임=> (1+2) -2에서의 ()와 같음
print(type(t3))

t4 = (1,)   # 튜플(한개짜리를 만들 때는 뒤에 , 붙이기
print(t4)
print(type(t4))
# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')
t2 = (9,8,7,6,5,4)
print(t2[1])     # 튜플을 얻어올 때는 list와 똑 같이
print(t2[1:])
print(t + t2)
print(t*2)

# (5) 튜플 요소 풀기
print('------------------- 5 -----------------')
t5 = ('a', 'b', 'c')
n1, n2, n3 = t5
print(n1, n2, n3)
print(n1+ n2+ n3)