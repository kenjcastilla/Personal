"""Kendall Castilla
This is my Python Tic Tac Toe game inpsired by Garrett Halstein."""

#For the board, we'll create a 2d list which will hold the spaces and their respective values.
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board(board):
    """This function displays the board for the user to see. """
    for row in board:
        for space in row:
            print(f' {space} ', end='')
        print(' ')

def quit(user_input):
    """Takes in user input and determines whether the user wishes to quit or keep playing. """
    if user_input.lower() == 'q':
        print("See you later!")
        return True
    else:
        return False

def check_input(user_input):
    """Check if the input is a number and if it is a valid number (1-9)."""
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    if not isvalidnum(user_input):
        return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print('That is not a number.')
        return False
    else:
        return True

def isvalidnum(user_input):
    if user_input not in range(1, 10):
        if user_input > 9:
            print("That number is too big.")
        else:
            print("That number is too small.")
        return False
    else:
        return True

def isoccupied(board, pair):
    """Check if the desired space is already occupied by a marker."""
    row = pair[0]
    col = pair[1]
    if board[row][col] == '-' or board[row][col] == ' ':
       return False
    return True

def orderedpair(user_input):
    """Convert user input into ordered pair resembling index in list for the board."""
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return  (row, col)

def curr_player(player):
    if player: return 'x'
    else: return 'o'
def add_marker(board, pair, player):
    """Place marker at designated index."""
    row = pair[0]
    col = pair[1]
    board[row][col] = active_player

def iswinner(board, player):
    """See if anyone has won by checking rows, columns, and diagonals."""
    if check_row(board, player) or check_col(board, player) or check_diag(board, player):
        return True
    else: return False

def check_row(board, player):
    """Check to see if any rows are of one marker."""
    for row in board:
        complete_row = True
        for space in row:
            if space != player:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(board, player):
    """Check to see if any columns are of one marker."""
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != player:
                complete_col = False
        if complete_col: return True
    return False

def check_diag(board, player):
    """Check to see if either diagonals are of one marker."""
    complete_diag = True
    for i in range(3):
        if board[i][i] != player:
            complete_diag = False
    if complete_diag: return True

    complete_diag = True
    for i in range(2, -1, -1):
        if board[i][2-i] != player:
            complete_diag = False
        if complete_diag: return True
    return False


player=True;
while True:
    active_player = curr_player(player)
    print_board(board)
    user_input = input('Enter a number 1-9 to choose where to place your marker. Enter \'q\' to exit: ')
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try inputting a number again.")
        continue
    user_input = int(user_input) - 1 #Because we're using a list which starts indexing from 0
    pair = orderedpair(user_input)
    if isoccupied(board, pair):
        print("Please try a different space. That space is occupied.")
        continue
    add_marker(board, pair, active_player)
    if iswinner(board, active_player):
        print_board(board)
        replay = input(f"Player {active_player.upper()} won! Do you want to play again? (y/n): ")
        if replay.lower() == 'y': continue
        else: break
    player = not player