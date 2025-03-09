nums = [1, 2, 2]
no_dubs = []

for i in range(len(nums)):
    if nums[i] in no_dubs:
        pass
    else:
        no_dubs.append(nums[i])

print(no_dubs)
