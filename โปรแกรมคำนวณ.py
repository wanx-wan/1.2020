weight = int(input('ป้อนน้ำหนัก kg :'))
high = int(input('ป้อนส่วนสูง cm :'))
high /= 100
weight /= high**2
print(weight)
if weight < 18.50:
    print('น้ำหนักน้อยหรือผอม ')
elif 18.50 < weight < 22.90:
    print('น้ำหนักสมส่วน ')
elif 22.90 < weight < 24.90:
    print('น้ำหนักเกิน ')
elif 24.90 < weight < 29.90:
    print('โรคอ้วนระดับที่ 1 ')
else :
    print('โรคอ้วนระดับ 2 ')