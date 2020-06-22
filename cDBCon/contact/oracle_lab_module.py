import cx_Oracle as oci

# 1 DB 연결 및 데이터 입력
def insertdata(data):
    print("넘어간거",data)
    print("넘어간거", data[3])
    conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")
    cursor = conn.cursor()
    sql = '''
        INSERT INTO CONTACT(NAME, phone_name, email, addr)
        VALUES(:v_name, :v_phone, :v_email, :v_addr)
    '''
    v_name=data[0]
    v_phone=data[1]
    v_email=data[2]
    v_addr=data[3]

    cursor.execute(sql, (v_name, v_phone, v_email, v_addr))
    conn.commit()

    cursor.close()
    conn.close()

