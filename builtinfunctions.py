print("Hello and welcome to my guessing numbers game!")
import random
numberToGuess = random.randint(1, 100)

print(numberToGuess)
numberOfTries = 0

for i in range(10):
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    numberOfTries = numberOfTries + 1

    if guess < numberToGuess:
        print("Your guess is too low.")
    if guess > numberToGuess:
        print("Your guess is too high.")
    if guess == numberToGuess:
        break