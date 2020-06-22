"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

    *********** 튜플 컨프리헨션은 없습니다.
"""


# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)


#------------------------------------------------
# 리스트 컨프리핸션**********************
print('-'*50)
blist = [n for n in range(1,7)]     # 1~6까지의 수를 뽑고(n) 이를 리스트로 만들겠다.
print('blist1=',blist)

blist = [n**2 for n in range(1,7) ]     
print('blist2=',blist)

blist = [n**2 for n in range(1,7) if n%2==1]     # 순서: 1. for문, 2. if문(for문의 값으로) 3. n**2 실행
print('blist3=',blist)

rows = range(1,4)   # 1,2,3
cols = range(1,3)   # 1,2
dlist = [(r,c) for r in rows for c in cols]     # for문 2개 사용 가능 개이득
print(dlist)
#-------------------------------------------
# 딕셔러니 컨프리핸션 {key: value}
data = (2,3,4)
a = { x:x**2 for x in data}
print(a)

word ='love lol'
wcnt = { letter: word.count(letter) for letter in word} # count는 공백까지 세주는 섬세함을 지님
                                                        # 중복된 key는 생략
print(wcnt)

#------------------------------------------------
# 셋 컨프리핸션

# 1부터 6까지 수 중에서 짝수만 Set에 요소로 만들기
# data2 = range(1,7)
data2 = [1,2,3,4,5,4,2,6]           # set은 중복값x - [1,2,3,4,5,6]으로 적용, 순서 no상관
set = { n for n in data2 if n%2 ==0}
print(set)


# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
data2 = [1,2,3,4,5,4,2,6]
set = ( n for n in data2 if n%2 ==0)
print(set)              #   <generator object <genexpr> at 0x000001D011B71D48>
print(type(set))        # <class 'generator'> : 요소를 추출하면서 처리 & 저장하지 않음
print(list(set))        # [2, 4, 4, 2, 6] 나옴
print(list(set))        # [] 나옴