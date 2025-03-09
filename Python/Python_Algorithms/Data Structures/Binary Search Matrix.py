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

def binary_search_matrix(matrix, target, start, end):
    for i in range(len(matrix)):
        if target in matrix[i]:
            j = binary_search(matrix[i], target, start, end)
            return i, j

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
target = 2
print(binary_search_matrix(matrix, target, 0, len(matrix) - 1))