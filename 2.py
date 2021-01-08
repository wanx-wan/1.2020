#2.py

import pyautogui as pg
import time

def CopyText(nextline=0):
    
    #-ใช้เมาส์คลิกไปยังตำแหน่งที่ต้องการก็อปปี้ (ด้านหน้า)
    #x=406, y=435

    time.sleep(1) #รอ1วินาที
    start_point = (406,435 + nextline)
    pg.click (start_point)

    #-ลากไปให้สุดบรรทัด

    end_point =(449,436 + nextline) #436+12
    pg.dragTo(end_point)

    #-กดปุ่ม Ctrl+C เพิ้อก็อปปี้

    pg.hotkey('ctrl','c')
    #-ขยับเมาส์ไปทางด้านซ้าย
    left_notepad = (95,436 + nextline)
    pg.click(left_notepad)
    #-กด Ctrl+V เพื่อวาง แล้วกด Enter
    pg.hotkey('ctrl','v','enter')

for i in range(3):
    CopyText(12)
