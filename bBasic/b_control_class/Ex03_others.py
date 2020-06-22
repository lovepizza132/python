msg = '밥먹자'                # 문자열
li = ['a','b','c']        # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = dict(k=5, j=6, i=7)       # 딕셔너리
# id = {k=5, j=6, i=7}

#-----------------------------------------
# (1) unpacking: 각 요소를 분해
c1, c2, c3 = di   # 문자열 뿐만 아니라, 리스트, 튜플, 딕셔너리 가능
print(c1, c2, c3)

c1, c2, c3 = di.values()
print(c1, c2, c3)

#------------------------------------------
# (2) 리스트의 요소가 튜플인 경우 기억하자*************
alist = [(1,2), (3,4), (5,6)]
for (a, b) in alist:
    print(a,b)

#------------------------------------------
# (3) enumerate()함수: 어떤 요소만 뙇 추출하는 함수
user_list = ['개발자', '코더', '전문가', '분석가']
for idx, user in enumerate(user_list):
    print(idx, ':', user)

#------------------------------------------
# (4) zip()함수: 여러 시퀀스를 순회하는 함수
days = ['월', '화', '수']
doit = ['잠자기', '놀기', '밥먹기', '공부']
print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

mon =[6, 7, 8]
print(list(zip(days, doit, mon)))   # list형태라면 zip으로 3개 이상 순회 가능
print(dict(zip(days, doit, mon)))   # 3개 이상부터는 dict는 에러(key-value 형태가 안됨)



