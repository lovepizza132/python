"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path


# (1) 해당 경로와 하위 목록들 확인
# pathlib.Path import를 안함
# p =Path('C:\Windows')
p = Path('..')
print(p)
print(p.resolve())      #경로를 절대경로로 보여줌

#------------하위디렉토리 찾는 법----------------
# test=[]
# for x in p.iterdir():      # iterdir()
#     if x.is_dir():         # is_dir(): 디렉토리인지 확인
#         test.append(x)
# print("부모 디렉토리의 하위 디렉토리 목록: ", test)
test = [x for x in p.iterdir() if x.is_dir()]   # list comprehension 사용
print('하위디렉토리 목록 확인',test)

# 하위 파일 찾기
test = [x for x in p.iterdir() if x.is_file()]   # list comprehension 사용
print('하위 파일 찾기', test)

a = list(p.glob('**/a_datatype_class/*.py'))    # ** 추가 시: 하위 자손들 다 찾아옴
print('glob함수 사용:', a)
#----------------------------------------------