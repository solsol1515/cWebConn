from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from urllib import request as req
from urllib.parse import quote_plus
import os
from urllib import request, parse


# [1] 초록색 글씨만 가져오기
html1 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

soup1 = BeautifulSoup(html1,'html.parser')
txt1 = soup1.select('#text .green')

for t1 in txt1:
    print(t1.text)

print('-'*50)

# [2] 아이템과 가격을 추출
html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")

soup2 = BeautifulSoup(html2, 'html.parser')
txt2 = soup2.select('#wrapper #giftList .gift')
# print(txt2)
for t2 in txt2:
    item = t2.select_one('td')                  # item Title 가져오기
    cost = t2.select_one('td:nth-child(3)')     # cost 가져오기
    print(item.text,':',cost.text)

print('='*50)


# [3]
html3 = urlopen("https://wikidocs.net/")

soup3 = BeautifulSoup(html3,'html.parser')

#  1) 책 제목과 저자만 추출
txt3 = soup3.select('#books .media')
# print(txt3)
for t3 in txt3:
    title = t3.select_one('h4').text.strip().replace('/','_')             # title(제목) 가져오기
    author = t3.select_one('.book-detail a')    # author(저자) 가져오기
    print('제목:',title)
    print('저자:',author.text)
    print('-'*50)

#  2) 이미지 다운
    img = t3.select_one('.media-left .book-image-box img')    # 이미지 태그 추출
    url = "https://wikidocs.net"
    i = parse.quote_plus(parse.urljoin(url, img.attrs['src']),safe="://")   # url 한글깨짐 문제 해결 : quote_plus 사용
    req.urlretrieve(i,'imgs/'+title+'.jpg')