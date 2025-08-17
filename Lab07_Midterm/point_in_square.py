print("Upper left corner coordinate:")
x1 = float(input("  << x axis: "))
y1 = float(input("  << y axis: "))

width = float(input("  << Eastern: "))
height = float(input("  << Southern: "))

x2 = x1 + width
y2 = y1 - height

print("Enter a coordinate:")
px = float(input("  << x axis: "))
py = float(input("  << y axis: "))

if x1 <= px <= x2 and y2 <= py <= y1:
    result = "inside"
else:
    result = "not inside"

print(f">>> ({px:.2f}, {py:.2f}) is {result} the rectangle.")
