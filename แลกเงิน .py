number = int(input('จำนวนเงิน :'))

if number>=1000:
    print('1000 บาท ',number//1000,' ใบ')
    number %= 1000
if number>=500:
    print('500 บาท ',number//500,' ใบ')
    number %= 500
if number>=100:
    print('100 บาท ',number//100,' ใบ')
    number %= 100
if number>=50:
    print('50 บาท ',number//50,' ใบ')
    number %= 50
if number>=10:
    print('10 บาท',number//10,' เหรียญ')