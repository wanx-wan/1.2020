n = int(input()) #อายุ เกรดเฉลี่ย เมล
dic = {}
for i in range(n):
    data = input().split(',')
    print(data)
    ky = data[2]
    val = data[:2]
    dic[ky] = [val]
for key,value in dic.items():
    print(key,value)