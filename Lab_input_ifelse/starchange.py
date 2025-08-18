n = int(input())
a = input()
b = input()

pair = (a + b) * (n // 2)
last = a * (n % 2)

print(pair + last)
