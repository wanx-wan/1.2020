name = 'Ubonratchathani University and Ubonratchathani Province'
print(name.count('Ubonratchathani')) #นับจำนวนประโยค
print(name.startswith('and')) #ตรวจสอบคำขึ้นต้น
if name.startswith('and'):
    print('1')
else:
    print('2')
print(name.endswith('Province')) #ตรวจสอบคำลงท้าย
if name.endswith('Province'):
    print('KK')
else:
    print('JJ')