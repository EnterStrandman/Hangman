"""
Matt Strand
Hangman
Started: 3/19/2019
Last Edited 3/19/2019

Ideas:
    keep score
    Create GUI
"""

import os
import random

def playGame(chars):
    currentState = []
    guessedLetters = []
    turns = 11
    play = True
    setup = 0

    while setup < len(chars):
        if chars[setup] == " ":
            currentState.append(" ")
        else:
            currentState.append("_")
        setup = setup + 1
    
    while play:
        print(' '.join(currentState))
        if turns > 0 and "_" in currentState:
            guess = input("Type a letter:").lower()
            if len(guess) == 1:
                if guess in guessedLetters:
                    print("You already guessed that. Try again.")
                else:
                    if guess in chars:
                        i = 0
                        while i < len(currentState):
                            if chars[i] == guess:
                                currentState[i] = guess
                            i = i + 1
                        print("Okay, you got lucky.")
                    else:
                        print("Nope, not in the word/phrase")
                        print("You have", turns, "turns left")
                        turns = turns - 1
                        guessedLetters.append(guess)
            else:
                print("You can only guess one letter at a time. Try Again")
        else:
            print("GAME OVER")
            k=0
            result = True
            while k < len(currentState) and result:
                if currentState[k] == "_":
                    print("You Lose.")
                    print("The word/phrase was.... ")
                    print(''.join(chars))
                    print()
                    result = False
                k = k + 1
            if result == True:
                print("YOU WIN!")
                print()
            play = False

def getCategories():
    categories = []
    for dirName, subdirList, fileList in os.walk('Categories List'):
        for fname in fileList:
            categories.append(os.path.splitext(fname)[0])
    return categories

        
"""

MAIN IS BELOW

"""
play = True

while play:
    #mode 1 is PVP, 2 is CPU
    mode = input("Select your opponent(0-Quit/1-PVP/2-CPU):")

    if mode == "0":
        print("Exited Game")
        play = False
    elif mode == "1":
        word = input("Type the word to be played on:").lower()
        chars = list(word)
        playGame(chars)
    elif mode == "2":
        categoryList = getCategories()
        numCat = 1
        while numCat <= len(categoryList): 
            print(str(numCat),''.join(categoryList[numCat-1]))
            numCat = numCat + 1
        category = input("Choose a category:")

        if os.path.exists("Categories List/"+category+".txt"):
            file = open("Categories List/"+category+".txt")
            choiceFile = file.read().split(',')
            randomSelect = random.randint(0,len(choiceFile)-1)
            chars = list(choiceFile[randomSelect])
            playGame(chars)
        else:
            print("Please type the file name exactly as in appears in the list.")
    else:
        print("Invalid Input")
    

