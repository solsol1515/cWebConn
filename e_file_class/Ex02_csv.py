# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value

data = [[1,'박','책임'],[2,'김','선임'],[3,'맹','연구원']]

import csv

# with open('./data/imsi.csv','wt',encoding='utf-8') as f:       # t는 생략 가능 (default값이라서)
#     # f.write(data)
#     cout = csv.writer(f)   # f와 csv 연결
#     cout.writerows(data)

result = []
with open('./data/imsi.csv','rt',encoding='utf-8-sig') as f:         # t는 생략 가능 (default값이라서)
    cin = csv.reader(f)
    result = [row for row in cin if row]
    # row가 있을 경우만 for문에 row값 추가 (빈 값 빼기 위해서 if문 사용)

print(result)