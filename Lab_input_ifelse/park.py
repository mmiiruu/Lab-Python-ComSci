hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))

# ตรวจสอบ input
if hours < 0 or minutes < 0 or minutes >= 60:
    print("Input Error!")
else:
    total_minutes = hours * 60 + minutes

    if total_minutes <= 15:
        print("No charge, thanks.")
    else:
        # ปัดเศษนาทีเป็นชั่วโมง
        if minutes > 0:
            total_hours = hours + 1
        else:
            total_hours = hours

        if total_hours <= 2:
            fee = 10
        elif total_hours > 2:
            fee = 10 + (total_hours - 2) * 10

        print("Total amount due is", fee, "Bahts.")