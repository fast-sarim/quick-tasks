
import random
number = random.randint(1, 100)
guess = None
tries = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct! You guessed number in", tries, "tries")
