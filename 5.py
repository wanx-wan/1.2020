def get_box_area(width,length,height):
    if width < 0 or length < 0 or height < 0:
        return 0
    box_area = width * length * height
    return box_area
box1 = get_box_area(4,-4,2)
box2 = get_box_area(width=1,length=1,height=1)
print(box1)