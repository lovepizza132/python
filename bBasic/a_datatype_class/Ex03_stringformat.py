
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100))   #json 형식 0:d
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴

msg = '{name}님 오늘은 뭐 먹어요? {menu} 어떠세요?'
print(msg.format(name='짝꿍', menu='짬뽕'))



# [참고] http://pyformat.info
# [나만참고] http://blog.naver.com/PostView.nhn?blogId=ksg97031&logNo=221126216595&parentCategoryNo=&categoryNo=172&viewDate=&isShowPopularPosts=true&from=search

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456


print('%s 님은 %d 세 이시고 키는 %.3f 입니다.' %(name, age, height)) # %10.3f 전체 10개 중 소수점 3자리


#--------------------------------------------------
# 실수인 경우
su = 99.999
print('내가 좋아하는 수: ', su)
print('내가 좋아하는 수: {:.2f}'.format(su))    # 실수일 경우 반올림 된다 주의
print('내가 좋아하는 수: %.2f'%su)             # 실수일 경우 반올림 된다 주의

a = 11
b = 9
print('a'+'b')