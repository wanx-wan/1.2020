name = '  wancharoenupamai  '
name=name.strip( ) #ซ้ายขวาเพิ่ม r หรือ l หน้า strip
print(name)
print(name[:3])
print(name[-3:])
print(len(name))
print(name.upper()) #แปลงเป็นตัวพิมพ์ใหญ่
#แปลงเป็นตัวพิมพ์เล็กใช้ lower
print(name.capitalize()) #แปลงตัวแรกเป็นตัวพิมพ์ใหญ่
print(name.replace('wan','Jong')) #แทนที่ประโยคที่ต้องการ
x = 'mai' in name #เช็คข้อความ
print(x) 
if x:
    name = name.replace('wan','Jong')
print(name)