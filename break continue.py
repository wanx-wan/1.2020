x = 1
y = 1
while x <= 10:
    x += 1
    if x == 5:
        continue
    print('รอบที่ ',x)
else:
    print('จบโปรแกรม')
    
while y <= 10:
    print('รอบที่ ',y)
    if x == 5:
        break
    y += 1
else:
    print('จบโปรแกรม')