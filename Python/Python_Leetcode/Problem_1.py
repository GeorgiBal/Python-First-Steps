def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [seen[remaining], i]
        else:
            seen[value] = i


print(two_sum([3, 2, 4], 6))
