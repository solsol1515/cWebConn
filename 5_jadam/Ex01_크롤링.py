from selenium import webdriver
from bs4 import BeautifulSoup
import time, folium, cx_Oracle as oci
import API

map_osm = folium.Map(location=[37.572807, 126.975918],
                     zoom_start=18)

# 1. webdriver 객체 생성
driver = webdriver.Chrome('../5_jadam/webdriver/chromedriver.exe')
driver.implicitly_wait(5)

for page_no in range(1,75):
    driver.get('http://ejadam.co.kr/bbs/board.php?bo_table=store&page=%d' % page_no)
    html = driver.page_source
    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html,'html.parser')
    datas = soup.select('table tbody tr')
    
    # 매장명 / 전화번호
    for data in datas:
        dLi = data.select('td')                      # td 얻어오기

        name = dLi[0].select_one('a').text.strip()   # 첫 번째 td 밑의 a 태그 text
        number = dLi[1].text.strip()                 # 두 번째 td
        addr = dLi[2].text.strip()                   # 세 번째 td

        res = [name, number, addr]                   # 입력할 배열 생성
        # print(res)                                 # 확인용 print
        
        # Contact 객체 생성 후 DB에 입력
        conn = oci.connect('project1/jadam@192.168.0.2:1521/xe')

        sql = '''
              INSERT INTO jadam3(name, tel, addr)
              VALUES(:0, :1, :2)
        '''

        cursor = conn.cursor()
        cursor.execute(sql,res)                       # jadam3 테이블에 내용 insert

    # 위도, 경도 얻어오기
    wk = API.addr_to_w_k(addr)
    # print('위도>>',wk[0],'경도>>',wk[1])

    res2 = [str(wk[0]), str(wk[1]), addr]
    sql2 = '''
            UPDATE jadam3
            SET    wido = :0,
                   gido = :1
            WHERE  addr = :2
    '''

    cursor = conn.cursor()
    cursor.execute(sql2, res2)                       # jadam3 테이블에 내용 insert

    folium.Marker(location=[wk[0],wk[1]],
                  popup=res[0],
                  icon=folium.Icon(color='green', icon='star')).add_to(map_osm)
    print('매장명:',res[0],'전화번호:',res[1],'주소:',res[2],'위도:',res2[0],'경도:',res2[1])

map_osm.save('./map/map.html')