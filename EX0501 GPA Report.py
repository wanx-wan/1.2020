'''EX0501 GPA Report กรอกจำนวนที่ต้องการ แล้วกรอกรหัสนักศึกษา,เกรด เพื่อหาผลต่างของเกรด'''
ids = []
gpas = []
n = int(input())

for i in range(n):
    line = input().split(',')
    ids.append( line[0] )
    gpas.append( float(line[1]) )

avg = sum(gpas)/len(gpas)

for i in range(len(ids)):
    print(f'{ids[i]},{abs(gpas[i]-avg):.2f}')