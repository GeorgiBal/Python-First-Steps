def hex_to_bin(hex_num):
    binary = ""
    dec = int(str(hex_num), 16)
    while dec > 0:
        binary = str(dec % 2) + binary
        dec >>= 1
    return binary


print(hex_to_bin("1a"))
