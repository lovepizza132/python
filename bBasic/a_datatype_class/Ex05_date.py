"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""
from datetime import date # date 년, 월, 일 만
today = date.today()
print(today)

# 년, 월, 일
print('년도: ', today.year)
print('월: ', today.month)
print('일: ', today.day)

# 날짜계산
from datetime import timedelta
print('어제: ', today+timedelta(days=-1))
print('7일 전: ', today+timedelta(days=-7))
print('10일 후: ', today+timedelta(days=+10))

# 날짜와 문자열 변환
from datetime import datetime # datetime년, 월, 일, 시, 분, 초 까지
today = datetime.today()
print(today)
print(today.strftime('%Y/%m/%d %H:%M'))

naljja = '2020-08-08 12:12:35'
mydate = datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)