# The program should have the right answer set to 8,
# then prompt the user repeatedly to guess the number from 1 to 20.
# When the user guesses incorrectly, the game should give the user
# a hint about whether the correct answer is higher or lower than the guess.
# Once the user guesses correctly,
# the program should print a message showing the number of guesses that the user made.
import random

randomNumber: int = random.randrange(1, 20)
print("I’m thinking of a number in the range 0-50. You have five tries to guess it.")
guessed = False

while not guessed:
    userInput = int(input("Guess 1?"))
    if userInput == randomNumber:
        guessed = True
        print("You are right! I was thinking of" + randomNumber + "!")
    elif userInput > randomNumber:
        print(randomNumber + "is too high.")
    elif userInput < randomNumber:
        print(randomNumber + "is too low.")
    elif userInput > 5:
        print("Your guess is incorrect. The right answer is" + randomNumber)

print("End of program")
