'''
pin = '880122-1234567'
birthday='홍길동님 생년월일 : '+ pin[0:6]
if pin[7:8]=='3' or pin[7:8]=='1':
    gender='성별 : 남자'
elif pin[7:8]=='2' or pin[7:8]=='4':
    gender='성별 : 여자'
print(birthday)
print(gender)
'''
'''
a = [1,3,5,4,2]
reverse =a[::-1]
a = reverse
print(a)
'''
'''
a = ['독도는','대한민국의','아름다운','섬입니다']
result = ' '.join(a)
print( result )
'''
'''
a = (1,2,3)
a = a + (4, )
print(a)
'''
'''
a = b = [1,2,3]
a[1] = 4
print(b)
'''
'''
star = 0
while star<5:
    star += 1
    print('*'*star)
'''
'''
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50, 60, 70, 80, 90]
midterm_score = [kor_score, math_score, eng_score]

print("국어 총점: ",sum(kor_score))
print("수학 총점: ", sum(math_score))
print("영어 총점: ", sum(eng_score))

print("국어 평균: ", sum(kor_score)/5)
print("수학 평균: ", sum(math_score)/5)
print("영어 평균: ", sum(eng_score)/5)
'''
'''
life = {
    'animal': {
        'cats': ('Kim', 'Lee', 'Choi'),
        'octopi': [],
        'emus': []
    },
    'plants': {

    },
    'other': {

    }
}

print(life['Venus']['mean_radius'])  # 6051.8
'''
'''
class Calculator(list):
    def sum(list):
        return print(sum(list))
    def avg(list):
        return print(sum(list)/len(list))


cal = Calculator([1,2,3,4,5])
cal.sum()
cal.avg()
'''
'''
kor_score=int(input('국어점수를 입력->'))
eng_score=int(input('영어점수를 입력->'))
math_score=int(input('수학점수를 입력->'))
print((kor_score + eng_score + math_score)/3)
'''

'''
def product(sca, vac):
    list=[]
    for i in vac:
        list+=[i*sca]
    print(list)

product( 5, [1,2,3,4] )
'''

# def matrix_add(matrix_x, matrix_y):
#     a, b= list(zip(matrix_x, matrix_y))
#     result = []
#     a_first = 0
#     a_second = 0
#     b_first = 0
#     b_second = 0
#     for i in a:
#         a_first += i[0]
#         a_second += i[1]
#     result.append([a_first]+[a_second])
#     for i in b:
#         b_first += i[0]
#         b_second += i[1]
#     result.append([b_first]+[b_second])
#     print(result)



# def matrix_add(matrix_x, matrix_y):
#     result =[]
#     for a, b in zip(matrix_x, matrix_y):
#         list = []
#         print(a, b)
#         for t in zip(a, b):
#             print(t)
#             list.append(sum(t))
#         print(list)
#         result.append(list)
#         print(result)
#
# matrix_x = [[2,5],[2,1]]
# matrix_y = [[2,4],[5,3]]
# matrix_add ( matrix_x, matrix_y )
# [[4,9],[7,4]]



def vector_sub(*vector_sub_values):
    a = 0
    b = 0
    for idx, i in enumerate(*vector_sub_values):
        if idx==0:
            a+=i[0]
            b+=i[1]
        else:
            a-=i[0]
            b-=i[1]
    return ([a, b])
#print( vector_sub([[1,3],[2,4]]) )
#[-1,-1]
print( vector_sub([[1,5],[10,4],[4,7]]) )
#[-13,-6]



