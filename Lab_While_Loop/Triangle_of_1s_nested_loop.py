height = int(input())

if height <= 0:
    exit()
    
i = 0
while i < height:
    current_line = ""
    
    leading_spaces_count = 2*height - (2 + 2*i)
    
    # print ตัวช่องว่างตามจำนวนครั้งที่คิดไว้
    # --------------------------------------
    j = 0
    while j < leading_spaces_count:
        current_line += " "
        j += 1
    # --------------------------------------
    
    if i == 0:
        current_line += "1"
    else:
        current_line += "1"

        inner_spaces_count = 3 + (i - 1) * 4
        
        # print ตัวช่องว่างตามจำนวนครั้งที่คิดไว้
        # ----------------------------------
        k = 0
        while k < inner_spaces_count:
            current_line += " "
            k += 1
        # ----------------------------------
            
        current_line += "1"
    
    print(current_line)
    i += 1
