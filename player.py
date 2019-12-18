'''
Programmer: Cody McNealy
Last Edited: 05/07/2018
Program: player File
'''
import os
import random
import time
from myTools import *
from BoardGen import *

from BoardGen import *

#selects a random name and suffix to assign to the player
def nameGen():
    names = "Aemad Aggie Agnar Ahab Ahrim Akrisae Amaranth Barnabus Bartak Awowogei Ariannwn Dawn Edward Eoin Flo Fossegrimen Gamfred".split()
    suffixes = " of the Amlodd~ the Annihilator~ the Araxyte~ of the Arc~ of Armadyl~ ate Dirt~ of Bandos~ the Beachbum~ the Beast Slayer~ the Betrayed~ Blackbeard~ the Blazing~ the Bloodchiller~ the Boundless~ the Brave~ of the Cadarn~ the Castaway~ the Charitable~ the Completionist".split("~")

    name = names[random.randint(0,len(names)-1)] + suffixes[random.randint(0,len(suffixes)-1)]
    return name

#Chooses a town, parent job and player job to create a history for the player
def historyGen():
    towns = " Ardougne~ Keldagrim~ Draynor~ Lumbridge~ Varrock~ Gnome Stronghold~ Falador~ Canifis~ Morytania~ Port Sarim~ Rellekka".split("~")
    jobs = "Woodcutter Miner Blacksmith Crafter Farmer Fisher Cook Inventor Attacker Healer Defender Ranger Mage Herbalist Priest Thief Hunter Pyromancer".split()
    
    hometown = towns[random.randint(0,len(towns)-1)]
    jobParent = jobs.pop(random.randint(0,len(jobs)-1))
    job = jobs[random.randint(0,len(jobs)-1)]
    history = ("You were born in" + hometown + ".\n" + "Your parents were both " + jobParent + "s.\n" + "As you grew older watching your parents in their jobs, you decided you'd be better off being a " + job + ".\n")
    return history

#randomly generates Attack, Defense and health while assinging all the other values of the player to a dictionary
def GenPlayer(modifier):
    player = {}
    player["name"] = nameGen()
    player["history"] = historyGen()
    player["attack"] = dieRoller(3,6) + dieRoller(modifier,4)
    player["defense"] = dieRoller(3,6) + dieRoller(modifier,4)
    player["health"] = dieRoller(5,6) + dieRoller(modifier,4)
    player["row"] = 0
    player["col"] = 0
    player["tfound"] = []
    player["enemyDefeated"] = []
    player["restartGame"] = False
    return player
    
#MovePlayer prompts the user to input a letter to move player, open their bag or view player stats.
def PlayerControl(player,board,treasure,treasuresList):
    while True:
        board[player["row"]][player["col"]] = "@"
        ShowBoard(board)
        print("Your character is \'@\'\n")
        print("Treasures found: " + str(len(player["tfound"])) + "/11.")
        print("Use W A S D for movement around the board, B to open Bag, C to view Character Stats, H for help screen or Q or ESC to Quit.")
        userInput = ord(getch())
        
        if userInput in (98, 66): #bB on keyboard opens Bag
            os.system('cls')
            print(player["tfound"])
            print("Press ENTER to continue...")
            input()
            os.system('cls')
        elif userInput in (72,104): #hH on keyboard Opens Help Menu
            os.system('cls')
            print("To move around W for up, S for down, A for left and D for right on board. C opens Character stats, B opens Bag to view treasures, Q or ESC exits and allows you to save the game.")
            print("Press ENTER to continue...")
            input()
            os.system('cls')
            print("The goal of the game is to collect all the treasures without dying. You need to travel around the board to find the random treasure.\nAlong the way, you can find Minor Treasures that will give you a character stat boost.\nYour character stats help within combat vs your enemy. The higher your stats the easier it will be to defeat yout opponent. Good luck collecting all the treasures!")
            print("Press ENTER to continue...")
            input()
            os.system('cls')
        elif userInput in (67, 99): #cC on keyboard shows character stats
            os.system('cls')
            print(str(player["name"]))
            print("Attack: " + str(player["attack"]))
            print("Defense: " + str(player["defense"]))
            print("Health: " + str(player["health"]))
            print("\nEnemies Defeated: " + str(player["enemyDefeated"]))
            print("Press ENTER to close...")
            input()
            os.system('cls')
        elif userInput in (113, 81, 27): #qQ or ESC on keyboard quits game and allows the user to save the game
            while True:
                os.system('cls')
                print("Would you like to save game?(Y/N)")
                userInput = ord(getch())
                if userInput in (121, 89): #yY
                    SaveGame(player, board, treasure, treasuresList) #saves player, board, treasure and treasureList into a single file and allows the file to be reopened later
                    print("Saving game....\nPress ENTER to continue...")
                    input()
                    os.system('cls')
                    player["restartGame"] = True
                    return player, board
                elif userInput in (110, 78): #nN
                    os.system('cls')
                    player["restartGame"] = True
                    return player, board
                else:
                    print("Invalid selection! Press ENTER to try again!")
                    input()
                    os.system('cls')
        elif userInput in (119, 87): #wW on keyboard North
            board[player["row"]][player["col"]] = "."
            if player["row"] > 0:
                player["row"] -= 1
                break #ends loop
            else:
                print("Edge of board!")
                time.sleep(1)
                os.system('cls')
        elif userInput in (115, 83): #sS on keyboard South
            board[player["row"]][player["col"]] = "."
            if player["row"] < len(board)-1:
                player["row"] += 1
                break #ends loop
            else:
                print("Edge of board!")
                time.sleep(1)
                os.system('cls')
        elif userInput in (100,68): #dD on keyboard East
            board[player["row"]][player["col"]] = "."
            if player["col"] < len(board[0])-1:
                player["col"] += 1
                break #ends loop
            else:
                print("Edge of board!")
                time.sleep(1)
                os.system('cls')
        elif userInput in (97, 65): #aA on keyboard West
            board[player["row"]][player["col"]] = "."
            if player["col"] > 0:
                player["col"] -= 1
                break #ends loop
            else:
                print("Edge of board!")
                time.sleep(1)
                os.system('cls')
        else: #Input validation only allowing the player to enter the set keys for controls.
            print("Invalid selection! Press ENTER to try again!")
            input()
            os.system('cls')
            board[player["row"]][player["col"]] = "@"
    board[player["row"]][player["col"]] = "@"
    return player, board