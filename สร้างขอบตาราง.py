x = int(input('ป้อนตัวเลข '))
for row in range(x):
    for column in range(x):
        if row == 0 or row == x-1 or column == 0 or column == x-1:
            print ('x',end='')
        else:
            print(' ',end='')
    print(' ') 