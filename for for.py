for i in range(2): #รหัสวิชา สาขา คะแนนรวม
    data = input().split(',')
    for j in range(int(data[2])):
        data2 = input().split(',')
        print(sum(map(int,data2[1:])))