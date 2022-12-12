"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수 (url 만들어주는 함수 (urljoin)?)
"""

from urllib import parse

baseUrl = 'http://www.example.com/html/a.html'

print(parse.urljoin(baseUrl,'b.html'))          #          http://www.example.com/html/b.html
print(parse.urljoin(baseUrl,'sub/c.html'))      # 상대경로  http://www.example.com/html/sub/c.html
print(parse.urljoin(baseUrl,'/sub/d.html'))     # 절대경로  http://www.example.com/sub/d.html

print(parse.urljoin(baseUrl,'../temp/e.html'))  # 상대경로  http://www.example.com/temp/e.html

print(parse.urljoin(baseUrl,'http://www.daum.net')) # http://www.daum.net (새로운 도메인이 나올 경우 다 덮어버림)