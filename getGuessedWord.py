def getGuessedWord (secretWord,lettersGuessed):
    for A in secretWord:
        if A == '_' or A == ' ':
            continue
        elif (A in lettersGuessed) == False:
            secretWord = secretWord.replace(A,'_ ')
    return(secretWord)