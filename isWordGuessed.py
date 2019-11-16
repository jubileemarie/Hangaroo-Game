def isWordGuessed(secretWord,lettersGuessed):
    ctr=0
    for A in secretWord:
        for B in lettersGuessed:
            if B==A:
                ctr = ctr + 1
                break
            elif B!=A:
                pass
    return(ctr==len(secretWord))