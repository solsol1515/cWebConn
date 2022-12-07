# (1) import package
# import mypackage.mymodule

# print('오늘의 날씨 :', mypackage.mymodule.get_weather())
# print('오늘은 :', mypackage.mymodule.get_date(),'요일')

# (2) from 패키지이름 import 가져올 파일
# from mypackage import mymodule

# print('오늘의 날씨 :', mymodule.get_weather())
# print('오늘은 :', mymodule.get_date(),'요일')

# (3) 별칭
from mypackage import mymodule as mm

print('오늘의 날씨 :', mm.get_weather())
print('오늘은 :', mm.get_date(),'요일')