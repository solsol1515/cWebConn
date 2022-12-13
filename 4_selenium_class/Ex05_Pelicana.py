from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3)

# [연습]
print('-' * 20)
print('매장명 - 전화번호')
print('-' * 20)

for page_no in range(1, 11):
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d' % page_no)
    html = driver.page_source
    # print(html)
    time.sleep(5)

    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select('table tbody tr')

    # 매장명 - 전화번호
    for data in datas:
        dLi = data.select('td.t_center')
        # print(dLi)
        if len(dLi) == 0:
            break

        name = dLi[0].text.strip()
        num = dLi[1]
        number = []
        # print(num)
        if '<br/>' in str(num):
            # print(num)
            number = str(num).split('<br/>')

            for i in range(len(number)):
                number[i] = number[i].strip()

            number[0] = number[0][-12:]
            number[1] = number[1][:11]

        else :
            number = num.text.strip()

        print(name, '-', number)