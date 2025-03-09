def hex_to_rgb(hex_num):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex_num[i:i + 2], 16)
        rgb.append(decimal)

    return tuple(rgb)


print(hex_to_rgb('FF001E'))