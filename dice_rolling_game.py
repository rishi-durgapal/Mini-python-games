import random

while True:
    choice = input("Roll the dice? (yes/no): ").strip().lower()
    if choice == 'yes' :
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}.")
    elif choice == 'no':
        print("Maybe next time!")
        break
    else:
        print("Invalid input, please type 'yes' or 'no'.")
        