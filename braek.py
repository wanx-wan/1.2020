for i in range(1,10): #break
    if i == 5:
        break
    print(i)

a = [ ]
while True:
    x = int(input())
    if x == -1:
        break
    a.append(x)
print(a)