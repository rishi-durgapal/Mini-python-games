import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        if int(guess) < number:
            print("Too low! Try again.")
        elif int(guess) > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input! Please enter a number.")
