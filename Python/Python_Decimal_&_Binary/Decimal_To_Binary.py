nums = [128, 64, 32, 16, 8, 4, 2, 1]
decimal = input()
decimal_list = decimal.split(".")
binary = ""
for index in range(len(decimal_list)):
    subtract = int(decimal_list[index])
    for i in range(len(nums)):
        if subtract - nums[i] >= 0:
            subtract -= nums[i]
            binary += "1"
        else:
            binary += "0"
    if index < len(decimal_list)-1:
        binary += "."

print(binary)
