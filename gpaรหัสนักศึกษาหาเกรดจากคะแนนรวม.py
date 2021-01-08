num = list(map(int,input().split(',')))
n = int(input())
for i in range(n):
    gpa = list(map(float,input().split(',')))
    gpas = sum(gpa) - gpa[0]
    if gpas >= num[0] and gpas < num[1]:
        print(gpa[0],'F')
    elif gpas < num[2]:
        print(gpa[0],'D')
    elif gpas < num[3]:
        print(gpa[0],'C')
    elif gpas < num[4]:
        print(gpa[0],'B')
    elif gpas <=num[5]:
        print(gpa[0],'A')
