#-------------------------------------------
# 파이썬 라이브러리가 설치된 디렉토리에 작성한 모듈이 있는 디렉토리를 추가
# 사용자 작성 모듈도 다른 곳에서 사용 가능

import sys
print(sys.path)
sys.path.append("D:\MyClass\Python\aBasic\c_module\mypackage")
print(sys.path)