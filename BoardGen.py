'''
Programmer: Cody McNealy
Last Edited: 05/07/2018
Program: Game Board Generator File
'''
import random
import os
from msvcrt import getch

#asks for user input for how many rows and columns then returns a board using "."
def CreateBoard():
    board = []
    while True:
        print("What size dungeon would you like?")
        print("1) Small\n2) Medium\n3) Large\n")
        userInput = ord(getch())
       
        if userInput == 49: #1 on keyboard
            row = random.randint(5,10)
            col = row
            break
        elif userInput == 50: #2 on keyboard
            row = random.randint(11,20)
            col = row
            break
        elif userInput == 51: #3 on keyboard
            row = random.randint(25,40)
            col = row
            break
        else:
            print("Invalid selection! Press ENTER to try again!")
            input()
            os.system('cls')
    os.system('cls')

    for i in range(0,row):
        board.append(["."] * col)
    return board

#prints out the board for the user to see
def ShowBoard(board):
    for row in board:
        print (" ".join(row))

#randomly places a @ where the players col and row is        
def PlacePlayer(board, player):
    row = random.randint(0,len(board)-1)
    col = random.randint(0,len(board[0])-1)
    board[row][col] = "@"
    player["row"] = row
    player["col"] = col
    return board, player