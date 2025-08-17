roll_count = 0
first_roll = True
target = 0

while True:
    # รับแต้มลูกเต๋า 2 ลูก
    d1 = int(input())
    d2 = int(input())

    # ตรวจสอบว่าลูกเต๋าถูกต้องหรือไม่
    if d1 < 1 or d1 > 6 or d2 < 1 or d2 > 6:
        print("ERROR")
        continue  # เริ่มรอบใหม่โดยไม่เพิ่มจำนวนครั้ง

    roll_count += 1  # นับจำนวนครั้งที่โยน
    total = d1 + d2

    if first_roll:
        first_roll = False
        if total == 7 or total == 11:
            print(roll_count, total, "W")
            break
        elif total == 2 or total == 3 or total == 12:
            print(roll_count, total, "L")
            break
        else:
            target = total  # กำหนดแต้มเป้าหมาย
    else:
        if total == target:
            print(roll_count, total, "W")
            break
        elif total == 7:
            print(roll_count, total, "L")
            break
