import math
x = float(input("Enter x : "))
if x < 0:
    fx = math.sqrt(x**2 + 1)
elif x == 0:
    fx = x
elif x <= 99:
    fx = 3*x**2 - (1-x)**2
else:
    fx = 2*x**3 - (x / math.sqrt(x+1))
# ปัดขึ้นเป็นจำนวนเต็ม
fx = math.ceil(fx)
print(f"f({x:.2f}) = {fx}")
