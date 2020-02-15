#Options : menu - difficulty
#_ = system('cls') to clear

import os
from time import sleep
import wordlist


def playgame():
    #provide commetns on whats happening

    word = wordlist.wordgiver()

    lines = []
    for i in word:
        lines.append('_')

    counter = 0

    while True:

        letter = input('\nGuess your letter or type GUESS to make a guess: ')
        #give the chance to guess the whole word
        if letter.lower() == "guess":
            g = input("Guess the word: ")
            if str(g.lower()) == word:
                print("The word was...")
                sleep(2)
                print(word + "!")
                break
            else:
                print("NOPE!")
                if counter == 6:
                    break
                
        #check if the guessed letter is in the word and set _ to letter
        if letter in word:
            for i in range(0, len(word)):
                if word[i] == letter:
                    lines[i] = letter
        #letter is not in the word
        else:
            counter += 1
        #print the word with inserted letters
        for i in lines:
            print(i, end=" ")

        #check letters remained in the list

        cnt = "".join(lines).count('_')
        print("     guesses remaining: {}".format(6-(int(counter))))
        if cnt == 0 or counter == 6:
            break
    #end of while loop

    if counter >= 6:
        print("\n\nThe word was {}!".format(word))
        print("\n\n\n You lose.............. Better luck next time!\n")
        input("Press any key to continue...")
    else:
        print("\n\nYes! You WON this match!\n")
        input("Press any key to continue...")


def loadingdots():
    os.system('cls')
    sleep(1)
    print(".")
    sleep(0.5)
    os.system('cls')
    print("..")
    sleep(0.5)
    os.system('cls')
    print("...")
    sleep(0.5)
    os.system('cls')


    
def mainmenu():
    print('''Welcome to hangman v.0.1.1! \nPlease type one of the following menu options:

    > NEW GAME
    > OPTIONS
    > QUIT
          
          ''')
    
    while True:
        choice = input("> ")

        if str(choice.lower()) == "a":
            print("test dont")
            
        if str(choice.lower()) == "new game":
            return "NEW GAME"
            break
        
        if str(choice.lower()) == "options":
            return "OPTIONS"
            break
        
        if str(choice.lower()) == "quit":
            return "QUIT"
            break

        else:
            print("Not valid choice...")
            continue


while True:
    playerdesire = mainmenu()
    
    if str(playerdesire.lower()) == "new game":
        print("\nStarting new game...\n")
        playgame()
        
    if str(playerdesire.lower()) == "options":
        os.system('cls')
        print("\nComing Soon...\n")
        sleep(1)
        print("Very soon...\n")
        sleep(1)
        print(";)")
        sleep(1)
        os.system('cls')
        
    if str(playerdesire.lower()) == "quit":
        print("\nGood Bye!")
        loadingdots()
        break
    else:
        continue
    
        
