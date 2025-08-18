n = int(input())
c = input()

i = 0
while i < n:
    current_line = ''
    
    j = 0
    while j < i+1:
        current_line += c
        j += 1
        
    print(current_line)
    i += 1
