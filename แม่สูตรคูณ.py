z = int(input('ต้องการสูตรคูณแม่ไหน '))
zz = int(input('สิ้นสุดสูตรคูณแม่ไหน'))
for i in range(z,zz):
    print('แม่ ',i)
    for n in range(1,13):
        print(i,'x',n,'=',i*n)
        