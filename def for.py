def grade(score): #เกรดเฉลี่ยแสดงค่าก่อนเกรด
    return 'FDCBA'[sum([1 for i in (50,60,70,80) if score > i ])]

gpa = []
for i in range(10):
    gpas = float(input())
    gpa.append( [gpas, grade(gpas)] )

numgpa = sorted(gpa, reverse=True)
for gpa in numgpa:
    print(f'{gpa[1]},{gpa[0]}')