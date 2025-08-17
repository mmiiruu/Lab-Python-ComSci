target = 72        # กำหนดค่าเป้าหมาย
count = 0          # ตัวนับจำนวนครั้งที่ทาย

while True:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess < 0 or guess > 100:
        print("Sorry, your guess is out of range.")
    elif guess < target:
        print("Sorry, your guess is too low.")
    elif guess > target:
        print("Sorry, your guess is too high.")
    else:  # guess == target
        print("Congratulations, your guess is correct.")
        print(f"Total number of guesses is {count}.")
        break
