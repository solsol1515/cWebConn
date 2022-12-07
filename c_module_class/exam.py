# exam.py

from mypackage.exam.exmodule import deohagi
#from mypackage.exam.exmodule import deohagi
#import mypackage.exam.exmodule as a
#from mypackage.exam import exmodule as ex

print(deohagi(3,4))     # 7
print(deohagi(3,'a'))   # 사용 불가

import mypackage
print(mypackage.exam.exmodule.deohagi(3,4))