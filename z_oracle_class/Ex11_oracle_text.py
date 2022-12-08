# [파이썬 + DB 절차]

import cx_Oracle as oci

# 1. 연결 객체 얻어오기 (Connection)
conn = oci.connect('scott/tiger@localhost:1521/xe')
print(conn.version)

# 2. sql 문장
sql = 'select * from emp'

# 3. cursor 객체 얻어오기(자바 전송 객체 얻어오기와 유사)
cur = conn.cursor()

# 4. 실행
cur.execute(sql)

datas = cur.fetchall()
# print(datas)
for row in datas:
    print(row[0], row[1], row[2])

# 5. cursor 객체 닫기
cur.close()

# 6. 연결 객체 닫기
conn.close()