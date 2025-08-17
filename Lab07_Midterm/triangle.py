a = int(input())
b = int(input())
c = int(input())

# เช็กทุกกรณีที่เป็นด้านมุมฉาก
if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print(True)
else:
    print(False)
