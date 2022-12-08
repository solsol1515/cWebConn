
f = open('./data/temp.json','rt',encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))           # str (단순 글자_ 값 추출 어려움)

import json
it = json.loads(data)

print(it)
print(type(it))          # dict (dictionary 객체)

for k,val in it.items():
    print(k,'>',val)
    print(k,'>>',val['Job'])