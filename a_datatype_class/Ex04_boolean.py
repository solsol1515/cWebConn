# 부울형 - 첫글자는 반드시 "대문자" True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(not hungry)           # False
print(hungry and sleepy)    # False
print(hungry or sleepy)     # True
print(hungry & sleepy)      # False
print(hungry | sleepy)      # True



"""
        자료형         값           부울형
    --------------------------------------------
        문자형       "문자"          True
                    ""                   False
        리스트       [1,2,3]        True       
                    []                   False
        튜플         ()                   False
        딕셔너리     {}                    False
        숫자형       0이아닌 숫자     True
                    0                    False
                    None                 False

"""
if '아':            # True
    print('True')
else:
    print('False')

if []:              # False
    print('True2')
else:
    print('False2')

if 0:               # False
    print('True3')
else:
    print('False3')

if -1:               # True (0이 아닌 모든 수: True)
    print('True4')
else:
    print('False4')
    
msg = '행복합시다'
if msg.find('행'):
    print('ok')
else:
    print('no')      # 인덱스 0번 자리에 '행'이 있어서 no 출력됨
    
if msg.find('가'):
    print('ok')
else:
    print('nono')    # '가'가 없어서 -1 리턴 > 0 이 아니라 ok 출력됨

if msg.find('행') > -1:  # 조건으로 인해 0>-1이 성립되므로 ok 출력
    print('ok(-1)')
else:
    print('no(-1)')