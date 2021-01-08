students = {} #ข้อมูลนักศึกษา 10 คน เป็น dictionary โดยให้ผู้ใช้กรอก ชื่อ และ อายุ เป็นข้อมูลของนักศึกษาแต่ละคน
for i in range(10):
    line = input()
    name = line.split(',')
    students[ name[0] ] = int(name[1])

print(students)