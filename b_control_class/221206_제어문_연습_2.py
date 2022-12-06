'''
1. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)
➀ [('apple', 1), ('banana', 2), ('grape', 3)]
➁ [(1, 'apple'), (2, 'banana'), (3, 'grape')]
➂ [(0, 'apple'), (1, 'banana'), (2, 'grape')]
➃ [('apple', 0), ('banana', 1), ('grape', 2)]
➄ [('grape',0), ('banana',1), ('apple',2)]
'''
# ➂

'''
2. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? 
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})
➀ {0: 'my', 1: 'cat', 2: 'has', 3: 'blue', 4: 'eyes,', 5: 'my', 6: 'cat', 7: 'is', 8: 'cute'}
➁ {'my': 0, 'cat': 1, 'has': 2, 'blue': 3, 'eyes,': 4, 'my': 5, 'cat': 6, 'is': 7, 'cute': 8}
➂ {0: 'my', 1: 'cat', 2: 'has', 3: 'blue', 4: 'eyes,', 5: 'is', 6: 'cute'}
➃ {'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}
➄ 오류
'''
# ➁

'''
3. 다음과 같이 코드를 작성했을 때, 예측되는 실행 결과를 쓰시오. 
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)
'''
# orange&pink&brown&black&white

'''
4. 다음 코드의 실행 결과를 쓰시오. 
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):   0 1 2 3
    user_dict[value_2] = value_1
print(user_dict)
'''
# {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}

'''
6. 다음 코드의 실행 결과를 쓰시오. 
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])
'''
# ['Cat', 'Panda', 'Owl']

'''
7. 다음 코드의 실행 결과를 쓰시오. 
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])
'''
# DongUniversity

'''
8. 다음과 같은 결과값을 출력하기에 적당한 함수를 빈칸에 쓰시오. 
>>> alist = ['a1', 'a2', 'a3']
>>> blist = ['b1', 'b2' ,'b3']
>>> for a, b in __________(alist, blist):
... print(a, b)
...
a1 b1
a2 b2
a3 b3
'''

'''
9. 다음과 같이 코드를 작성했을 때, 예측되는 실행 결과를 쓰시오. 
>>> a = [1, 2, 3]
>>> b = [4, 5, ]
>>> c = [7, 8, 9]
>>> print([[sum(k), len(k)] for k in zip(a, b, c)])
① [[6, 3], [9, 2], [24, 3]] 
② [[12, 3], [15, 3]] 
③ [[12, 3], [15, 3], [17, 3]] 
④ 오류 
⑤ [[12, 3], [15, 3], [12, 2]] 
'''
#

'''
10. 다음 코드의 실행 결과를 쓰시오. 
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])
'''
#

'''
11. 다음 코드의 실행 결과를 쓰시오. 
kor_score = [30, 79, 20, 100, 80] 
math_score = [43, 59, 0, 30, 90] 
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])
'''
#

'''
12. 다음 코드의 실행 결과를 쓰시오. 
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):
try:
    abcd.append(b[a])
except IndexError:
    abcd.append("error")

print(abcd)
'''
#

'''
13. 다음 코드의 실행 결과를 쓰시오. 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))
'''
#