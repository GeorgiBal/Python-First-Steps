def hex_to_dec(hex_num):
    binary = ""
    dec = int(str(hex_num), 16)
    while dec > 0:
        binary = str(dec % 2) + binary
        dec >>= 1

    dec_number = int(binary, 2)
    return dec_number


print(hex_to_dec("a12"))
