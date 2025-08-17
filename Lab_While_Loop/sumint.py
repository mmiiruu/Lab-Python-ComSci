n = int(input())

while n >= 10:  # ทำซ้ำจนตัวเลขเหลือหลักเดียว
    total = 0
    temp = n
    while temp > 0:  # หาผลรวมของทุกหลัก
        digit = temp % 10
        total += digit
        temp = temp // 10
    n = total  # อัปเดตตัวเลขด้วยผลรวม

print(n)
