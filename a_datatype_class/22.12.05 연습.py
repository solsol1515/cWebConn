'''
1. 다음 코드의 실행 결과를 쓰시오

a = [0, 1, 2, 3, 4]

print(a[:3], a[:-3])

# [0, 1, 2] [0, 1]
'''

'''
2. 다음 코드의 실행 결과를 쓰시오.

a = [0, 1, 2, 3, 4]

print(a[::-1])

# [4, 3, 2, 1, 0]
'''

'''
3. 다음 코드의 실행 결과를 쓰시오.

first = ["egg", "salad", "bread", "soup", "canafe"]

second = ["fish", "lamb", "pork", "beef", "chicken"]

third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]

john = [order[0][:-2], second[1::3], third[0]]
# first, second, lamb, pork, apple
del john[2]
# first, second, pork, apple
john.extend([order[2][0:1]])
# 
print(john)

'''
'''
4. 다음 코드의 실행 결과를 쓰시오.

list_a = [3, 2, 1, 4]

list_b = list_a.sort()

print(list_a, list_b)

# [1, 2, 3, 4, 1, 2, 3, 4]
'''

'''
5. 다음 코드의 실행 결과를 쓰시오.

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']

print(fruits[-3:], fruits[1::3])

# ['orange', 'strawberry', 'melon'] ['banana', 'orange']
'''

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']

print(fruits[-3:], fruits[1::3])
'''
6. 다음 코드의 실행 결과를 쓰시오.

num = [1, 2, 3, 4]

print(num * 2)

# [1, 2, 3, 4, 1, 2, 3, 4]
'''

num = [1, 2, 3, 4]

print(num * 2)
'''
7. 다음 코드의 실행 결과를 쓰시오.

a = [1, 2, 3, 5]

b = ['a', 'b', 'c', 'd', 'e']

a.append('g')

b.append(6)

print('g' in b, len(b))

# False 6
'''


'''
8. 다음과 같이 코드를 작성했을
때, 실행
결과로
알맞은
것은?

list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']

list_b = []

for i in range(len(list_a)):

if i % 2 != 1:

list_b.append(list_a[i])

print(list_b)

➀ None

➁ Error

➂ ['Hankook', 'is', 'academic', 'located', 'South Korea']

➃ ['University', 'an', 'institute', 'in']

➄ ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']

# ➀
'''

'''
9. 다음 코드를 실행한 후, 2018과 "2018"을 각각 입력했을 경우 알맞은 실행 결과끼리 묶인 것은?

admission_year = input("입학 연도를 입력하세요: ")

print(type(admission_year))

➀ <class ‘str’ >, < class ‘float’ >

➁ <class ‘int’’ >, < class ’str’ >

➂ <class ‘str’ >, < class ‘str’ >

➃ <class ‘int’ >, < class ‘int’ >

➄ <class ‘float’ >, < class ‘int’ >

# ➂
'''

'''
10. 다음 코드의 실행 결과를 쓰시오.

country = ["Korea", "Japan", "China"]

capital = ["Seoul", "Tokyo", "Beijing"]

index = [1, 2, 3]

country.append(capital)

country[3][1] = index[1:]

print(country)

# ['Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]
'''

'''
11.
다음과 같이 코드를 작성했을 때 예측되는 실행 결과를 쓰고, 이러한 결과가 나오는 이유에 대해 서술하시오.
( is 키워드는 주소를 비교한다 )

>> > a = [5, 4, 3, 2, 1]

>> > b = a

>> > c = [5, 4, 3, 2, 1]

>> > a is b
# a와 b는 같은 주소와 리스트를 가지기때문에 얕은 복사를 함 (True)

>> > a is c
# a와 b는 값만 같을 뿐 주소는 다르기때문에 False

'''



'''
15. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

list_1 = [[1, 2], [3], [4, 5, 6]]

a, b, c = list_1

list_2 = a + b + c

print(list_2)

➀ [1, 2, 3, 4, 5, 6] ➁ [[1, 2], [3], [4, 5, 6]]➂ 21

➃ Error ➄ [[1, 2], [3, 4, 5, 6]]

# ➀
'''
