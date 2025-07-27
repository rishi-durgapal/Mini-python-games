import random

easy_words = ["cat", "dog", "fish", "bird", "tree"]
medium_words = ["apple", "banana", "orange", "grape", "peach"]
hard_words = ["elephant", "giraffe", "crocodile", "hippopotamus", "rhinoceros"]

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")
difficulty = input("Enter your choice: ").lower()
if difficulty == 'easy':
    secret_word = random.choice(easy_words)
elif difficulty == 'medium':
    secret_word = random.choice(medium_words)
elif difficulty == 'hard':  
    secret_word = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to Easy level.")
    secret_word = random.choice(easy_words)
attempts = 0
print("Guess the secret word!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == secret_word:
        print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
        break
    hint = ""
    for i in range(len(secret_word)):
        if i < len(guess) and guess[i] == secret_word[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")

print("Thanks for playing the Password Guessing Game!")
