import math

while True:
    # รับค่าพิกัดจุด a
    print("<<Point a>>")
    xa = int(input("Enter x coordinate: "))
    ya = int(input("Enter y coordinate: "))

    # รับค่าพิกัดจุด b
    print("<<Point b>>")
    xb = int(input("Enter x coordinate: "))
    yb = int(input("Enter y coordinate: "))

    # เงื่อนไขหยุดโปรแกรม
    if (xa, ya) == (0, 0) and (xb, yb) == (0, 0):
        print("Goodbye")
        break

    # คำนวณระยะทาง
    horizontal_distance = abs(xb - xa)
    vertical_distance = abs(yb - ya)
    euclidean_distance = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    # แสดงผลระยะทาง
    print(f"Distance between ({xa}, {ya}) and ({xb}, {yb}):")
    print(f"Euclidean distance is {euclidean_distance:.2f}.")
    print(f"Horizontal distance is {horizontal_distance}.")
    print(f"Vertical distance is {vertical_distance}.")

    # หาทิศทาง
    dx = xb - xa
    dy = yb - ya

    if dx == 0 and dy == 0:
        direction = "nowhere"
    elif dx == 0:
        direction = "north" if dy > 0 else "south"
    elif dy == 0:
        direction = "east" if dx > 0 else "west"
    elif dx > 0 and dy > 0:
        direction = "north-east"
    elif dx < 0 and dy > 0:
        direction = "north-west"
    elif dx > 0 and dy < 0:
        direction = "south-east"
    else:
        direction = "south-west"

    print(f"We are going {direction}.")
