"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 증권 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Key
from bs4 import BeautifulSoup

# from urllib import request as req

options = webdriver.ChromeOptions()     # 크롬 브라우저 옵션
options.add_argument('headless')        # 브라우저 안 띄우기
options.add_argument('lang=ko_KR')      # KR 사용
chromedriver_path = "chromedriver"      # 크롬 드라이버 위치
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)     #chromedriver 열기


driver.quit     # driver 종료, 브라우저 닫기

# 웹 문서 가져오기
# //*[@id="search.keyword.query"]
search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')    # 검색 창
search_area.send_keys('맛집')    # 맛집 검색어 입력
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  #Enter로 검색

# 파싱하기
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
lists = soup.select('.placelist > .PlaceItem')

for jmt in lists:
    jmt_name = jmt.select('.head_item > .tit_name > .link_name')[0].text    # 맛집 이름
    print(jmt_name)


"""
# 추출하기 (find,attr(속성값),select)
jonmat = soup.select_one('.link_name')
# print('맛집 이름:',jonmat.text)



print('-'*50)
#con = soup.select('#exchangeList h3.h_lst span.blind')       # 나라명
#usd1 = soup.select('#exchangeList span.value')               # 환율값 가져오기
naver = soup.select('#exchangeList li')

for m in naver:
    name = m.select_one('h3.h_lst')
    f = m.select_one('span.value')
    print(name.text,':',f.text)

print('-'*50)
"""