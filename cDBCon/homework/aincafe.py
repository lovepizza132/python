# tkinter는 Lightweight GUI 모듈
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from homework.aincafe_module import *


price = {'아이템1': 3500, '아이템2': 4000, '아이템3': 4500, '아이템4': 3000, '아이템5': 4000, '아이템6': 5500, '아이템7': 6000, '아이템8': 4500, '아이템9': 4000}
buylist = []  #주문 리스트
sum = 0     # 총 금액
orderList = {}  # 주문 리스트 : 메뉴명 n개 가격


# 주문 리스트 추가 함수
def add(item):
    global sum  #전역 변수 사용을 위해 global 이용
    # 주문 총합 계산
    this_price = price[item]
    sum += this_price

    # 주문 리스트 함수
    if item in orderList:
        orderList[item] += 1
    else:
        orderList[item] = 1

    textarea.delete(0.0, 'end')
    for order_item in orderList:
        st_line = str(order_item) + '\t\t\t'+ str(orderList[order_item]).center(6) + '개 \t\t\t\t' + str(price[order_item]*orderList[order_item]).rjust(7) + '원'
        textarea.insert(tk.INSERT, st_line+" \n")


    label1['text'] = "금액: " + str(sum) + "원"


# 프로그램 종료 함수
def btn_exit():
    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        exit()

window = tk.Tk()    # 화면을 띄움
window.title("음료 주문")
window.geometry("1200x800+350+100")  #화면 크기 설정
window.resizable(False, False)

# 주문 함수(DB와 연결)
def btn_order():
    msgbox = tk.messagebox.askquestion('확인', '주문을 진행할까요?')
    if msgbox == 'yes':
        global sum
        order_id = aincafe_module.order(orderList, price, sum)
        print_orderList(order_id)
        sum = 0
        label1['text'] = "금액: 0원"
        orderList.clear()
        textarea.delete(0.0, 'end')

def print_orderList(order_id):
    print('*'*50)
    print(order_id)
    print('*'*50)
    print()



# 윈도우 안에 있는 프레임 형성, 프레임에 버튼 나열을 위한 프레임 형성)
topframe=tk.Frame(window, width=1100, height=50)
topframe.pack(side=TOP)

frame0 = tk.Frame(window, width=1100, height=700)
frame0.pack()

frame1 = tk.Frame(frame0, width=850, height=700)
frame1.pack(side=LEFT)

frame2 = tk.Frame(frame0, width=250, height=700)
frame2.pack(side=RIGHT)

frame2_bottom = tk.Frame(frame2, width=250, height=10)
frame2_bottom.pack(side=BOTTOM)


# 프레임 안에 버튼 들 배열
tk.Button(frame1, text='아이템1', command=lambda: add('아이템1'), width=30, height=15).grid(row=0, column=0)
tk.Button(frame1, text='아이템2', command=lambda: add('아이템2'), width=30, height=15).grid(row=0, column=1)
tk.Button(frame1, text='아이템3', command=lambda: add('아이템3'), width=30, height=15).grid(row=0, column=2)
tk.Button(frame1, text='아이템4', command=lambda: add('아이템4'), width=30, height=15).grid(row=1, column=0)
tk.Button(frame1, text='아이템5', command=lambda: add('아이템5'), width=30, height=15).grid(row=1, column=1)
tk.Button(frame1, text='아이템6', command=lambda: add('아이템6'), width=30, height=15).grid(row=1, column=2)
tk.Button(frame1, text='아이템7', command=lambda: add('아이템7'), width=30, height=15).grid(row=2, column=0)
tk.Button(frame1, text='아이템8', command=lambda: add('아이템8'), width=30, height=15).grid(row=2, column=1)
tk.Button(frame1, text='아이템9', command=lambda: add('아이템9'), width=30, height=15).grid(row=2, column=2)


# 선택한 메뉴를 나열하는 textarea 형성
textarea = tk.Text(frame2, width=70, height=33)
textarea.pack(side=TOP)


# 총금액이 표시되는 label 추가
label1 = tk.Label(frame2, text="금액: 0원", width=20, height=2, fg='blue')
label1.pack()


# 주문종료 버튼
tk.Button(frame2_bottom, text='주문하기', command=btn_order, width=20, height=2).grid(row=0, column=0)
tk.Button(frame2_bottom, text='영수증 출력', command=btn_exit, width=20, height=2).grid(row=0, column=1)
#orderButton.pack()
tk.Button(frame2_bottom, text='종료하기', command=btn_exit, width=20, height=2).grid(row=0, column=2)
#exitButton.pack()


window.mainloop()   # .mainloop(): 이벤트 메시지 루프로서 키보드나 마우스 혹은 화면 Redraw와 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역활을 한다.
