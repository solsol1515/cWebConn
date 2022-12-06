
# ------------------------------------------------------
"""
   (2) for문 (파이썬은 반복문 뒤에도 else 사용 가능_필수 아님)
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문:
            문장들
        else:
            문장들

"""
a = 112                     # 숫자형
b = ['1','2','3']           # 리스트
c = '987'                   # 문자열
# d = tuple(['1','2','3'])  # 튜플
d = tuple(b)                # 튜플
d = ('1','2','3')           # 튜플
e = dict(k=5, j=6)          # 딕셔너리

for entry in e:             # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)            # dict는 키만 출력됨

# 딕셔너리인 경우
for entry in e:
    print(e[entry])         # value 출력

for entry in e:
    print(entry, e[entry])  # key value 출력
else:
    print('end')

# 1부터 10까지의 합 구하기
'''
<자바 스타일>
int sum = 0;
for(int i=1; i<11; i++){
    sum += i;
}
'''
sum = 0
for i in range(1, 11):
    sum += i
print('sum =',sum)

# 1부터 10까지의 홀수의 합 구하기
sum = 0
for i in range(1, 11, 2):   # 1, 3, 5, 7, 9
    sum += i
print('sum =',sum)


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
gugu = 0
for x in range(2, 10):              # 2 ~ 9 단
    print("----"+str(x)+"단----")
    for y in range(1, 10):          # 1 ~ 9까지
        print(x,'*',y,'=',x*y)

li = ['z', 'y', 'x']
while li:
    data = li.pop()
    print(data)                     # x y z 순으로 출력
else:                               # 마지막에 위치한 각 요소가 pop되기때문에 무한루프X
    print('end')

