'''
 [과제] 교보문고에서 파이썬 책 검색하여
    - csv 파일로 저장
    - mysql 테이블에 저장
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 교보문고 > '파이썬' 검색 > 국내도서
html = urlopen("https://search.kyobobook.co.kr/search?keyword=python&gbCode=TOT&target=total")

soup = BeautifulSoup(html,'html.parser')

prod_item = soup.select('li.prod_item')
for prod_info in prod_item:
    # print(prod_info)
    imgTag = prod_info.select('img')
    print(imgTag)
    # print(imgTag[0].attrs['src'])     # 데이터 크롤링 불가능해서 yes24로 연습 !