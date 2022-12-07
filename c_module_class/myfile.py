# !!! import 잘 확인하기 !!!

#(1) mymodule.py에서 가져온 함수 호출하기 (import)
# import mymodule           #mymodule.py에서 가져온 함수 호출하기
#
# print('오늘의 날씨 :', mymodule.get_weather())
# print('오늘은 :', mymodule.get_date(),'요일')

#(2) import 별칭을 정해줄 경우, 별칭으로만 호출해야함
# import mymodule as mm
#
# print('오늘의 날씨 :', mm.get_weather())
# print('오늘은 :', mm.get_date(),'요일')

#(3) import할 함수를 부분적으로 가져와서 모듈 이름 필요없이 이름으로만 호출 가능
from mypackage.mymodule import get_weather, get_date

print('오늘의 날씨 :', get_weather())
print('오늘은 :', get_date(),'요일')