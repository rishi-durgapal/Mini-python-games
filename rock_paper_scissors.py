import random

emojis = {
    "rock": "🪨",
    "paper": "📃",
    "scissors": "✂️"
}
choices = ("rock", "paper", "scissors")

def get_user_choice():
    while True:
        user_choice = input ("Rock, Paper, Scissors! Choose your move (rock, paper, scissors): ").lower()
        if user_choice in choices:
           return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def display_choices(user_choice, computer_choice):  
       print(f"You chose: {emojis[user_choice]}")
       print(f"Computer chose: {emojis[computer_choice]}") 

def determine_winner(user_choice, computer_choice): 
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
        (user_choice == "rock" and computer_choice == "scissors") or 
        (user_choice == "paper" and computer_choice == "rock") or 
        (user_choice == "scissors" and computer_choice == "paper")):
            print("You win!")
        else:
            print("You lose!")  

def play_game():  
    while True:
    
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        
        display_choices(user_choice, computer_choice )

        determine_winner(user_choice, computer_choice)  

        should_continue = input("Continue ? Yes/No: ").strip().lower()
        if should_continue == "no":
            print("Thanks for playing!")
            break

play_game()