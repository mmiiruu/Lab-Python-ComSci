# รับค่าตัวเลข 3 ตัว
a = int(input())
b = int(input())
c = int(input())

# หาตัวที่ใหญ่ที่สุด (ให้เป็นด้านยาวสุด)
if a > b and a > c:
    x, y, z = b, c, a
elif b > a and b > c:
    x, y, z = a, c, b
else:
    x, y, z = a, b, c

# ตรวจสอบตามสูตรพีทาโกรัส
if x*x + y*y == z*z:
    print(True)
else:
    print(False)
