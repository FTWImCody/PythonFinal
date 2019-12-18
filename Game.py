'''
Programmer: Cody McNealy
Date Submitted: 05/07/2018
Program: Game Main File
'''
import os
import sys
import time
from player import *
from BoardGen import *
from myTools import *
from TreasureGen import *
from msvcrt import getch

#All the main gameplay goes into the Main() function
def main():
    print("Welcome to Ankaria!") #Intro Screen
    time.sleep(1)
    os.system('cls')
    print("In the world of Ankaria you will fight bosses, collect treasures and level up from the treasures you find!")
    print("There are 11 Treasures to collect and once you collect them all, YOU WIN!")
    print("Sounds easy right? But if you die then you have to start over from last save or start a new game!")
    print("Press ENTER to continue...")
    input()
    os.system('cls')
    while True:
        #opens the Main Menu of the game showing the user 3 options: New Game, Load Game or Exit
        while True:
            print("Ankaria\n")
            print("Main Menu")
            print("1) New Game\n2) Load Game\n3) Exit\n")
            userInput = ord(getch())
            if userInput == 49: #1 on keyboard New Game
                os.system('cls')
                #assigning the Treasures in a list
                treasuresList = "Gold Bar~Dragonkin Journal~Effigy~Chalice~Stack of Gold Coins~Green Partyhat~Purple Partyhat~Blue Partyhat~Yellow Partyhat~White Partyhat~Big ol' Pile of Nothing".split("~")
                while True:	#Game Building Loop
                    player = GenPlayer(5)
                    print("Name: " + str(player["name"]))
                    print("History: " + str(player["history"]))
                    print("Attack: " + str(player["attack"]))
                    print("Defense: " + str(player["defense"]))
                    print("Health: " + str(player["health"]))
                    print("\nDo you like this character?(Y/N)")
                    userInput = ord(getch())
                    if userInput in (121, 89): #yY on keyboard
                        break
                    elif userInput in (110, 78): #nN on keyboard
                        os.system('cls')
                    else:
                        print("Invalid selection! Press ENTER to try again!")
                        input()
                        os.system('cls')
                os.system('cls')
                board = CreateBoard() #allows user to select how many rows or columns they want and builds a board.
                PlacePlayer(board, player) #places a player at a random position on board.
                treasure, GameOver, treasuresList = GenTreasure(board, treasuresList) #End of Game Building Loop
                break
            elif userInput == 50: #2 on keyboard Load Game
                os.system('cls')
                player, board, treasure, treasuresList = LoadGame()
                if player == 0:
                    continue
                board[player["row"]][player["col"]] = "@"
                os.system('cls')
                break
            elif userInput == 51: #3 on keyboard Exit Game
                os.system('cls')
                print("Thank you for playing my game!")
                print("Press ENTER to close...")
                input()
                sys.exit()
            else:
                print("Invalid selection! Press ENTER to try again!")
                input()
                os.system('cls')
            
        
        while True: #Gameplay Loop
            PlayerControl(player,board,treasure,treasuresList)
            if player['restartGame'] == True:
                break
            if CheckTreasure(treasure, player): #checks if player col and row are equal to treasure col row
                print("You got a " + str(treasure["name"]))
                player["tfound"].append(treasure["name"]) #adds found treasures to a the player dictionary list for treasures found
                treasure, GameOver, treasuresList = GenTreasure(board, treasuresList)
                checkGameOver(GameOver) #when the player has found all the items the game will end.
                print("Press ENTER to continue...")
                input()
            else:
                encounterRoll = dieRoller(1,6) #if the player doesn't find a treasure then it will randomly roll for an encounter: Minor Treasure or Combat.
                if encounterRoll == 1: #combat roll
                    enemy = GenPlayer(len(player["tfound"]))
                    player = Combat(player, enemy)
                    if player['restartGame'] == True:
                        break
                elif encounterRoll == 6: #minor treasure roll
                    minorTreasure = MinorGen()
                    randomStat = dieRoller(1,3)
                    if randomStat == 1:
                        randomMod = dieRoller(1,4)
                        player["attack"] += randomMod
                        statInc = "Attack"
                    elif randomStat == 2:
                        randomMod = dieRoller(1,4)
                        player["defense"] += randomMod
                        statInc = "Defense"
                    elif randomStat == 3:
                        randomMod = dieRoller(2,4)
                        player["health"] += randomMod
                        statInc = "Health"
                    print("You found " + str(minorTreasure["name"] + ". +" + str(randomMod) + " " + statInc))
                    print("Press ENTER to continue...")
                    input()
            os.system('cls')
            
            
main()