x = float(input())       # รับค่าจำนวนจริง
n = int(x)               # แปลงเป็นจำนวนเต็ม

if x == n:               # ถ้าเท่ากับจำนวนเต็ม
    print(f"{n} is an integer.")
else:                    # ถ้าไม่เท่ากับจำนวนเต็ม
    print(f"{x} is not an integer.")
