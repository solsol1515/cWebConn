"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse, request
# from urllib import request

'''
    함수명 : enum_links(a,b)
    인자   : html,base
    리턴값 : result
    역할   : url 주소 받아서 하나의 list에 결과값 저장해서 붙이고 리턴 !  
            (서버에 의존해서 작업하기엔 응답받는 시간이 오래걸리기때문에 데이터 저장)
'''
def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html,'html.parser')
    links = soup.select('a')            # a태그 여러개 links로 받기
#   print(links)                        # a태그 잘 받아오는지 확인


    result = []
    for a in links:
        href = a.attrs['href']
        # print(href)
        url = parse.urljoin(base,href)
        # print(url)
        result.append(url)              # result list에 저장하기

    return result

if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)