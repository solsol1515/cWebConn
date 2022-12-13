import cx_Oracle as oci
from selenium import webdriver
from bs4 import BeautifulSoup
import time                         # 사용 안 했음
import folium

import API

map_osm = folium.Map(location=[37.572807, 126.975918],
                     zoom_start=7)

# (1) 페이지에서 매장명, 전화번호, 주소 추출

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

f = open('location.txt', 'w')
f.write('지점명, 전화번호, 주소, 위도, 경도\n')


# 페이지 수 만큼 돌림
for page_no in range(1, 75):

    # print('******** page'+str(page_no)+' ********')
    driver.get('http://ejadam.co.kr/bbs/board.php?bo_table=store&page=%d' % page_no)
    html = driver.page_source

    # print(html)
    # time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('table tbody tr')

    for data in datas:

        # [1] 수집 시스템 -- 웹 페이지에서 매장명, 전화번호, 주소 크롤링

        dLi = data.select('td')         # td 얻어옴

        name = dLi[0].select_one('a').text.strip() # 첫번째 td 밑의 a태그의 text
        number = dLi[1].text.strip()               # 두번째 td
        addr = dLi[2].text.strip()                 # 세번째 td

        res = [name, number, addr] # 입력할 배열 생성
        # print(res) 확인용 print문

        # Contact 객체를 생성하고 DB 에 입력
        conn = oci.connect('project1/jadam@192.168.0.2:1521/xe')

        # jadam 테이블에 지점명, 전화번호, 주소 입력 (insert)
        sql = '''
            INSERT INTO jadam3(name, tel, addr)
                VALUES(:0, :1, :2)
            '''
        cursor = conn.cursor()
        cursor.execute(sql, res)   # jadam 테이블에 리스트 내용 insert 함


        # **************************************
        
        # [2] 저장 시스템 -- DB에 위도, 경도 컬럼 추가
        
        # API 파일에서 위도, 경도를 얻어옴
        wk = API.addr_to_w_k(addr)


        #얻어온 값 저장
        res2 = [str(wk[0]), str(wk[1]), addr]

        # 주소가 같은 행에 위도, 경도 추가 (update)
        sql2 = '''
            UPDATE jadam3
            SET wido = :0 ,
                gydo = :1
            WHERE addr = :2
        '''
        cursor = conn.cursor()
        cursor.execute(sql2, res2)

        cursor.close()
        conn.commit()
        conn.close()

        # **************************************

        # [3] 처리 시스템 : 데이타베이스에 저장된 값으로 지도에 해당 위치 출력

        # 위도와 경도가 있는 경우 (찾을 수 없는 경우에는 마크를 추가하지 않음)
        if wk[0] != '찾을 수 없음' :
            folium.Marker(location=[wk[0], wk[1]],
                          popup=res[0],
                          icon=folium.Icon(color='green', icon='star')).add_to(map_osm)

        # [1] ,를 구분자로 하여 파일에 값 입력
        f.write(res[0] + ',' +  res[1] + ',' + res[2] + ',' + res2[0] + ',' + res2[1]+'\n')


map_osm.save('./map/map.html') # 지도 저장
f.close() # 파일 닫음
