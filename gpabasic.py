gpa = int(input('กรอกเกรด : '))
if gpa >= 0 and gpa < 50:
    print('F')
elif gpa >= 50 and gpa < 60:
    print('D')
elif gpa >= 60 and gpa < 70:
    print('C')
elif gpa >= 70 and gpa < 80:
    print('B')
elif gpa >= 80 and gpa <=100:
    print('A')