# tic tac toe
print('Start the game!')
# board
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def board():
    print(f'| {list1[0]} | {list1[1]} | {list1[2]} |\n'
          f'| {list1[3]} | {list1[4]} | {list1[5]} |\n'
          f'| {list1[6]} | {list1[7]} | {list1[8]} |\n')


board()
turn = 0
sign = 'X'

while True:
    # rules
    player = int(input('Player %s choose a number(1 to 9): ' % sign))
    turn += 1
    while player > 9 or player < 1:
        print('Not in range(1 to 9)!')
        player = int(input('Player %s choose a number(1 to 9): ' % sign))
    if 0 < player < 10:
        while list1[player - 1] == 'X' or list1[player - 1] == 'O':
            print('This place is already taken!')
            player = int(input('Player %s choose a number(1 to 9): ' % sign))
            while player > 9 or player < 1:
                print('Not in range(1 to 9)!')
                player = int(input('Player %s choose a number(1 to 9): ' % sign))
        # play
        if player == list1[player - 1]:
            list1[player - 1] = sign
            board()
    # check winning
    if list1[0] == list1[1] == list1[2] or \
            list1[3] == list1[4] == list1[5] or \
            list1[6] == list1[7] == list1[8] or \
            list1[0] == list1[3] == list1[6] or \
            list1[1] == list1[4] == list1[7] or \
            list1[2] == list1[5] == list1[8] or \
            list1[0] == list1[4] == list1[8] or \
            list1[2] == list1[4] == list1[6]:
        print("Player %s wins!" % sign)
        break
    # check tie
    elif turn > 8:
        print('Tie!')
        break
    # switch players
    else:
        if sign == 'O':
            sign = 'X'
        else:
            sign = 'O'
