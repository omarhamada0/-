print("Welcome to the Rock, Paper, Scissors game:")
confirm = input("Press Enter to continue or type (Help) for the rules help\n").lower()

if confirm == "help":
    print("""
                   ********* RULES *********
                   1) You choose and the computer chooses
                   2) Rock smashes Scissors -> Rock wins
                   3) Scissors cut Paper -> Scissors win
                   4) Paper covers Rock -> Paper wins
          """)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

choices = ["rock" , "paper" , "scissors"]
import random
computer_choice = random.choice(choices)

if (user_choice == "rock" and computer_choice == "scissors") or (user_choice.lower() == "paper" and computer_choice == "rock") or (user_choice.lower() == "scissors" and computer_choice == "paper"):
    print(f"you chose: {user_choice}")
    print(f"computer chose: {computer_choice}")
    print(f"you win! {user_choice} beat {computer_choice}.")

elif (user_choice.lower() == "rock" and computer_choice == "paper") or (user_choice.lower() == "paper" and computer_choice == "scissors") or (user_choice.lower() == "scissors" and computer_choice == "rock"):
    print(f"you chose: {user_choice}")
    print(f"computer chose: {computer_choice}")
    print(f"you win! {user_choice} beat {computer_choice}.")

else:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")