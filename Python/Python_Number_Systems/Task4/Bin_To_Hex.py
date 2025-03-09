def bin_to_hex(binary):
    hex_num = ""
    dec = int(str(binary), 2)
    while int(dec) > 0:
        digit = int(dec) % 16
        if digit < 10:
            hex_num += str(digit)
        else:
            hex_num += chr(digit + 55)
        dec /= 16
    return hex_num[::-1]


print(bin_to_hex(1111))
