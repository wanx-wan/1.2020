n = int(input()) #จำนวนครั้ง รหัสวิชา ชื่อวิชา รหัสนักศึกษา 
students = {}
for i in range(n):
    course = input().split(',')
    x = int(course[2])
    for j in range(x):
        strlist = input().split(',')
        name = strlist[0]
        scores = map(int, strlist[1:])
        if name in students.keys():
            students[name][course[0]] = sum(scores)
        else:
            students[name] = {
                course[0]: sum(scores)
            }
for name in sorted(students.keys()):
    print(f'{name}')
    for course in sorted(students[name].keys()):
        print(f'{course}: {students[name][course]}