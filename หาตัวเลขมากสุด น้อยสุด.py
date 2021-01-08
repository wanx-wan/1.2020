max,min = 0,9999
while True:
    number  = int(input('กรอกตัวเลขของคุณ '))
    if number < 0:
        break
    if number > max:
        max = number
    if number < min:
        min = number
print('ค่าสูงสุด ',max)
print('ค่าต่ำสุด',min)