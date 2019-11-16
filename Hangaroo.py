def Hangaroo(secretWord):
    import string
    mistakesMade = 0
    lettersGuessed=[]
    list(lettersGuessed)
    
    print("Welcome to HANGAROO!")
    print("")
    print("Guess the letters and win the game!")
    print("We'll be counting your number of incorrect guess!")
    print("Lets start!")
    print("Number of Incorrect Guess: ", mistakesMade)
    print("")
    print(getGuessedWord(secretWord,lettersGuessed))
    
    
    while isWordGuessed(secretWord,lettersGuessed) == False:
        G = input("Guess a letter: ")
        guessedLetter = G.lower()
        
        if len(guessedLetter)!=1 or (guessedLetter in string.ascii_lowercase) == False:
            print("Oops invalid guess! Try Again")
            print("")
        elif (guessedLetter in secretWord) == False and (guessedLetter in lettersGuessed) == False:
           mistakesMade += 1
           print("Oh no! Wrong guess. Try again")
           print("Number of Incorrect Guess: ",mistakesMade)
           print("")
           lettersGuessed.append(guessedLetter)
           
        elif (guessedLetter in lettersGuessed) == True:
            print("Oh no! You've already guessed that letter. Try again")
        else:
            print("Nice one! You got that right! Continue guessing")
            print("")
            lettersGuessed.append(guessedLetter)
            
        print(getGuessedWord(secretWord,lettersGuessed))
        print("Available Letters: ", getAvailableLetters(lettersGuessed))
            
    if isWordGuessed(secretWord,lettersGuessed) == True: 
        print("")
        return(print("Congratulations! You correctly guessed the word : ",secretWord))
    