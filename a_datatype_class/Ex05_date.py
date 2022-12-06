
# import datetime
# today = datetime.date.today()
# print('today is ', today)

#from datetime import date
#today = date.today()
#print('today is ', today)

from datetime import date, timedelta
today = date.today()
print('today is ', today)

# 날짜 구하기
print('년도: ', today.year)
print('월: ', today.month)
print('일: ', today.day)
print('요일: ', today.weekday())  # 월:0 화:1 수:2 목:3 금:4 토:5 일:6

# 날짜 계산
print('어제: ', today + timedelta(days=-1))

#일주일 전 날짜
print('일주일 전 날짜: ', today + timedelta(days=-7))
print('일주일 전 날짜: ', today + timedelta(weeks=-1))

#10일 후 날짜
print('10일 후 날짜: ', today + timedelta(days=10))

from datetime import datetime
day = datetime.today()
print(day)

# import datetime
# day = datetime.datetime.today()
# print(day)

# 날짜를 문자열 형태 (strftime() 이용)
print(day.strftime('%y년 %m월 %d일 %H:%M'))  # Y:2022 y:22

# 문자열을 날짜 형태 (strptime() 이용)
naljja = '2022-12-25 12:50:59'
print(type(naljja))
mydate = datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))