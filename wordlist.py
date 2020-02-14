import random



def wordgiver():
    randindex = random.randint(0, 9) 
    wordlist = ["worm", "hammy", "dog", "cat", "zebra", "elephant", "bird", "dolphin", "hamster", "tiger"]
    return wordlist[randindex]


#test only
#print(wordgiver())
