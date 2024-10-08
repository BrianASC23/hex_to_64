def hex_to_64(hex_input):
    base64_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-"
    bytes = ""

    length_of_hex = len(hex_input)
    for i in range(0, length_of_hex, 2):
        hex_pair = hex_input[i:i+2]
        decimal = int(hex_pair, 16)
        bits_before = bin(decimal)
        bits_after = bits_before[2:]
        bits_after = '0' * (8 - len(bits_after)) + bits_after
        bytes = bytes + bits_after

    
    output = ""
    length_of_string = len(bytes)
    for i in range(0, length_of_string, 6):
        six_bits = bytes[i:i+6]
        
        while len(six_bits) < 6:
           
            six_bits = six_bits + '0'
    
        key = int(six_bits, 2)
        output += base64_key[key]


    print(output)
    return output


