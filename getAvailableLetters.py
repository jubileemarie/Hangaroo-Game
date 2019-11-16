def getAvailableLetters(lettersGuessed):
    import string
    lowercase = string.ascii_lowercase
    for B in lettersGuessed:
        for L in lowercase:
            if L == B:  
                lowercase = lowercase.replace(L,'')