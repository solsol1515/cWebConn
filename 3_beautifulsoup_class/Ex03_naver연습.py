"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 증권 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
print(res)

# 파싱하기
soup = BeautifulSoup(res,'html.parser')

# 추출하기 (find,attr(속성값),select)
usd = soup.select_one('#exchangeList span.value')
print('달러:',usd.text)

print('-'*50)
#con = soup.select('#exchangeList h3.h_lst span.blind')       # 나라명
#usd1 = soup.select('#exchangeList span.value')               # 환율값 가져오기
naver = soup.select('#exchangeList li')

for m in naver:
    name = m.select_one('h3.h_lst')
    f = m.select_one('span.value')
    print(name.text,':',f.text)

print('-'*50)
