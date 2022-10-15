from gameModule import MasterMind

if __name__ == "__main__":
    masterMind = MasterMind()
    masterMind.startGame()
    masterMind.displayInstructions()
    playGame = "y"
    
    while playGame.lower() == "y":
        userGuess = None
        masterMind.setUpNewGame()
        masterMind.generateSecretCode()
        secretCode = masterMind.secretCode
        userWon = False
        
        while masterMind.userGuessCountPerGame <= 10:
            userGuess = input("Enter your guess: ")
            if len(userGuess) != 3:
                print("Please enter a 3 digit number\n")
                continue
            if userGuess == secretCode:
                userWon = True
                break
            
            flags = masterMind.getFlagColour(userGuess)
            print(flags)
        
        masterMind.endRound(userWon)
        masterMind.displayGameResult(userWon)
        
        playGame = input("\nDo you want to play again? (yes/no) ")[0]            
        
    masterMind.displayOverallResult()
        
        
        
        
            
            
        
        
