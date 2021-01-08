def avg(*t): #เก็บข้อมูลหลายชนิด หลายตัวแล้วเรียกใช้ เพิ่มข้อมูลเข้าไป
    print(sum(t)/len(t))
gpas = list(eval(input('GPA : ')))
avg(*gpas)