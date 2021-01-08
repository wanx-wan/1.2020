while True: #continue
    x = int(input())
    if x <= 1:
        continue
    else:
        break
    print(x)

for i in range(1,10):
    if i%2 == 0:
        continue
    print(i)