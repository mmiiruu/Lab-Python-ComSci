number = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

if number < 0:
    print("Invalid number.")
if digit < 0 or digit > 9:
    print("Invalid digit.")
if number>=0 and 0 <= digit <=9 :
    count = 0
    temp = number
    while temp > 0:
        if temp % 10 == digit:
            count += 1
        temp //= 10
    if count == 1:
        print(f"Digit {digit} occurs 1 time.")
    else:
        print(f"Digit {digit} occurs {count} times.")
