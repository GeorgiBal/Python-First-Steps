def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [1, 2, 3, 4, 5]
print(search(arr, 3))