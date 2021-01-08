x = int(input('ป้อนตัวเลข '))
for row in range(1,x+4):
    for column in range(1,row+1):
        print(column,end='')
    print(' ')