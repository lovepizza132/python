def sum(a, b):
    if type(a) != type(b):
        print("자료형이 달라서 계산 불가!")
        return  # 리턴하는 자료형이 없어 None 리턴
    else:
        return a+b
