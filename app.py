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

user_x = int(input ("Player X, Select a number you would like X to go?"))
print(user_x)

# To change 1 (player X)
if (user_x == 1):
   top_three = f" | 'X' | {top_three[1]} | {top_three[2]} | .replace('1','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | X | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')
# to change 2
if (user_x == 1):
   top_three = f" | {top_three[0]} | 'X' | {top_three[2]} | .replace('2','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | X | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

# User X 3
if (user_x == 3):
   top_three = f" | {top_three[0]} | {top_three[1]} | 'X' | .replace('3','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | X |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

# user-x 4
if (user_x == 4):
   middle = f" | 'X' | {middle[1]}  | {middle[2]} | .replace('4','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | X | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

#USER X 5
if (user_x == 5):
   middle = f" | {middle[0]} | 'X'  | {middle[2]} | .replace('5','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | X | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

#USER X-6
if (user_x == 6):
   middle = f" | {middle[0]} | {middle[1]}  | 'X' | .replace('6','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | X | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

#USER X-7
if (user_x == 4):
   bottom = f" | 'X' | {bottom[1]} | {bottom[2]} | .replace('7','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | X | {bottom[1]} | {bottom[2]} | ")
print("   ------------- ")
print('\n')

#USER X-8
if (user_x == 4):
   bottom = f" | {bottom[0]} | 'X'| {bottom[2]} | .replace('8','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | X | {bottom[2]} | ")
print("   ------------- ")
print('\n')

#USER X-9
if (user_x == 4):
   bottom = f" | {bottom[0]}| {bottom[1]} | 'X' | .replace('9','X')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | {top_three[0]} | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | X | ")
print("   ------------- ")
print('\n')


# PLAYER O
user_O = int(input('Player O, select a number you would like O to go')) 
if (user_O == 1):
   top_three = f" | 'O' | {top_three[1]} | {top_three[2]} | .replace('1','O')"
print("     B O A R D ")
print("   ------------- ")
top_three = ('1', '2', '3')
print(f"   | O | {top_three[1]} | {top_three[2]} |")
print("   ------------- ")
middle = ('4', '5', '6')
print(f"   | {middle[0]} | {middle[1]} | {middle[2]} | ")
print("   ------------- ")
bottom = ('7', '8', '9')
print(f"   | {bottom[0]} | {bottom[1]} | X | ")
print("   ------------- ")
print('\n')

# Define a function to check if a player has won.
# Define a function to alternate between players and execute their moves.
# Define a function to check if the game is over.
# Define a main function that executes the game logic.