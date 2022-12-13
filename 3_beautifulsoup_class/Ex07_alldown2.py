"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

'''
    함수명: download_file
    인자  : url
    리턴값: result
    역할  : index.html 만들기, 디렉토리 만들기, 파일 만들기?

'''

def download_file(url):
    p = parse.urlparse(url)                 # url 쪼개기?
    # print('1-',p)
    savepath = './' + p.netloc + p.path
    # print('2-',savepath)                  # 2- ./docs.python.org/3.6/library/ 출력

    if re.search('/$',savepath):            # '/'로 끝나는 결과 찾아서
        savepath += 'index.html'            # 결과가 존재한다면 savepath에 index.html 붙여주기
        # print('3-',savepath)              # 3- ./docs.python.org/3.6/library/index.html

    # 만들고 싶은 디렉토리가 존재한다면 savepath로 리턴(디렉토리를 또 만들지 않도록)
    if os.path.exists(savepath): return savepath

    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):         # savedir이 존재하지 않는다면
         os.makedirs(savedir)

    try:
        request.urlretrieve(url,savepath)   # 파일 만들기
        time.sleep(2)                       # 파일 만들기 전 2초 쉬는 시간 주기 !
        print('download-',url)
        return savepath

    except:
        print('fail download:',url)
        return None

if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'    # (index.html생략됨)
    result = download_file(url)
    print(result)



