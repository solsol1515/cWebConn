import cx_Oracle as oci
import csv

def createDBTable():
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
        CREATE TABLE supply
        (
            id              number       primary key,
            Supplier_Name   varchar2(50),
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(30),
            Cost            number,
            Purchase_Date   date        
        )
    '''
    cur = conn.cursor()
    cur.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cur.execute(sql2)

    cur.close()
    conn.close()


def saveDBTable(data):
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
            INSERT INTO supply
            VALUES(seq_supply_id.NEXTVAL,:0,:1,:2,:3,:4)
    '''
    cur = conn.cursor()
    cur.execute(sql, data)

    cur.close()
    conn.commit()           # 잊지 말자 !!!!!
    conn.close()

def viewDBTable(tableName):
    # 넘겨 받은 테이블명의 데이터 화면에 출력
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
          SELECT *
          FROM 
        ''' + tableName
    cur = conn.cursor()
    cur.execute(sql)

    datas = cur.fetchall()
    for row in datas:
        print(row[0], row[1], row[2], row[3], row[4], row[5])

    cur.close()
    conn.close()

if __name__ == '__main__':
    # (1) 테이블 생성
    # createDBTable()

    # (2-0) 입력 확인
    imsi = ['kosmo', '9999', '8888', 1000, '2022-12-24']
    saveDBTable(imsi)
    
    # (2) CSV 파일 읽어서 -> DB 입력
    file = open('supply.csv','rt')
    datas = csv.reader(file)
    # print(datas) 객체 출력됨

    header = next(datas, None)
    #print(header)
    #print('-'*50)

    for row in datas:
        saveDBTable(row)

    # (3) 테이블 내용 출력
    viewDBTable('supply')