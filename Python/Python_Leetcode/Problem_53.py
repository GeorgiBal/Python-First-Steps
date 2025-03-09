nums = input()
nums_list = nums.split(",")
print(nums_list)
total = 0
for i in nums_list:
    total += int(i)

print(total)