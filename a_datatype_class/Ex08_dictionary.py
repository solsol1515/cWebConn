"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경 가능

    ` 사전.keys()     : key만 추출 (임의의 순서)
    ` 사전.values()   : value만 추출 (임의의 순서)
    ` 사전.items()    : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1])
print(dt['3'])


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2[(3,4)])
# 'turple' -> 'python' 값 변경하기
dt2[(3,4)] = 'python'
print(dt2)

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt2['korea'] = 'seoul'
print(dt2)

# 'seoul -> '한국'
dt2['korea'] = '한국'
print(dt2)

# 여러개 추가할 때
dt2.update({5:'five', 6:'six'})
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2.keys())
print(dt2.values())
print(dt2.items())  # key: value의 값을 튜플형식으로 여러개 뽑아줌


# Key와 Value만 따로 검색