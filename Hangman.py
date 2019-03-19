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


word = input("Type the word to be played on:").lower()
chars = list(word)
play = True
turns = 11
guessedLetters = []
currentState = []
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


