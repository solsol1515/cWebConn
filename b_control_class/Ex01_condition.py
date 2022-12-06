"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자 !!! 탭 사용하는 걸로 맞추자 !!!

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들 (아무것도 실행하지 않을 경우라면 pass 기재해줘야함 !! 공백으로 두면 X)

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = 20
if a:
    print('True')
else:
    print('False')      # 0이 아니기때문에 True 출력됨

b = 0
if a and b:
    print('True2')      # False > 출력 안 됨

if a or b:
    print('True3')      # True3 출력

print(a and b)          # b에 의해 결과가 결정되기때문에 [b값 출력]
print(a or b)           # or 연산자이기때문에 a로 인해 True 출력 가능하기때문에 [a값 출력]

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6

print(c)                # a가 20이므로 True > c = 2가 출력됨