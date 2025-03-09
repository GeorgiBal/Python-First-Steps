x, y = input().split(',')
x = int(x)
y = int(y)
board = []
life = 100


def print_board():
    for rows in range(x):
        for columns in range(y):
            print(board[rows][columns], end=' ')
        print()


for i in range(x):
    z = []
    for j in range(y):
        z.append(life)
    board.append(z)

print_board()

minus = 0

while True:
    text = input()
    if text == 'GAME OVER':
        print_board()
        break
    else:
        try:
            text = text.split(',')
            row = int(text[0])
            column = int(text[1])
            damage = int(text[-1])
            if 1 <= damage <= 30:
                minus = 5
            elif 30 < damage <= 70:
                minus = 10
            elif damage > 70:
                minus = (damage / 100) * 20
            else:
                minus = 0
            board[row][column] -= round(damage - minus)
            for r in range(row-1, row+2):
                for c in range(column-1, column+2):
                    if any([r < 0, c < 0, r >= len(board), c >= len(board)]):
                        pass
                    else:
                        board[r][c] -= round(minus)
        except IndexError:
            pass
    print_board()
