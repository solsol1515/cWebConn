
'''
    data / sample.json 파일을 읽고, 총 합을 구해서 출력하기
'''

f = open('./data/sample.json','rt',encoding='utf-8')
sample = f.read()
f.close()

print(sample)

import json
sam = json.loads(sample)

print(sam)

sum = 0

for k,val in sam.items():
    print(k,'>',val)
    sum += val['price']*val['count']

print('총 합:',sum,'원')