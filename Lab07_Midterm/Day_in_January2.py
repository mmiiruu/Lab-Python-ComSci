# รับวันของสัปดาห์ของวันที่ 1 มกราคม
first_day = input().strip()
# รับวันที่ที่ต้องการหา
n = int(input())

# ตรวจสอบข้อมูลเบื้องต้น
if n < 1 or n > 31:
    print("ERROR")
else:
    # แปลงชื่อวันเป็นตัวเลข 0-6
    if first_day == "Sunday":
        start_index = 0
    elif first_day == "Monday":
        start_index = 1
    elif first_day == "Tuesday":
        start_index = 2
    elif first_day == "Wednesday":
        start_index = 3
    elif first_day == "Thursday":
        start_index = 4
    elif first_day == "Friday":
        start_index = 5
    elif first_day == "Saturday":
        start_index = 6
    else:
        print("ERROR")
        exit()

    # คำนวณวัน
    day_index = (start_index + (n - 1)) % 7

    # แปลงกลับเป็นชื่อวัน
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
    elif day_index == 6:
        print("Saturday")
