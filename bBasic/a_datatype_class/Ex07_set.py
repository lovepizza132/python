# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다


s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
print(s)

s3 = {3,4,5,6}          # set = 집합

print(s3.union(s))  # 합집합 = print(s|s3)
print(s3.intersection(s))   #교집합 = print(s&s3)

print(s&s3)
print(s|s3)
print(s-s3) # 차집합
print(s3-s)