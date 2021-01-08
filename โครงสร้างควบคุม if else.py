age = int(input('ป้อนอายุ :'))
if 15 <= age < 20:
    print('วัยรุ่น')
elif 20 <= age < 30 :
    print('วัยผู้ใหญ่')
elif 30 <= age < 80 :
    print('วัยทำงาน')
elif age >= 80 :
    print('สูงวัย')
else:
    print('วัยเด็ก')