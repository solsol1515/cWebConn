import cx_Oracle as oci
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import folium

import API

map_osm = folium.Map(location=[37.572807, 126.975918],
                     zoom_start=7)

# (1) ���������� �����, ��ȭ��ȣ, �ּ� ����

# ������̹� ��ü ����
driver = webdriver.Chrome('webdrive/chromedriver.exe')
driver.implicitly_wait(3)

f = open('location.txt', 'w')
f.write('������, ��ȭ��ȣ, �ּ�, ����, �浵\n')

# ������ �� ��ŭ ����
for page_no in range(1, 75):

    # print('******** page'+str(page_no)+' ********')
    driver.get('http://ejadam.co.kr/bbs/board.php?bo_table=store&page=%d' % page_no)
    html = driver.page_source

    # print(html)
    # time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('.link-name')

    for data in datas:

        # [1] ���� �ý��� -- �� ���������� �����, ��ȭ��ȣ, �ּ� ũ�Ѹ�

        dLi = data.select('td')  # td ����

        name = dLi[0].select_one('a').text.strip()  # ù��° td ���� a�±��� text
        number = dLi[1].text.strip()  # �ι�° td
        addr = dLi[2].text.strip()  # ����° td

        res = [name, number, addr]  # �Է��� �迭 ����
        # print(res) Ȯ�ο� print��

        # Contact ��ü�� �����ϰ� DB �� �Է�
        conn = oci.connect('project1/jadam@192.168.0.2:1521/xe')

        # jadam ���̺� ������, ��ȭ��ȣ, �ּ� �Է� (insert)
        sql = '''
            INSERT INTO jadam(name, tel, addr)
                VALUES(:0, :1, :2)
            '''
        cursor = conn.cursor()
        cursor.execute(sql, res)  # jadam ���̺� ����Ʈ ���� insert ��

        # **************************************

        # [2] ���� �ý��� -- DB�� ����, �浵 �÷� �߰�

        # API ���Ͽ��� ����, �浵�� ����
        wk = API.addr_to_w_k(addr)

        # ���� �� ����
        res2 = [str(wk[0]), str(wk[1]), addr]

        # �ּҰ� ���� �࿡ ����, �浵 �߰� (update)
        sql2 = '''
            UPDATE jadam
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

        # [3] ó�� �ý��� : ����Ÿ���̽��� ����� ������ ������ �ش� ��ġ ���

        # ������ �浵�� �ִ� ��� (ã�� �� ���� ��쿡�� ��ũ�� �߰����� ����)
        if wk[0] != 'ã�� �� ����':
            folium.Marker(location=[wk[0], wk[1]],
                          popup=res[0],
                          icon=folium.Icon(color='green', icon='star')).add_to(map_osm)

        # [1] ,�� �����ڷ� �Ͽ� ���Ͽ� �� �Է�
        f.write(res[0] + ',' + res[1] + ',' + res[2] + ',' + res2[0] + ',' + res2[1] + '\n')

map_osm.save('./map/map.html')  # ���� ����
f.close()  # ���� ����
