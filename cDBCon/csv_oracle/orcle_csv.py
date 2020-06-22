import cx_Oracle as oci
import csv

def createTable():
    # 1) 연결객체 얻어오기
    conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")

    # 2) 커서 얻어오기
    cursor = conn.cursor()

    # 3) sql 문장 만들기
    sql = '''
        CREATE TABLE supply(
            id  integer  primary key,
            Supplier_Name   varchar2(30),
            Invoice_Number  varchar2(20),
            Part_Number     varchar2(20),
            Cost    integer,
            Purchase_Date   date
            )
    '''

    # 4) sql 문장 실행
    cursor.execute(sql)

    # 시퀀스 생성하는 sql 만들어서 실행
    sql2 = "CREATE SEQUENCE seq_supply_id"
    cursor.execute(sql2)

    # 5) 커서 닫기
    cursor.close()

    # 6) 연결 닫기
    conn.close()

def insertTable(data):
    # 1) 연결객체 얻어오기
    conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")

    # 2) 커서 얻어오기
    cursor = conn.cursor()

    # 3) sql 문장 만들기
    sql = '''
        INSERT INTO supply
        (id, Supplier_Name, Invoice_Number, Part_Number, Cost, Purchase_Date)
        VALUES(seq_supply_id.nextval, :v_name, :v_invoice, :v_part, :v_cost, :v_date)
    '''

    # 4) sql 문장 실행
    v_name=data[0]
    v_invoice=data[1]
    v_part=data[2]
    v_cost=data[3]
    v_date=data[4]

    cursor.execute(sql, (v_name, v_invoice, v_part, v_cost, v_date))
    conn.commit() ### commit 꼭 필요

    # 5) 커서 닫기
    cursor.close()

    # 6) 연결 닫기
    conn.close()

def viewTable(tableName):
    # 1) 연결객체 얻어오기
    conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")

    # 2) 커서 얻어오기
    cursor = conn.cursor()

    # 3) sql 문장 만들기
    sql = "SELECT * FROM {0}".format(tableName)

    # 4) sql 문장 실행
    cursor.execute(sql)

    datas = cursor.fetchall()   # DB 결과 값 받아오는 함수
    for row in datas:
        print(row)

    # 5) 커서 닫기
    cursor.close()

    # 6) 연결 닫기
    conn.close()


# 메인 함수 역할
if __name__ == '__main__':

    # (1) db(table)생성
    # createTable()

    # (2) csv 읽어서 DB에 입력
    # file_name = '../files/supply.csv'
    # file = open(file_name, 'r')
    # datas = csv.reader(file,delimiter=',')  #',' 기준으로 데이터를 자름
    # header = next(datas, None)   # 컬럼명이 기입되어있는 첫번째 줄을 빼기 위해 next사용, 그리고 버릴것이기에 None 사용
    # print(header)
    # print('-'*50)
    # for row in datas:   # 리스트 형식과 문자열로 처리 됨 ex- ['Samsung', '1001' ] 이런 식
    #     print(row)
    #     insertTable(row)

    # (3) DB 값을 가져와서 보여주기
    viewTable('supply')