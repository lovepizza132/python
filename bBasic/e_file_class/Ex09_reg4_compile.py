'''
    # compile
     - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
     - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능
'''

import re


#----------------------------------------
webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',       #file transper protocal
        'http:://www.test.com',     #
       'htp://www.test.com',        #
       'http://www.google.com',
       'https://www.homepage.com.'] #http://로 시작, 마지막에 .으로 끝나면 안됨

web_reg = re.compile('^https?://[\w.]+\w+$')    #맞다 틀리다를 감지해주는 정규식
result = list(map(lambda w:web_reg.search(w)!=None, webs))   #map(함수, 인자-리스트) / 여기 search는 문자열 search다
# s? -> s가 0번 또는 1번 있을 수 있다.
# [\w.]+ -> 모든 문자 숫자 _ 와 . 이 한개 이상(+) 들어갈 수 있다.
# \w+$ -> 모든 문자가 숫자 _ 가 한개 이상(+) 들어가면서 문장이 끝($)난다.
print(result)