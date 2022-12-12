"""
    [ 노랑통닭 매장 주소 가져오기 ]

    노랑통닭 http://www.norangtongdak.co.kr/ > 매장찾기 > 매장찾기
                  http://www.norangtongdak.co.kr/store/store.html

    개발자모드( F12 ) 열고 페이지 번호를 누르면 링크 확인

"""

from selenium import webdriver

#-------------------------------1. 웹 페이지 접근
# 웹드라이버 객체 생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3)

# 페이지 접근

