n = int(input())
c1 = input()
c2 = input()

pair = (c1 + c2) * (n // 2)
last = c1 * (n % 2)

print(pair + last)
