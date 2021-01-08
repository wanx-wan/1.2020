n,m = eval(input()) #หาเกรดตามทิศ
gpa = []
for i in range(n):
    tmp = input()
    gpa.append(tmp)
stx,sty = eval(input())
for i in range(2):
    tmp = input().split(',')
    a = tmp[0]
    b = int(tmp[1])
    if a == 'W':
        stx -= b
    elif a == 'S':
        stx += b
    elif a == 'A':
        sty -= b
    else:
        sty += b
print(gpa[stx][sty])