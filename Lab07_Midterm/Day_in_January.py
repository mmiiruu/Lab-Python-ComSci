x = int(input())
n = int(input())

# ตรวจสอบความถูกต้อง
if x < 1 or x > 7 or n < 1 or n > 31:
    print("ERROR")
else:
    # หาค่าวันของสัปดาห์
    day_index = (n - x) % 7  # 0 = Sunday, 1 = Monday, ..., 6 = Saturday

    if day_index == 0:
        print("Sunday")
    elif day_index == 1:
        print("Monday")
    elif day_index == 2:
        print("Tuesday")
    elif day_index == 3:
        print("Wednesday")
    elif day_index == 4:
        print("Thursday")
    elif day_index == 5:
        print("Friday")
    else:
        print("Saturday")
