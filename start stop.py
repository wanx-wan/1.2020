start,stop = 1,5
sum,avg = 0,0
while (start<=stop):
    number = int(input())
    sum += number
    start += 1
avg = sum/stop
print(sum)
print(avg)