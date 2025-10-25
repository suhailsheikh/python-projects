import random

board = {
    '1' : ' ',
    '2' : ' ',
    '3' : ' ',
    '4' : ' ',
    '5' : ' ',
    '6' : ' ',
    '7' : ' ',
    '8' : ' ',
    '9' : ' '
}

def print_board():
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

print('===========')
print('Tic Tac Toe'.upper())
print('===========')

# Variables
player_one = ''
player_two = ''

winning_combinations = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']
]

# Check for winner
def check_winner(symbol):
    for combo in winning_combinations:
        if all(board[pos] == symbol for pos in combo):
            return True
    return False

# Check for a draw
def check_draw():
    return all(space != ' ' for space in board.values())

# Validate the player selection
while True:
    player_one = input("Enter 'X' or 'O': ").strip()

    if player_one.upper() in ['X', 'O']:
        break
    else:
        print("Invalid character. Please enter 'X' or 'O'")

# Assign the remaining symbol to Player 2
player_two = 'O' if player_one == 'X' else 'X'

# Play game
while True:
    print_board()

    # Player 1 Move
    while True:
        player_one_selection = input('Your move Player 1. Choose a position (1-9): ').strip()
        if player_one_selection in board and board[player_one_selection] == ' ':
            board[player_one_selection] = player_one
            break
        else:
            print("Invalid move. Try again.")

    # Check if Player 1 wins
    if check_winner(player_one):
        print_board()
        print("Player 1 wins!")
        break

    # Check for draw before computer move
    if check_draw():
        print_board()
        print("It's a draw!")
        break

    # Computer (Player 2) Move
    empty_cells = [k for k, v in board.items() if v == ' ']
    player_two_selection = random.choice(empty_cells)
    board[player_two_selection] = player_two
    print(f"Computer chooses position {player_two_selection}")

    # Check if Computer wins
    if check_winner(player_two):
        print_board()
        print("Computer (Player 2) wins!")
        break

    # Check for draw after computer move
    if check_draw():
        print_board()
        print("It's a draw!")
        break