
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
   print(entry)

for entry in e.items(): # dictionary한테는 items()를 사용해 key, value(값) 모두 출력 가능 = Tuple형으로 출력-ex('k', 5)
   print(entry)
   print('key=', entry[0], 'value', entry[1])


# [연습1] 1~10까지의 합 출력
hap = 0
for i in range(1, 11):
    hap += i
print('총 합', hap)

# [연습2] 1~10까지의 홀수의 합 출력
hap2 = 0
for i in range(1, 11):
    if i%2 == 1:
      hap2 += i
print('홀수의 총 합', hap2)

# [연습3] 2단부터 9단까지 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(i,'*',j,'=',i*j)
        print('{0}*{1}={2}'.format(i,j,i*j))



# =========================================================
# while

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break

"""
while(true){
    if(a==1)
        break;
}
"""

a = ['x', 'y', 'z']
while a:
    data = a.pop()          # 마치 stack 구조처럼 pop사용
    print(data)

print('end')                # z,y,x가 빠져나가고 빈 리스트가 되면 반복문에서 빠져나와 'end' 출력


a = ['x', 'y', 'z']
while a:
    data = a.pop()          # 마치 stack 구조처럼 pop사용
    print(data)
    if data == 'y':         # y일 때 break했기 때문에 else까지 가지 않음
        break
else:                       # else: 는 반복문 뒤에 위치, 반복하는 조건에 만족하지 않을 때만(False) 실행
    print('end')

"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
