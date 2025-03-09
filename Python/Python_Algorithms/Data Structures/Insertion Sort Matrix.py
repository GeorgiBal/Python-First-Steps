def insertion_sort_matrix(arr):
    flat_list = [item for sublist in arr for item in sublist]

    # Perform insertion sort on the flattened list
    for i in range(1, len(flat_list)):
        key = flat_list[i]
        j = i - 1
        while j >= 0 and key < flat_list[j]:
            flat_list[j + 1] = flat_list[j]
            j -= 1
        flat_list[j + 1] = key

    # Reshape the sorted list back into 2D array
    rows = len(arr)
    cols = len(arr[0])
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = flat_list[i * cols + j]

    return arr

matrix = [[5, 3, 7, 12],
          [1, 9, 2, 10],
          [8, 6, 4, 11]]
print(insertion_sort_matrix(matrix))