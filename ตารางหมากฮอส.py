x = int(input('ป้อนตัวเลข '))
for row in range(x):
    for column in range(x):
        print ('x',end='') if (row+column)%2 == 0 else print('o',end='')
    print('x') 