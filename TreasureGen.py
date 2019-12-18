'''
Programmer: Cody McNealy
Last Edited: 05/07/2018
Program: Treasure Generator Functions File
'''
import random
import sys

minorTreasures = "a Ring of Health~a Amulet of Attack~some Boots~some Gloves~a Cape of Origins~a Shortsword~a Longsword~a Broadsword~a Off-hand Shortsword~a Shieldbow~a Crossbow~a Two-Handed Crossbow~a Wand~a Spellbook~a Staff~a Shield~a Defender~a Spear".split("~") #assigning the Minor Treasures in a list

#Randomly generates a Treasure on the game board and removes it from treasure list.
def GenTreasure(board, treasuresList):
    if len(treasuresList) >= 1:
        treasureName = treasuresList.pop(random.randint(0,len(treasuresList)-1))
        treasure = {}
        row = random.randint(0,len(board)-1)
        col = random.randint(0,len(board[0])-1)
        treasure["name"] = treasureName
        treasure["row"] = row
        treasure["col"] = col
        GameOver = 0
    elif len(treasuresList) == 0: #if the list is empty it will return GameOver to 1 which will end the game.
        treasure = {}
        row = random.randint(0,len(board)-1)
        col = random.randint(0,len(board[0])-1)
        treasure["row"] = row
        treasure["col"] = col
        GameOver = 1
    return treasure, GameOver, treasuresList

#checks if the player row and col are the same as treasure row and col
def CheckTreasure(treasure, player):
    if player["col"] == treasure["col"] and player["row"] == treasure["row"]:
        return True
    return False

#Generates a minor Treasure from the minorTreasure list.
def MinorGen():
    minorTreasureName = minorTreasures[random.randint(0,len(minorTreasures)-1)]

    minorTreasure = {}
    minorTreasure["name"] = minorTreasureName
    return minorTreasure