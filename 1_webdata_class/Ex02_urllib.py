# 내장 모듈 이용

from urllib import request

url = 'http://www.google.com'
site = request.urlopen(url)

page = site.read()                      # 연 뒤에 읽기
print(page)
print('-'*50)

print(site.status)                      # 01과 다르게 status를 따로 요청해야 볼 수 있음

headers = site.getheaders()
print(headers)                          # 리스트 구조 - 튜플 형식으로 출력됨

for header in headers:
    print(header)                       # 튜플 형식으로 나옴

print('='*50)

for header in headers:
    print(header[0],'>>',header[1])     # key : value