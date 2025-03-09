rows, cols = map(int, input().split(","))
board = [[100] * cols for i in range(rows)]


def update_board(r, c, damage):
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            board[i][j] = max(0, board[i][j] - (damage if i == r and j == c else 10))


while True:
    try:
        line = input()
        if line == "GAME OVER":
            break
        r, c, damage = map(int, line.split(","))
        update_board(r, c, damage)
    except:
        continue

for row in board:
    print(row)
