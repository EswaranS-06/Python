# 2048 Game in Python
# This code implements a simple version of the 2048 game using Python.

import random
from tabulate import tabulate
from os import system as cls

def display(tiles): #function to display the game board
    cls('cls')
    print(tabulate(tiles, tablefmt='fancy_grid'))
    
def added_value(row):
    i = 1
    while i<=len(row):
        if len(row) <= i:
                return row
        value = row[i - 1] + row [i]
        if value >> 1 == row[i]:
            row[i-1] = value
            row.pop(i)
        else :
            i+=1
    return row
    
def move_left(tiles): #function to move tiles left
    for i in range(4):
        stack = []
        for j in range(4):
            if tiles[i][j] != 0:
                stack.append(tiles[i][j])
        if len(stack) > 1:
            stack = added_value(stack)        
        
        for j in range(len(stack)):
            tiles[i][j] = stack[j]
        for j in range((len(stack)), 4):
            tiles[i][j] = 0
                
def move_right(tiles): #function to move tiles right
    for i in range(4):
        stack = []
        for j in range(4):
            if tiles[i][j] != 0:
                stack.append(tiles[i][j])
        if len(stack) > 1:
            stack = added_value(stack)        
        
        for j in range(4-(len(stack))):
            tiles[i][j] = 0 
        for j in range(4-(len(stack)), 4):
            tiles[i][j] = stack.pop(0)

def move_up(tiles): #function to move tiles up
    for j in range(4):
        stack = []
        for i in range(4):
            if tiles[i][j] != 0:
                stack.append(tiles[i][j])
        if len(stack) > 1:
            stack = added_value(stack)        
        
        for i in range(len(stack)):
            tiles[i][j] = stack[i]
        for i in range((len(stack)), 4):
            tiles[i][j] = 0

def move_down(tiles): #function to move tiles down
      for j in range(4):
        stack = []
        for i in range(4):
            if tiles[i][j] != 0:
                stack.append(tiles[i][j])
        if len(stack) > 1:
            stack = added_value(stack[::-1])[::-1]       
        
        for i in range(4-(len(stack))):
            tiles[i][j] = 0 
        for i in range(4-(len(stack)), 4):
            tiles[i][j] = stack.pop(0)


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
    #tiles = [[0, 2, 0, 0], [2, 0, 0, 2], [2, 2, 4, 8], [0, 0, 0, 8]]
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
    # display(tiles)
    # move_right(tiles)
    # display(tiles)
        
if __name__ == main():
    main()