import shutil
from pathlib import Path
# shutil.rmtree('imsi')   # 해당 디렉토리가 비어 있지 않아도 바로 지워 줌

# shutil.copy('Ex00.txt', Path('temp2/imsi2/2copy.txt'))

shutil.copytree('temp2', '../copytemp')     # copytree: temp2 파일을 ../copytemp위치에 (부모 디렉토리에 copytemp이름의 파일로) 카피 함