nums = [128, 64, 32, 16, 8, 4, 2, 1]
binary = input()
binary_list = binary.split(".")
decimal = ""
for index in range(len(binary_list)):
    num = 0
    for i in range(len(list(binary_list[index]))):
        new_list = list(binary_list[index])
        if new_list[i] == "1":
            num += nums[i]
    if index < len(binary_list)-1:
        decimal += str(num) + "."
    else:
        decimal += str(num)

print(decimal)
