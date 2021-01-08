data = input()
lst = data.split(' ')
dic = {}
for i in lst:
    tmp = i.lower()
    dic[tmp] = dic.get(tmp,0)+1
for key,value in dic.items():
    print(key,value)