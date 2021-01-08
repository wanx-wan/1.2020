data = input() #นับคำ
lst = data.split(' ')
lst2 = []
for i in lst:
    lst2.append(i.lower())
count = 0
for i in range(len(lst2)):
    chk = True
    for j in range(i):
        if(lst2[i] == lst2[j]):
            chk = False
    if chk:
        count += 1
print(count)