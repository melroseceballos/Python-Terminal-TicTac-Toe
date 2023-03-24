# Clear the terminal on linux and mac computers
import os
os.system('clear')

# GAME STARTS HERE

# Create a greeter for the game
print("--- Let's Play Tic Tac Toe ! ---")
print('\n')
# Create a function for the board
def tictac_board (board):
    print("     B O A R D ")
    print("   ------------- ")
    print(f"   | {board[0][0]} | {board [0][1]} | {board [0][2]} |")
    print("   ------------- ")
    print(f"   | {board [1][0]} | {board[1][1]} | {board[2][2]} | ")
    print("   ------------- ")
    print(f"   | {board[2][0]} | {board[2][1]} | {board[2][2]} | ")
    print("   ------------- ")
    print('\n')
board = [['1','2','3'], ['4','5','6'],['7','8','9']]

tictac_board(board)

#GAME LOOP HERE
    #Player X
while True:
    player_x = int(input("Place X in board by selecting number"))
    row = (player_x - 1) // 3
    col = (player_x - 1) % 3
    board[row][col] = 'X'
    os.system('clear')
    tictac_board(board)

    #Player O
    player_o = int(input("Player X: Place O in the board by selecting a number"))
    row = (player_o - 1) // 3
    col = (player_o - 1) % 3
    board[row] [col] = 'O'
    os.system('clear')
    tictac_board(board)

    # PROMPT IF PLAYERS CHOOSE SAME NUMBER
    if player_x == player_o:
        print('Player O: Number already chosen by Player X, please choose a different number')
        break
    else:
        print('Number already chosen by Player O, please choose a different number')
        break




