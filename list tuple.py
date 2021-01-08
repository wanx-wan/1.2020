a = [3,5,7,9,10,19,17,15] #list[] tuple()
for i in a:
    print(i)

num = list(map(int,input().split(','))) #ผู้ใช้กรอกค่าเอง
for i in num:
    print(i)

N = int(input()) #Nรอบ
for i in range(N):
    num = input().split(',')
    for i in num:
        print(i)