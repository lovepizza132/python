"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨 (권장하지 않음)
    - 형변환 권장: str() / int() / float()
"""

# name = input('이름을 입력-> ')
# print('당신의 이름은 {0} 입니다.' .format(name))
# print('당신의 이름은 {} 입니다.' .format(name))
# print('당신의 이름은 %s 입니다.' %(name))

#
# height = input('키를 입력하세요-> ')
# age = input('나이를 입력하세요-> ')
# print('당신의 키는 {0}입니다.'.format(height))
# print('당신의 나이는 {}입니다.'.format(age))
# print('당신의 키와 나이는 {0}, {1}입니다.'.format(height, age))
#eval() 확인
# print('1+2')
# print(eval('1+2'))

#----------------------------------
# 단을 입력받아 구구단을 구하기
# dan = int(input('단 입력-> '))
# for i in range(1, 10): # range(1, 10): 1 ~ (10-1)
#     print('{0}*{1}={2}'.format(dan, i, dan*i))
#-----------------------------------------
# print() 함수
# print('친구'+'안녕') # 문자열 연결 - 친구안녕
# print('친구','안녕') # 컴마(,)로 연결로하면 띄어쓰기가 됨 - 친구 안녕
# print('친구' '안녕') # 아무런 기호가 없어도 연결 됨 (권장하지 않음) - 친구안녕

# print는 자동 개행 됨
# for i in range(1, 6):
#     print(i)

# ln(자동 개행)을 막는 법 - end 사용
# for i in range(1, 6):
#     print(i, end=' ')

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3

import sys
args = sys.argv[1:] # 1부터 끝까지 받겠다.(윗 줄에 1번 ourserver부터 끝까지 받아오겠다.)
print(args[0], '서버에 연결합니다.') # [0]=scott, [1]=tiger