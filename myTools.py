'''
Programmer: Cody McNealy
Last Edited: 05/07/2018
Program: different Tools for game functions File
'''
import random
import os
import sys
import pickle
import time
from TreasureGen import *
from msvcrt import getch

def dieRoller(times, sides): #imitates a dice and allows user to input number of sides and how many times you roll it
    total = 0
    for i in range(times):
        total += random.randint(1,sides)
    return total
        
def checkGameOver(GameOver): #uses the GameOver to determine if the player has won the game or not
    if GameOver == 1:
        print("\nCongratulations! You have found all the treasures!")
        print("And you defeated: " + str(len(player["enemyDefeated"])) + " enemies on the way!")
        while True:
            print("Would you like to view a list of enemies killed?(Y/N)")
            userInput = ord(getch())
            if userInput in (121,89):
                print(player["enemyDefeated"])
                break
            elif userInput in (110, 78):
                break
            else:
                print("Invalid selection! Press ENTER to try again!")
                input()
        time.sleep(1)
        os.system('cls')
        print("Thank you for playing my game!")
        print("Press ENTER to close...")
        input()
        sys.exit()
    else:
        return
        
def SaveGame(player, board, treasure, treasuresList): #allows the user to save a game in the saves folder
    directory = "saves/"
    extention = ".sav"
    saveFile = input("What would you like to name your save?: ")
    gameFile = {"player":player, "board":board, "treasure":treasure, "treasuresList":treasuresList}
    pickle.dump(gameFile, open(directory + saveFile + extention, "wb"))

def LoadGame(): #prints out the users save files in a list and allows the user to type in the number of the save file they want to play.
    loadGameList = []
    for file in os.listdir("saves/"):
        loadGameList.append(file)
    while True:
        for i in range(len(loadGameList)):
            print(i + 1, loadGameList[i])
        directory = "saves/"
        userInput = int(input("Enter the number of the file you would like to open or type a -1 to return to menu: "))
        if  userInput <= len(loadGameList) and userInput >= 0:
            gameFile = pickle.load(open(directory + loadGameList[userInput - 1], "rb"))
            player = gameFile["player"]
            board = gameFile["board"]
            treasure = gameFile["treasure"]
            treasuresList = gameFile["treasuresList"]
            break
        elif str(userInput) == "-1":
            os.system('cls')
            player = 0
            board = 0
            treasure = 0
            treasuresList = 0
            break
        else:
            print("Invalid selection! Press ENTER to try again!")
            input()
            os.system('cls')
    return player, board, treasure, treasuresList
    
def Combat(player, enemy): #combat encounters allow user to attack enemy with 4 different attacks: normal, power, quick or counter
    os.system('cls')
    print(enemy["name"] + " appears!")
    print("Press ENTER to continue...")
    input()
    os.system('cls')
    while player["health"] > 0 and enemy["health"] > 0:
        print("{:<30}".format("Player: " + str(player["name"])),end = "")
        print("{:>40}".format(str("Enemy: " + enemy["name"])))
        
        print("{:<30}".format("Health: " + str(player["health"])),end = "")
        print("{:>40}".format("Health: " + str(enemy["health"])))
        
        print("{:<30}".format("Attack: " + str(player["attack"])),end = "")
        print("{:>40}".format("Attack: " + str(enemy["attack"])))
        
        print("{:<30}".format("Defense: " + str(player["defense"])),end = "")
        print("{:>40}".format("Defense: " + str(enemy["defense"])))
        
        playerAttRoll = dieRoller(1,20)
        enemyAttRoll = dieRoller(1,20)
        playerAttBonus = player["attack"]//5
        enemyAttBonus = enemy["attack"]//5
        playerDefBonus = player["defense"]//5
        enemyDefBonus = enemy["defense"]//5
        while True:
            print("\n1) Power attack!\n2) Quick attack!\n3) Counter attack!\n4) Normal attack!")
            userInput = ord(getch())
            if userInput not in (49, 50, 51, 52):
                print("Invalid selection! Press ENTER to try again!")
                input()
                os.system('cls')
                print("{:<30}".format("Player: " + str(player["name"])),end = "")
                print("{:>40}".format(str("Enemy: " + enemy["name"])))
        
                print("{:<30}".format("Health: " + str(player["health"])),end = "")
                print("{:>40}".format("Health: " + str(enemy["health"])))
                
                print("{:<30}".format("Attack: " + str(player["attack"])),end = "")
                print("{:>40}".format("Attack: " + str(enemy["attack"])))
                
                print("{:<30}".format("Defense: " + str(player["defense"])),end = "")
                print("{:>40}".format("Defense: " + str(enemy["defense"])))
            elif userInput == 49: #1 on keyboard Power Attack
                playerAttBonus = playerAttBonus * 2
                enemyAttBonus = enemyAttBonus * 1.5
                break
            elif userInput == 50:#2 on keyboard Quick Attack
                playerAttBonus = playerAttBonus * 2
                enemyDefBonus = enemyDefBonus * 1.5
                break
            elif userInput == 51:#3 on keyboard Counter Attack
                playerDefBonus = playerDefBonus * 2.5
                playerAttBonus = 0
                break
            elif userInput == 52:#4 on keyboard Normal Attack
                break
        pCritChance = dieRoller(1,25)
        eCritChance = dieRoller(1,25)
        pCrit = False
        eCrit = False
        if pCritChance == 1:
            pCrit = True
            critHit = dieRoller(1,5)
            playerDmg = int(playerAttRoll + playerAttBonus - enemyDefBonus + critHit)
        else:
            playerDmg = int(playerAttRoll + playerAttBonus - enemyDefBonus - 10)
        if eCritChance == 1:
            eCrit = True
            critHit = dieRoller(1,5)
            enemyDmg = int(enemyAttRoll + enemyAttBonus - playerDefBonus + critHit)
        else:
            enemyDmg = int(enemyAttRoll + enemyAttBonus - playerDefBonus - 10)
        if playerDmg <= 0:
            print("You missed!")
        else:
            if pCrit == False:
                enemy["health"] -= playerDmg
                print("You hit " + str(playerDmg) + "!")
            elif pCrit == True:
                enemy["health"] -= playerDmg
                print("You critically hit " + str(playerDmg) + "!")
        if enemy["health"] <= 0:
            print("You defeated " + enemy["name"] + "!")
            print("Press ENTER to continue..")
            input()
            player["enemyDefeated"].append(enemy["name"])
            os.system('cls')
            return player
        if enemyDmg <=0:
            print("The enemy missed!")
        else:
            if eCrit == False:
                player["health"] -= enemyDmg
                print("Enemy hit " + str(enemyDmg) + "!")
            elif eCrit == True:
                enemy["health"] -= playerDmg
                print("You were critically hit " + str(enemyDmg) + "!")
        if player["health"] <= 0:
            os.system('cls')
            print("You died! Game over!\n" + "You still defeated: " + str(len(player["enemyDefeated"])) + " enemies in your way!")
            while True:
                print("Would you like to view a list of enemies killed?(Y/N)")
                userInput = ord(getch())
                if userInput in (121, 89): #yY on keyboard Yes
                    print(player["enemyDefeated"])
                    break
                elif userInput in (110, 78): #nN on keyboard No
                    break
                else:
                    print("Invalid selection! Press ENTER to try again!")
                    input()
                    os.system('cls')
            time.sleep(1)
            print("Press ENTER to return to the main menu!")
            input()
            os.system('cls')
            player["restartGame"] = True
            return player    
        print("Press ENTER to continue...")
        input()
        os.system('cls')