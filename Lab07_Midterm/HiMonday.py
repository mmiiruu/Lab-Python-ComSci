# รับหมายเลขวัน (1=Sunday, ..., 7=Saturday)
day_num = int(input())
hour = int(input())
minute = int(input())

# แปลงหมายเลขวันเป็นชื่อภาษาอังกฤษ
if day_num == 1:
    day_name = "sunday"
elif day_num == 2:
    day_name = "monday"
elif day_num == 3:
    day_name = "tuesday"
elif day_num == 4:
    day_name = "wednesday"
elif day_num == 5:
    day_name = "thursday"
elif day_num == 6:
    day_name = "friday"
else:
    day_name = "saturday"

# แปลงเวลาเป็นนาทีรวม
time = hour * 60 + minute

# ตรวจสอบช่วงเวลา
if 4*60 + 1 <= time <= 12*60:
    part = "morning"
elif 12*60 + 1 <= time <= 18*60:
    part = "afternoon"
elif 18*60 + 1 <= time <= 22*60:
    part = "evening"
else:
    part = "night"

# แสดงผลลัพธ์
print(f"good-{part}-{day_name}.png")