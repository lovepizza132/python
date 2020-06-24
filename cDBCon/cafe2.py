from tkinter import *
import random
import time


# --------------부가세를 계산해 주는 함수입니다.-----------------------------
def cal_tax(totalPrice):
    tax = totalPrice / 11
    return int(tax)


def cal_productPrice(totalPrice):
    productPrice = totalPrice * 10 / 11
    return int(productPrice)


# -------랜덤주문을 눌렀을 때 제품을 살지 안 살지 정해주는 함수입니다.------------------------------------------
def random_order_choice(price):
    random_choice = random.randint(0, 1) * price
    return random_choice


# ----------버튼을 눌렀을 때 카운트가 올라가는 함수입니다.---------------------------------------
def update_count(self):
    self.bttn = Button(self)

    self.bttn_clicks += 1

    return str(self.bttn_clicks)


# -----------정산 버튼을 눌렀을 때 할 행동들을 기술한 함수입니다------------------------------------
def sum1(list1):
    n = 0
    now = time.localtime()

    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    sum1 = sum(list1)
    print("\n" * 100)
    print("행복햄버거 강남대점  T:010-9971-7132")
    print("경기도 용인시 기흥구 강남로 40")
    print("감사합니다. 또 이용해주세요.")
    print("[정  산]".center(50))
    print("정산일:", s)
    print("판매담당:0001/김지섭".ljust(13), "               거래번호:", update_count(orderbutton))
    print("*" * 50)
    print("  청 구 액".ljust(10) + " 판 매 시 간".center(8) + "주문코드".rjust(15))
    print("*" * 50)
    for i in list2:
        n += 1
        print(n, ":", i)
    print("*" * 50)
    print("총 매출:", sum1)


# -----------정산버튼을 눌렀을 때 오류가 생겨서 임시로 만든 함수입니다------------------
def sum_orderlist():
    sum1(list1)


# -------------------주문완료 버튼을 눌렀을 때의 행동을 기술한 함수입니다---------------------------
def ordersuccess():
    menulist = [("햄버거    ", 3000, e3.get()), ("피자      ", 5000, e4.get()), ("치킨      ", 7000, e5.get()),
                ("냉면      ", 1500, e6.get()), ("도시락    ", 2500, e7.get()), ("치킨부리또", 3000, e8.get()),
                ("아이스크림", 500, e9.get())]

    ordersum = 0

    if e11.get() == "김지섭":

        now = time.localtime()

        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        recept_price="  제 품 명".ljust(10) + "   단가      수량".center(8) + "금 액".rjust(15)
        i = 0
        print("\n" * 100)
        print("업체 이름")
        print("업체주소")
        print("감사합니다. 또 이용해주세요.")
        print("[판  매]".center(50))
        print("거래일:", s)
        print("판매담당:0001/담당자".ljust(13), "               거래번호:", update_count(orderbutton))
        print("*" * 50)
        print(recept_price.rjust(50))
        print("*" * 50)

        for menuname, price, howmany in menulist:

            howmany = int(howmany)

            ordersum = (price * howmany) + ordersum

            if howmany > 0:
                prhow = price * howmany
                howmany = str(howmany)
                price = str(price)
                prhow = str(prhow)
                print(menuname + price.rjust(10) + howmany.rjust(9) + prhow.rjust(18))

        print("*" * 50)

        sale = int(ordersum - ordersum * 0.7)
        sale = str(sale)
        ordersum = int(ordersum)
        list1.append(int(ordersum * 0.7))
        a = random.randint(100000000000000000, 999999999999999999)
        list2.append(str(int(ordersum * 0.7)) + "  " + s + "  " + str(a))

        print("총 합 계", str(ordersum).rjust(13), "할    인", sale.rjust(16))
        print("과세금액", str(cal_productPrice(int(ordersum * 0.7))).rjust(13), "부가세액",
              str(cal_tax(int(ordersum * 0.7))).rjust(16))
        print("청 구 액", str(int(ordersum * 0.7)).rjust(13), "받 은 돈", str(int(ordersum * 0.7)).rjust(16))
        print("*" * 50)
        print("          주문코드:", random.randint(100000000000000000, 999999999999999999))



    else:

        now = time.localtime()

        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        i = 0
        print("\n" * 100)
        print("업체이름")
        print("업체주소")
        print("감사합니다. 또 이용해주세요.")
        print("[판  매]".center(50))
        print("거래일:", s)
        print("판매담당:0001/담당자".ljust(13), "                  거래번호:", update_count(orderbutton))
        print("*" * 50)
        print("  제 품 명".ljust(10) + "   단가      수량".center(8) + "금 액".rjust(15))
        print("*" * 50)

        for menuname, price, howmany in menulist:

            howmany = int(howmany)

            ordersum = (price * howmany) + ordersum

            if howmany > 0:
                prhow = price * howmany
                howmany = str(howmany)
                price = str(price)
                prhow = str(prhow)
                print(menuname + price.rjust(10) + howmany.rjust(9) + prhow.rjust(18))

        print("*" * 50)
        sale = 0
        sale = str(sale)
        ordersum = int(ordersum)
        list1.append(int(ordersum))

        a = random.randint(100000000000000000, 999999999999999999)
        list2.append(str(int(ordersum)) + "  " + s + "  " + str(a))

        print("총 합 계", str(ordersum).rjust(13), "할    인", sale.rjust(16))
        print("과세금액", str(cal_productPrice(int(ordersum))).rjust(13), "부가세액", str(cal_tax(int(ordersum))).rjust(16))
        print("청 구 액", str(ordersum).rjust(13), "받 은 돈", str(ordersum).rjust(16))
        print("*" * 50)
        print("          주문코드:", a)


# ----------랜덤 주문 버튼을 눌렀을 때의 행동을 기술한 함수입니다--------------------------
def randomorderbutton():
    randombutton["text"] = "★랜덤주문완료★"

    e3get = random_order_choice(3000)
    e4get = random_order_choice(5000)
    e5get = random_order_choice(7000)
    e6get = random_order_choice(1500)
    e7get = random_order_choice(2500)
    e8get = random_order_choice(3000)
    e9get = random_order_choice(500)

    pricelist = [e3get, e4get, e5get, e6get, e7get, e8get, e9get]

    menulist = [("햄버거    ", 3000, e3get), ("피자      ", 5000, e4get), ("치킨      ", 7000, e5get),
                ("냉면      ", 1500, e6get), ("도시락    ", 2500, e7get), ("치킨부리또", 3000, e8get), ("아이스크림", 500, e9get)]

    ordersum = 0

    for i in pricelist:
        ordersum += i

    if e11.get() == "김지섭":

        ordersum = ordersum * 0.7

        now = time.localtime()

        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        print("\n" * 100)
        print("업체이름")
        print("업체주소")
        print("감사합니다. 또 이용해주세요.")
        print("[판  매]".center(50))
        print("거래일:", s)
        print("판매담당:0001/담당자".ljust(13), "               거래번호:", update_count(orderbutton))
        print("*" * 50)
        print("  제 품 명".ljust(10) + "   단가      수량".center(8) + "금 액".rjust(15))
        print("*" * 50)

        if ordersum > 0:

            for menuname, price, howmany in menulist:
                if howmany > 0:
                    prhow = price * 1
                    howmany = str(howmany)
                    price = str(price)
                    prhow = str(prhow)
                    print(menuname + price.rjust(10) + "1".rjust(9) + prhow.rjust(18))

            print("*" * 50)
            sale = int(ordersum - ordersum * 0.7)
            sale = str(sale)
            ordersum = int(ordersum)

            list1.append(int(ordersum * 0.7))
            a = random.randint(100000000000000000, 999999999999999999)
            list2.append(str(int(ordersum * 0.7)) + "  " + s + "  " + str(a))

            print("총 합 계", str(ordersum).rjust(13), "할    인", sale.rjust(16))
            print("과세금액", str(cal_productPrice(int(ordersum * 0.7))).rjust(13), "부가세액",
                  str(cal_tax(int(ordersum * 0.7))).rjust(16))
            print("청 구 액", str(int(ordersum * 0.7)).rjust(13), "받 은 돈", str(int(ordersum * 0.7)).rjust(16))
            print("*" * 50)
            print("          주문코드:", random.randint(100000000000000000, 999999999999999999))




    else:

        now = time.localtime()

        s = "%04d-%02d-%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        print("\n" * 100)
        print("업체이름")
        print("업체주소")
        print("감사합니다. 또 이용해주세요.")
        print("[판  매]".center(50))
        print("거래일:", s)
        print("판매담당:0001/담당자".ljust(13), "               거래번호:", update_count(orderbutton))
        print("*" * 50)
        print("  제 품 명".ljust(10) + "   단가      수량".center(8) + "금 액".rjust(15))
        print("*" * 50)

        if ordersum > 0:

            for menuname, price, howmany in menulist:

                if howmany > 0:
                    prhow = price * 1
                    howmany = str(howmany)
                    price = str(price)
                    prhow = str(prhow)
                    print(menuname + price.rjust(10) + "1".rjust(9) + prhow.rjust(18))

            print("*" * 50)
            sale = 0
            sale = str(sale)
            ordersum = int(ordersum)

            list1.append(int(ordersum))
            a = random.randint(100000000000000000, 999999999999999999)
            list2.append(str(int(ordersum)) + "  " + s + "  " + str(a))

            print("총 합 계", str(ordersum).rjust(13), "할    인", sale.rjust(16))
            print("과세금액", str(cal_productPrice(int(ordersum))).rjust(13), "부가세액", str(cal_tax(int(ordersum))).rjust(16))
            print("청 구 액", str(int(ordersum)).rjust(13), "받 은 돈", str(int(ordersum)).rjust(16))
            print("*" * 50)
            print("          주문코드:", random.randint(100000000000000000, 999999999999999999))


kangfood = Tk()

kangfood.title("")

list1 = []
list2 = []

# ----메뉴판입니다----------------------

Label(kangfood, text="★행복햄버거에 오신 것을 환영합니다★").grid(row=0)
Label(kangfood, text="========메뉴========").grid(row=1)
Label(kangfood, text="주문 할 갯수를 입력하세요(주문 하지 않는 메뉴는 0 입력)^^").grid(row=1, column=1)
Label(kangfood, text="햄버거 3000 원").grid(row=2)
Label(kangfood, text="피자 5000 원").grid(row=3)
Label(kangfood, text="치킨 7000 원").grid(row=4)
Label(kangfood, text="냉면 1500 원").grid(row=5)
Label(kangfood, text="도시락 2500 원").grid(row=6)
Label(kangfood, text="치킨부리또 3000 원").grid(row=7)
Label(kangfood, text="아이스크림 500 원").grid(row=8)
Label(kangfood, text="★★다 고르셨다면★★  →→→").grid(row=9)
Label(kangfood, text="☆☆고르기 힘들다면☆☆  →→→").grid(row=10)
Label(kangfood, text="♥주방장 이름을 맞춰보세요!!♥  →→→").grid(row=11)

# ----------몇개 살지 입력하는 곳입니다.---------------

e3 = Entry(kangfood)
e3.grid(row=2, column=1)
e4 = Entry(kangfood)
e4.grid(row=3, column=1)
e5 = Entry(kangfood)
e5.grid(row=4, column=1)
e6 = Entry(kangfood)
e6.grid(row=5, column=1)
e7 = Entry(kangfood)
e7.grid(row=6, column=1)
e8 = Entry(kangfood)
e8.grid(row=7, column=1)
e9 = Entry(kangfood)
e9.grid(row=8, column=1)
e11 = Entry(kangfood)
e11.grid(row=11, column=1)

# ---------------버튼입니다-----------------------------


orderbutton = Button(kangfood, text="주문하기", command=ordersuccess)
orderbutton.grid(row=9, column=1)
orderbutton.bttn_clicks = 0

calculate = Button(kangfood, text="정산하기", command=sum_orderlist)
calculate.grid(row=9, column=2)

randombutton = Button(kangfood, text="랜덤선택", command=randomorderbutton)
randombutton.grid(row=10, column=1)

exitbutton = Button(kangfood, text="프로그램 종료", command=exit)
exitbutton.grid(row=10, column=2)

kangfood.mainloop()