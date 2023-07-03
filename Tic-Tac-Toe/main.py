heading = ['  |', '1 |', '2 |', '3 |']
r1 = ['A |', '  |', '  |', '  |']
r2 = ['B |', '  |', '  |', '  |']
r3 = ['C |', '  |', '  |', '  |']

# Set player to 1.
player = 1
symbol = 'X'


def pattern():
    # Prints out the board to play the game on.
    print(heading[0], heading[1], heading[2], heading[3])
    print(r1[0], r1[1], r1[2], r1[3])
    print(r2[0], r2[1], r2[2], r2[3])
    print(r3[0], r3[1], r3[2], r3[3])


# check if row and column are valid.
def valid_move(move_list):
    if move_list[0] == "a" or move_list[0] == "b" or move_list[0] == "c":
        if move_list[1] == "1" or move_list[1] == "2" or move_list[1] == "3":
            return True
        else:
            print(f"Invalid move. Player{player}, try again.")
            return False
    else:
        print(f"Invalid move. Player{player}, try again.")
        return False


# checks if cell is empty and if yes, then puts the symbol.
def modify_row(move_list):
    global symbol
    column = int(move_list[1])

    if player == 1:
        symbol = "X"
    elif player == 2:
        symbol = "O"

    # check for first row
    if move_list[0] == 'a':
        # check for column
        for position in range(1, 4):
            if column == position:
                if r1[position] == '  |':
                    r1[position] = f'{symbol} |'
                    return True
                else:
                    print(f"Cell occupied, try another move Player{player}")
                    return False

    # check for second row
    if move_list[0] == 'b':
        # check for column
        for position in range(1, 4):
            if column == position:
                if r2[position] == '  |':
                    r2[position] = f'{symbol} |'
                    return True
                else:
                    print(f"Cell occupied, try another move Player{player}")
                    return False

    # check for third row
    if move_list[0] == 'c':
        # check for column
        for position in range(1, 4):
            if column == position:
                if r3[position] == '  |':
                    r3[position] = f'{symbol} |'
                    return True
                else:
                    print(f"Cell occupied, try another move Player{player}")
                    return False


def ask_for_input():
    move = input(f"Player{player}, make your move: ").lower()
    move_list = [char for char in move]
    return move_list


def winner():
    cell = f'{symbol} |'

    if r1[1] == cell and r2[1] == cell and r3[1] == cell:
        return False
    elif r1[2] == cell and r2[2] == cell and r3[2] == cell:
        return False
    elif r1[3] == cell and r2[3] == cell and r3[3] == cell:
        return False
    elif r1[1] == cell and r1[2] == cell and r1[3] == cell:
        return False
    elif r2[1] == cell and r2[2] == cell and r2[3] == cell:
        return False
    elif r3[1] == cell and r3[2] == cell and r3[3] == cell:
        return False
    elif r1[1] == cell and r2[2] == cell and r3[3] == cell:
        return False
    elif r1[3] == cell and r2[2] == cell and r3[1] == cell:
        return False
    else:
        return True


def game():
    global player

    pattern()
    print("Player1 is 'X' and Player2 is 'O'. Enter A, B or C for row and 1, 2 or 3 for column. Example: B2")

    game_on = True
    change_made = True
    cells_occupied = 0

    while game_on:
        input_list = ask_for_input()
        validity = valid_move(input_list)

        if validity:
            change_made = modify_row(input_list)
            pattern()

            if change_made:
                cells_occupied += 1
                game_on = winner()

                if not game_on:
                    print(f"Player{player} wins.")
                elif cells_occupied == 9:
                    print("It's a draw.")
                    game_on = False
                else:
                    if player == 1:
                        player = 2
                    else:
                        player = 1


game()
