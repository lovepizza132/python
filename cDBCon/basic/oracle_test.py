# 오라클 패키지 필요: cx_Oracle
# (윈도우) pip install cx_Oracle

import cx_Oracle as oci

# 1) 연결 객체 얻어오기
conn = oci.connect("scott/tiger@192.168.0.19:1521/orcl")
print(conn)

# 2) 커서 얻어오기
cursor = conn.cursor()

# 3) sql 문장 만들기
sql = "SELECT * FROM emp"

# 4) sql 문장 실행
cursor.execute(sql)

datas = cursor.fetchall()
for row in datas:
    print(row[0], ">", row[1])
print(datas)

# 5) 커서 닫기
cursor.close()

# 6) 연결 닫기
conn.close()