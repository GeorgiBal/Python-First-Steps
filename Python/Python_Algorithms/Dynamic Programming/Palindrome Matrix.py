def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def palindromic_path(string, arr, i, j, cols, rows):

    if j < cols - 1 or i < rows - 1:
        if i < rows - 1:
            palindromic_path(string + arr[i][j], arr, i + 1, j, cols, rows)
        if j < cols - 1:
            palindromic_path(string + arr[i][j], arr, i, j + 1, cols, rows)
    else:
        string += arr[rows - 1][cols - 1]
        if is_palindrome(string):
            print(string)

arr = [['a', 'a', 'a'],
     ['b', 'b', 'a'],
     ['a', 'b', 'a']]

string = ""
palindromic_path(string, arr, 0, 0, 3, 3)