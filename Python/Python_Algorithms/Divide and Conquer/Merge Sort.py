def merge_sort(arr):
    mid = len(arr) // 2
    left = sorted(arr[:mid])
    right = sorted(arr[mid:])
    new_arr = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            new_arr.append(insert)
        elif right[0] > left[0]:
            insert = left.pop(0)
            new_arr.append(insert)

    if len(left) > 0:
        for i in left:
            new_arr.append(i)
    if len(right) > 0:
        for i in right:
            new_arr.append(i)

    return new_arr


arr = [4, 6, 1, 8, 7, 9]
print(merge_sort(arr))
