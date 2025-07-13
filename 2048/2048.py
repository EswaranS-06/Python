# 2048 Game in Python
# This code implements a simple version of the 2048 game using Python.

import random
from tabulate import tabulate

def display(tiles): #function to display the game board
    print(tabulate(tiles, tablefmt='fancy_grid'))
    
def move_left(tiles): #function to move tiles left
    pass

def move_right(tiles): #function to move tiles right
    pass

def move_up(tiles): #function to move tiles up
    pass

def move_down(tiles): #function to move tiles down
      pass

def add_new_tile(tiles): #function to add a new tile (2 or 4) to the board
    while True:
        for i in [random.randrange(0,4)]:
            for j in [random.randrange(0,4)]:
                if tiles[i][j] == 0:
                    value = random.randrange(1, 3) * 2  
                    tiles[i][j] = value
                    return


def check_game_over(tiles): #function to check if the game is over
    if not any(0 in row for row in tiles):
        return True

def main():
    tiles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #initialize the game board
    add_new_tile(tiles) #add the first tile
    add_new_tile(tiles) #add the second tile
    
    while True:
        display(tiles) #display the current state of the board
        move = input("Enter move (w/a/s/d): ").strip().lower() #get user input for move
        
        if move == 'a':
            move_left(tiles)
        elif move == 'd':
            move_right(tiles)
        elif move == 'w':
            move_up(tiles)
        elif move == 's':
            move_down(tiles)
        else:
            print("Invalid move! Please enter w/a/s/d.")
            continue
        
        if check_game_over(tiles): #check if the game is over
            display(tiles)
            print("Game Over!")
            break
        
        add_new_tile(tiles) #add a new tile after each valid move
        
if __name__ == main():
    main()