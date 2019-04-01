# Guessing Game
import random


def guessing_game():
    randomNumber = random.randint(1, 100)
    guessedCorrectly = False
    lastGuess = -1
    numberOfGuesses = 0
    while not guessedCorrectly:
        guess = int(input("Guess a number between 1 and 100: "))
        if lastGuess != guess:
            numberOfGuesses += 1
            lastGuess = guess
        if randomNumber == guess:
            print("You got it!  You guessed the secret number in %d guesses." % numberOfGuesses)
            guessedCorrectly = True
        elif randomNumber < guess:
            print("Too high!")
        else:
            print("Too low!")


guessing_game()
