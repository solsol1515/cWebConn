'''[ 기초문제 ]


1.다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
	a = set(list_data)          # 0 1 3 4 5 7 8
	return list(a)[1:5]         # 1 3 4 5

print(quiz_2(list_1))           # 1 3 4 5


➀ {1, 3, 4, 5} ➁ [1, 3, 4, 5]➂ {3, 1, 7, 5}
➃ {0, 3, 1, 7} ➄ [3, 1, 7, 5]
'''
# ➀

'''
2. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
def  delete_a_list_element(list_data, element_value):
	if element_value in list_data:
		list_data.remove(element_value)
		return list_data
	else:
		return "False"

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)


➀ Error ➁ ['a', 1, 'gachon'] ➂ None
➃ False ➄ ['a', 1, 'gachon', '2016.0']
'''
# ➁ 아니고 ➃ 2016.0은 str > 21라인 성립 X > else에 걸려서 False 출력

'''
3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):
		result.append(i)
	return result

print(quiz_1(tuple_1, tuple_2))

➀ [1, 2, 3, 4, 5, 6] ➁ [(1, 2, 3) (4, 5, 6)] ➂ (1, 2, 3) (4, 5, 6)
➃ [(1, 2, 3, 4, 5, 6)] ➄ (1, 2, 3, 4, 5, 6)
'''
# ➃ 아니고 ➀

'''
[ 연습문제 ]

1- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수를 만들어서 호출하여 그 결과를 출력하시오
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

    [ 결과 ]
        [2,4,8,10]
'''
def even_filter(numbers):
    list = []
    for i in numbers:               # 입력 받은 배열 수만큼 반복
        if i % 2 == 0 :
            list.append(i)
    print(list)

even_filter([1, 2, 4, 5, 8, 9, 10])


'''
2- 주어진 수가 소수인지 아닌지 판단하는 함수를 만들어서 호출하여 그 결과를 출력하시오
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

    [ 결과 ]
        False
        True
'''

def is_prime_number(num):       # num 입력받아 소수인지 아닌지 구분하는 함수
    # num이 1이 아니면

    for i in range(2,num):
        if num % i==0:
            return "False"
        return "True"

print('2(1)- ',is_prime_number(60))
print('2(2)- ',is_prime_number(61))


'''
3- 주어진 문자열에서 모음의 개수를 출력하는 함수를 만들어서 호출하여 그 결과를 출력하시오
    [ 실행 ]
        print(count_vowel("pythonian"))

    [ 결과 ]
        3
'''
def count_vowel(str):
    
    vowels = 'aeiouAEIOU'       # 모음들
    count = 0                   # 모음 개수

    for i in str:
        if i in vowels:         # 모음이 있을 경우,
            count += 1          # +1 count
    return count
print('(3)', count_vowel("pythonian"))