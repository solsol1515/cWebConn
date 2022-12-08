import cx_Oracle as oci

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


if __name__ == '__main__':
    # (1) 테이블 생성
    createDBTable()