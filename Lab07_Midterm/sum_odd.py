n = int(input())   # รับจำนวนเต็มบวกจากผู้ใช้

total = 0          # ตัวแปรเก็บผลรวมเลขคี่
found = False      # ตัวแปรตรวจว่ามีเลขคี่หรือไม่

while n > 0:
    digit = n % 10        # หารเศษ 10 ได้เลขหลักสุดท้าย
    if digit % 2 == 1:    # ถ้าเลขเป็นคี่
        total += digit
        found = True
    n //= 10              # ตัดเลขหลักสุดท้ายทิ้ง

if found:
    print(total)
else:
    print(-1)
