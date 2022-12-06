'''
1. 다음 코드의 실행 결과를 쓰시오.
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)
'''
# apple

'''
2. 다음 코드의 실행 결과를 쓰시오. 
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:              str(5) != 5(숫자?)
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])
'''
# [3, 4.0]

'''
3. 다음 코드의 실행 결과를 쓰시오. 
num = 0
i = 1
while i < 8:                    # 
    if i % 3 == 0:              # 
        break
    i += 1 (i = i + 1)          1   2   3 
    num += i (num = num + i)    2   3   5

print(num)
'''
# 5

''' 다시 풀어보세용 !!! 
4. 다음 코드의 실행 결과를 쓰시오. 
result = 0
for i in range(5, -5, -2):      # 5, 3, 1, -1, -3, -5
    if i < -3:                  # -5일 때, result + 1?
        result += 1             
    else:
        result -= 1(result = result-1) # -1 -2  
print(result)
'''
# -5

'''
5. 다음 코드의 실행 결과를 쓰시오. 
num = ""
for i in range(10):             # 0 ~ 9
    if i <= 5 and (i % 2)==0:   # 8 9
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num
print(num)                      
# str(9)+str(8)+str(6)+str(5)+str(3)+str(1)
'''
# 986531

'''
6. 다음 코드의 실행 결과를 쓰시오. 
coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee  #16500  13000   9500    6000            5300    1800
        coupon += 1             #1      2       3       4               1       2
    else:                                                   
        money += 2800                                           8800
        coupon = 0                                              
print(money)                    #16500  13000   9500    6000    8800 5300       1800
'''
# 1800

'''
7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은? 
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:       # 1 2
    for j in list_data_b:   # 3 4
        result = i + j

print(result)

➀ 20 ➁ 6 ➂ [13, 14, 23, 24] ➃ [4, 5, 5, 6] ➄ Error
'''
# ➁