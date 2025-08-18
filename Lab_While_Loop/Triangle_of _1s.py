height = int(input())

i = 0
while i < height:
    current_line = ""
    
    leading_spaces_count = 2*height - (2 + 2*i)
    current_line += " " * leading_spaces_count
    
    if i == 0:
        current_line += "1"
    else:
        current_line += "1"

        inner_spaces_count = 3 + (i - 1) * 4
        current_line += " " * inner_spaces_count
        current_line += "1"
    
    print(current_line)
    i += 1
