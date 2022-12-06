msg = '행복해'                    # 문자열
li = ['a','b','c']               # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')            # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking: 요소 분해
''' for(int i=0; i<msg.length(); i++){
    }
        or
    a = msg[0]
    b = msg[1]
    c = msg[2]
'''
a, b, c = msg
print(a)        # 행
print(b)        # 복
print(c)        # 해

alist = [(1,2), (3,4), (5,6)]       # 요소 3개 (튜플 3) > 반복문 3회
for temp in alist:
    print(temp)

for first, second in alist:
    print("{0} + {1} = {2}".format(first, second, first+second))
            # 1 + 2 = 3
            # 3 + 4 = 7
            # 5 + 6 = 11

# (2) enumerate() 함수
#       - 요소 & 인덱스 같이 뽑아주는 함수
'''
    [참고] 자바에서 
          Iterator > Enumerator(이전 버전)
'''
blist = ['개발자','코더','전문가','노가다']
for value in blist:
    print(value)

for value in enumerate(blist):          # 인덱스와 함께 출력해줌 (튜플형식)
    print(value)                        # (0, '개발자') 형식 출력

for idx, value in enumerate(blist):     # 인덱스와 밸류값 따로 출력
    print(idx, value)                   # 0 개발자 형식 출력

# (3) zip() 함수

days = ['월','화','수']
doit = ['잠자기','밥먹기','숨쉬기','멍때리기']

print(zip(days,doit))
print(list(zip(days,doit)))             # [('월', '잠자기'), ('화', '밥먹기'), ('수', '숨쉬기')]
print(dict(zip(days,doit)))             # {'월': '잠자기', '화': '밥먹기', '수': '숨쉬기'}

for data in zip(days,doit):
    print(data)                         # 튜플로 출력됨

for yoil, hallil in zip(days,doit):     # 월 잠자기 화 밥먹기 수 숨쉬기 출력
    print(yoil, hallil)

mon = [11, 12, 1]
print(list(zip(days,doit,mon)))
# [('월', '잠자기', 11), ('화', '밥먹기', 12), ('수', '숨쉬기', 1)]