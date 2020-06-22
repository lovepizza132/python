import csv
# csv는 텍스트이지만 엑셀파일 느낌?
# 1. 리스트의 데이타를 csv로 저장하기
# data = [[1, '감', '책임'], [2, '주', '연구원']]
# with open('./data/imsi.csv', 'w', encoding='utf-8') as f:
#     cout = csv.writer(f)
#     cout.writerows(data)

# 2. csv 파일을 읽어서 리스트 변수에 저장하기
data =[]
with open('./data/imsi.csv', 'r', encoding='utf-8') as f:
    cin = csv.reader(f)
    data = [row for row in cin if row]      # 개행되어서 빈 배열이 나옴 따라서 row값 중에 none이 있음 if row를 써서 빈 값은 false로 거름
    
print(data)