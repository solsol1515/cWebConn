from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')

soup = BeautifulSoup(html,'html.parser')

# [1]
'''
infos = soup.select('#goodsListWrap a.gd_name')
for info in infos:
    print(info.text)

print(len(infos),'권이 검색되었습니다.')
'''

# [2]
imgs = soup.select('#yesSchList div.itemUnit img')
print(imgs)
for imgUrl in imgs:
    # imagae link 출력: src
    # 책 제목 출력: alt
    imgPath = imgUrl.attrs['data-original']
    bookName = imgUrl.attrs['alt'].strip().replace('/','_') 
    # 양쪽 공백 없애기 strip / '/'를 '_'로 바꾸기
    print(bookName,':',imgPath)
    request.urlretrieve(imgPath,'imgs/' + bookName + '.jpg')    # 디렉토리 없을 경우 오류 발생하기때문에 반드시 만들고 실행!
