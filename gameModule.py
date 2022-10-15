# MasterMind gives the complete abstraction of functionality of a guess game.
# The game generates a secret code(digits based upon the NUMBER_OF_DIGITS constant).
# The user then has to guess the number in the given number of chances(MAXIMUM_NUMBER_OF_GUESSES).

from random import randrange
import constants

class MasterMind:
    # class constructor
    # initalizes the private game parameters
    def __init__(self) -> None:
        self.__username : str = ""
        self.__secretCode : str = ""
        self.__userGuessCountPerGame : int = 0
        self.__overallGuessCount : int = 0
        self.__gameCount : int = 0
        
    # sets up a new game
    # sets parameters to it's initial value
    # increaments the game count
    def setUpNewGame(self) -> None:
        self.__secretCode = ""
        self.__userGuessCountPerGame = 1
        self.__gameCount += 1
        
    # ends a game round
    # computes the total user guesses
    def endRound(self, userGuessedTheCode: bool) -> None:
        if userGuessedTheCode:
            self.__overallGuessCount += self.__userGuessCountPerGame
        else:
            self.__overallGuessCount += 10
    
    # prints out the game details and takes name of the user
    def startGame(self) -> None:
        print("\n\n\t\t\t~~~~~~WELCOME TO MASTERMIND~~~~~~")
        print("\nHi gamer, welcome to the Mastermind game")
        self.__username = input("What is your name? ")
        print(f"Hello, {self.__username}, Please follow the given instructions to play the game")\
            
    # prints out instructions to play the game
    def displayInstructions(self) -> None:
        print("\n\n\t\t\t~~~GAME INSTRUCTION~~~")
        print("\nI am thinking of a 3-digit number. Try to guess what it is.")
        print("Here are some clues:")
        print("When I say:\tThat means:")
        print("Yellow\t\tOne digit is correct but in the wrong position.")
        print("Green\t\tOne digit is correct and in the right position.")
        print("Red\t\tNo digit is correct.")
        
    
    # getter function for __secretCode
    @property
    def secretCode(self) -> str:
        return self.__secretCode
    
    # setter function for __secretCode
    @secretCode.setter
    def secretCode(self, value: str) -> None:
        self.__secretCode = value
        
    # getter function for __userGuessCountPerGame
    @property
    def userGuessCountPerGame(self) -> int:
        return self.__userGuessCountPerGame
    
    # setter function for __userGuessCountPerGame
    @userGuessCountPerGame.setter
    def userGuessCountPerGame(self, value: int) -> None:
        self.__userGuessCountPerGame = value
    
    # generates a secret 3 digit code with unique digits
    # sets this generated value to __secretCode
    def generateSecretCode(self) -> None:
        secretCode = ""
        while len(secretCode) != constants.NUMBER_OF_DIGITS:
            randomNo = str(randrange(10))
            if (randomNo not in secretCode):
                secretCode += randomNo
        self.__secretCode = secretCode
        print("\nI have thought up a number")
        print(f"You have {constants.MAXIMUM_NUMBER_OF_GUESSES} chances to guess it\n")
        
    
    # generates falgs of different colour based on user input
    # green if user guesses a digit in correct position
    # yellow if user guesses a digit but in wrong position
    # red if user guesses no digits correct
    def getFlagColour(self, userGuess) -> str:
        flags = []
        for index in range(constants.NUMBER_OF_DIGITS):
            if userGuess[index] ==  self.__secretCode[index]:
                flags.append("Green")
            elif userGuess[index] in self.__secretCode:
                flags.append("Yellow")
            else:
                pass
        
        if not flags:
            flags.append("Red")
        
        self.__userGuessCountPerGame += 1
        
        return " ".join(flags)
    
    # prints out the results of the current round
    # called after the current round is completed
    def displayGameResult(self, userGuessedTheCode: bool) -> None:
        if userGuessedTheCode:
            print(f"\nCongrats, You guessed the answer in {self.__userGuessCountPerGame} guesses")
        else:
            print(f"\nGame Over. You were not able to guess the code in {constants.MAXIMUM_NUMBER_OF_GUESSES} guesses")
            print(f"The correct answer was {self.__secretCode}")
    
    # prints out the overall result of the user
    # called after user has decided to quit the game
    def displayOverallResult(self) -> None:
        avgGuesses = self.__overallGuessCount / self.__gameCount
        print(f"\nThank You {self.__username} for playing Master Mind")
        print(f"Your Overall Results: ")
        print(f"Total Games: {self.__gameCount}")
        print(f"Total guesses: {self.__overallGuessCount}")
        print(f"Average guesses per game: {avgGuesses}") 


                
        
    
         