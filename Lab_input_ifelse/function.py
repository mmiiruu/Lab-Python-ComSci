import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
a1 = (x ** y) + z 
a2 = math.cos(2 * math.pi) + math.log(x)
a3 = abs(x) + abs(y)
a4 = math.sqrt(x**2 + y**2 + z**2)
a5 = math.sin(x)**2 + math.cos(x)**2
a6 = (x + y)**(1/5)
a7 = math.exp(x * math.log(y))
print(f"a1 = {a1:.2f}")
print(f"a2 = {a2:.2f}")
print(f"a3 = {a3:.2f}")
print(f"a4 = {a4:.2f}")
print(f"a5 = {a5:.2f}")
print(f"a6 = {a6:.2f}")
print(f"a7 = {a7:.2f}")