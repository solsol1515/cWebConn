
import cx_Oracle as oci
import csv
"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""

# (0) DB에 저장할 테이블 생성
def createDBTable():
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
        CREATE TABLE contact
        (
            name            varchar2(30),
            phone_number    varchar2(13),
            email           varchar2(30),
            addr            varchar2(50)
        )
        '''
    cur = conn.cursor()
    cur.execute(sql)

    cur.close()
    conn.close()

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input('이름은? ')
    phone = input('전화번호는? ')
    email = input('이메일은? ')
    addr = input('주소는? ')

    data = [name, phone, email, addr]

    # Contact 객체를 생성하고 DB 에 입력
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
             INSERT INTO contact
             VALUES(:0,:1,:2,:3)
          '''
    cur = conn.cursor()
    cur.execute(sql,data)

    cur.close()
    conn.commit()       # commit 빼먹지 말기 !!! 아주 중요 !!!
    conn.close()

def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = '''
              SELECT *
              FROM   contact
          '''
    cur = conn.cursor()
    cur.execute(sql)

    datas = cur.fetchall()
    for row in datas:
        c = Contact(row[0], row[1], row[2], row[3])
        c.print_info()

    cur.close()
    conn.close()

def delete_contact(name):
    # (3)
    # 해당 이름과 같은 요소를 찾아서 삭제
    conn = oci.connect('scott/tiger@localhost:1521/xe')
    sql = "DELETE  FROM   contact WHERE name = '"+name+"'"

    cur = conn.cursor()
    cur.execute(sql)

    cur.close()
    conn.commit()
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)

if __name__ == "__main__":
    # createDBTable()
    run()
