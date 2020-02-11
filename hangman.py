#Options : menu - difficulty
#_ = system('cls') to clear
import os
from time import sleep



from wordlist


def getwordlist():
    print(wordlist)
    

def playgame():
    getwordlist()

    

def loadingdots():
    os.system('cls')
    sleep(1)
    print(".")
    sleep(1)
    os.system('cls')
    print("..")
    sleep(1)
    os.system('cls')
    print("...")
    sleep(1)
    os.system('cls')


    
def mainmenu():
    print('''Welcome to hangman v.0.1.1! \nPlease type one of the following menu options:

    > NEW GAME
    > OPTIONS
    > QUIT
          
          ''')
    choice = input("> ")
    while True:
        if str(choice) == "NEW GAME":
            return "NEW GAME"
            break
        if str(choice) == "OPTIONS":
            return "OPTIONS"
            break
        if str(choice) == "QUIT":
            return "QUIT"
            break
        else:
            print("Not valid choice...")
            continue

while True:
    playerdesire = mainmenu()

    print(playerdesire)
    
    if str(playerdesire) == "NEW GAME":
        print("\nStarting new game...\n")
        playgame()
    if str(playerdesire) == "OPTIONS":
        os.system('cls')
        print("\nComing Soon...\n")
        sleep(1)
        print("Very soon..")
        sleep(1)
        print("like today lol")
        input("...")
        os.system('cls')
    if str(playerdesire) == "QUIT":
        print("\nGood Bye!")
        loadingdots()
        break
        
