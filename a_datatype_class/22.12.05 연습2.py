'''
1. 각 자료구조에 대한 설명이다. (가) ~ (라)에 알맞은 용어를 쓰시오.
(가) 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, LIFO(Last In First Out)로 구현된다.
(나) 먼저 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, FIFO(First In First Out)로 구현된다.
(다) 값의 변경이 불가능하며, 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용한다.
(라) 값을 순서 없이 저장하면서 중복을 불허한다.
'''

'''
2. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
a = [3, "apple", 2016, 4]
b = a.pop(0)        # ["apple",  2016, 4]
c = a.pop(1)        # [3, 2016, 4]
print(b + c)        


➀ 2019 ➁ Error ➂ 2010 ➃ 6 ➄ apple
'''

'''
3. 다음 코드의 실행 결과를 쓰시오.
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])
'''
'''
4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)

➀ {0: 'snake', 8: 'spider', 2: 'monkey', 6: 'ant', 4: 'cat'}
➁ {0: 'snake', 8: 'spider', 2: 'monkey', 4: 'ant', 4: 'cat', 'ant': 6}
➂ {0: 'snake', 8: 'spider', 2: 'monkey', 4: 'ant', 'ant': 6}
➃ {4: 'ant', 0: 'snake', 2: 'monkey', 8: 'spider', 'ant': 6}
➄ {0: 'snake', 8: 'spider', 2: 'monkey', 6: 'ant'}
'''
'''
5. 다음 코드의 실행 결과를 쓰시오.
Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)
'''
'''
6. 다음 코드의 실행 결과를 쓰시오.
a = list(range(10))
a.append(a[3])
a.pop(a[3])
a.insert(3, a[-1])
a.pop( )
print(a)
'''

'''
7. 다음 코드의 실행 결과를 쓰시오.
data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")
'''