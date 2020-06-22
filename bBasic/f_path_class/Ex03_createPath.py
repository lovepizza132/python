
from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
print(Path.cwd())   # 현재 경로: 리눅스는 pwd
print(Path.home())  # 홈 경로

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
p = Path('Ex03_createPath.py')
print(p.stat().st_ctime)        #stat(): 파일의 상태 값을 알 수 있는 함수
                                # st_ctime: 1970.1.1 0시 0분 0초 부터

from datetime import datetime
z = datetime.fromtimestamp(p.stat().st_ctime)   # 우리 시간 때로 바꿔 줌
print(z)

# ------------------------------------------------
# 3. 디렉토리 생성
# p1 = Path('imsi')
# p1.mkdir()

# p2 = Path('imsi')   # 이미 있는 파일로 만들 수 없음
# p2.mkdir(exist_ok=True) # exist_ok=True: 이미 있어도 덮어서 만들어 주는 함수
#
# p3 = Path('temp2/imsi2/test2')  # test2 앞에 디렉토리(부모)는 없기에 에러 발생
# p3.mkdir(parents=True)          # parents=True: 부모 디렉토리까지 한번에 만들기 위해


# ------------------------------------------------
# 4. 파일 생성
# f = open('imsi/1.txt', 'w', encoding='utf-8')   #write모드로 여는 경우 파일이 존재하지 않을 경우 파일 생성
# f.write('')
# f.close()
#
# f2 = Path('imsi/2.txt')
# f2.touch()

# ------------------------------------------------
#  5. 경로 제거
# f = Path('temp2/imsi2/test2')
f = Path('imsi')    # 지울 때, 폴더 안이 비어 있지 않으면 에러 발생
f.rmdir()
