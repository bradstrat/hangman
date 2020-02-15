import random

def getdifficulty():
    while True:
        getworddifficulty = input("Please choose difficulty: \n\nEASY (7 letters or more)\nMEDIUM (5 - 6 letters)\nHARD (4 letters or less)\n > ")

        if getworddifficulty.upper() == "EASY":
            return "easy"
            break
        
        if getworddifficulty.upper() == "MEDIUM":
            return "medium"
            break
        
        if getworddifficulty.upper() == "HARD":
            return "hard"
            break
        
        else:
            print("Please choose one of the choices provided. \n")
            continue
        

    
def wordgiver():
    while True:
        #EASY (7 letters or more) -- MEDIUM (5 - 6 letters) -- HARD (4 letters or less)
        worddict = {'easy': ["hamster", "dolphin", "elephant", "ostrich", "alligator", "penguin", "giraffe", "peacock", "lobster", "squirrel"], 'medium': ["hammy", "zebra", "tiger", "rabbit", "goose", "turtle", "donkey", "horse", "lizard", "sheep"], 'hard': ["pig", "cat", "worm", "bird", "dog", "bat", "cow", "duck", "owl", "fox", "fish", "goat", "lion"]}

        difficulty = getdifficulty()
        randindex = random.randint(0, (len(worddict[difficulty])-1))

        return worddict[difficulty][randindex]



#test only
#wordgiver()
