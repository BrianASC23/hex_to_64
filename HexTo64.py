

def hex_to_base_64(input):
    
    hex_list = input.split()
    
    base64_array = []
    
    for hex_num, hex in enumerate(hex_list):
        sum = 0
        word = ''
        for i, char in enumerate(hex):
            if i == 0:
                exp = 1
            elif i == 1:
                exp = 0
            if char.isdigit():
                num = char
            else:
                num = ord(char) - ord('a') + 10
        
            sum += int(num) * 16**(exp)
        #Convert to Base 64
        while sum != 0:
            remainder = sum % 64
            print("remainder is", remainder)
            if remainder < 26:
                remainder = chr(ord('A') + remainder)
            elif remainder < 51:
                remainder = chr(ord('A') + remainder + 6)
            elif remainder < 62:
                remainder = chr(remainder)
            elif remainder == 62:
                remainder = '+'
            elif remainder == 63:
                remainder = '-'

            word = remainder + word
            sum = (sum)//64 
            
        base64_array.append(word)   
    return base64_array








