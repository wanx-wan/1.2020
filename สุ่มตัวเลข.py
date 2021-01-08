import random
myrandom = random.randrange(1,7)
k = 0
correct = False
while True:
    number =int(input('ป้อนตัวเลขที่ต้องการ '))
    if number<0 or k == 3:
        break
    correct = (number == myrandom)
    if not correct:
        if(number<myrandom):
            print('ป้อนมากกว่า ')
        else:
            print('ป้อนน้อยกว่า')
    if correct:
        print('ตอบถูก')
        break
    else :
        print('เสียใจด้วย')
    k += 1
if not correct:
    print('เสียใจด้วยนะ')
print('เฉลย',myrandom)