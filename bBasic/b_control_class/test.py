'''
[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 출력 결과 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 출력 결과 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 출력 결과 ]
        print(count_vowel("pythonian"))
'''


with open("i_have_a_dream.txt", "r") as f:
    contents = f.read()
    print(contents)

# num = 0
# def is_prime_number(num):
#     isSosu = False
#     for i in range(2, num):
#         if num%i==0:
#             return isSosu
#     isSosu=True
#     return isSosu
# print(is_prime_number(9))
# print(is_prime_number(7))


# list = []
# def even_filter(list):
#     even = []
#     for i in list:
#         if i%2 == 0:
#             even.append(i)
#     return even
#
# print(even_filter([1, 2, 4, 5, 8, 9, 10]))