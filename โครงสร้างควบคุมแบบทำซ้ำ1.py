i = 1
summation = 0
average  = 0
count = int(input())
while i <= count:
     summation += i
     print('รอบที่ ', i ,'ค่า sum =',summation)
     i += 1
average = summation/count
print('ผลรวมการบวกเลข = ',summation)
print('ค่าเฉลี่ย ',average)