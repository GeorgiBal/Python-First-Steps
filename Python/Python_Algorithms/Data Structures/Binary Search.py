def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid -1
            binary_search(arr, target, start, end)
        elif arr[mid] < target:
            start = mid + 1
            binary_search(arr, target, start, end)
        else:
            return mid

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 3
print(binary_search(arr, target, 0, len(arr) - 1))