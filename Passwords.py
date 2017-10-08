import random

def generatePassword(passwordLength):
    password = ""
    for i in range(passwordLength):
        if(random.randrange(0,2) == 1):
            password += randomCase()
        else:
            password += randomSpecialCharacters()
            
    return password

def randomSpecialCharacters():
    special = "@![]$#%^&*()\",.></?:;'=+-_\\|0123456789"
    return special[random.randrange(0,(len(special)-1))]

def randomCase():
    if(random.randrange(0,2) == 1):
        return randomLetter().capitalize()
    else:
        return randomLetter()

def randomLetter():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[random.randrange(0,25)]


print(generatePassword(7))
