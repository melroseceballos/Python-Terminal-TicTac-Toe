# Clear the terminal on linux and mac computers
import os
os.system('clear')

# GAME STARTS HERE

# Create a greeter for the game
print("--- Let's Play Tic Tac Toe ! ---")
print('\n')
# Define a 3x3 list to represent the Tic Tac Toe board.
    #put numbers in variables and then use .replace to change it to the shape X|O?
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

user_x = int(input ("Select a number you would like X to go?"))
print(user_x)
if (user_x == 1):
    .replace(1, 'x')
# Define a function to prompt the user to input their move.
    #create a function with .replace()?

# Define a function to check if a player has won.
# Define a function to alternate between players and execute their moves.
# Define a function to check if the game is over.
# Define a main function that executes the game logic.