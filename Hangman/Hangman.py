"""
Matt Strand
Hangman
Started: 3/19/2019
Last Edited 3/19/2019

Ideas:
    PVP and CPU mode
    Allow for multiple plays and keep score
    Add a text file of words and allow the user to play against a CPU with different categories
    Create GUI
"""

import os

def playGame(chars):
    currentState = []
    guessedLetters = []
    turns = 11
    play = True
    setup = 0

    while setup < len(word):
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
            while k < len(currentState):
                if currentState[k] == "_":
                    print("You Lose.")
                    print("The word/phrase was.... " + word)
                    result = False
                k = k + 1
            if result == True:
                print("YOU WIN!")
            play = False

def printCategories():
    categories = [x[0] for x in os.walk("Categories List")]
    count = 1
    while count <= len(categories):
        print(count,':'.join(categories))
        count = count + 1




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
        printCategories()
        category = input("Choose a category:")
    else:
        print("Invalid Input")
    

