n = int(input())  # รับเลขจำนวนเต็ม

if n <= 0:        # ตรวจสอบว่าเป็น 0 หรือเลขลบ
    print("ERROR")
else:
    while n > 0:
        digit = n % 10    # หาหลักหน่วย
        print(digit)      # พิมพ์หลักนั้น
        n //= 10          # ตัดหลักหน่วยออก
