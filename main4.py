import random

print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

choice = input("Enter your choice (1 or 2):\n")

if choice == "1":
    random_number = random.random()

    if random_number >= 0.5:
        computer_result = "heads"
    else:
        computer_result = "tails"

    user_choice = input("Enter your guess (Heads or Tails):\n")

    if user_choice.lower() == computer_result:
        print("Congratulations! you won.")
        print(f"The computer's coin toss result was: {computer_result}")
    else:
        print("Sorry! you lost.")
        print(f"The computer's coin toss result was: {computer_result}")

elif choice == "2":
    randint_number = random.randint(0,1)

    if randint_number == 0:
        computer_result = "heads"
    else:
        computer_result = "tails"

    user_choice = input("Enter your guess (Heads or Tails):\n")

    if user_choice.lower() == computer_result:
        print("Congratulations! you won.")
        print(f"The computer's coin toss result was: {computer_result}")
    else:
        print("Sorry! you lost.")
        print(f"The computer's coin toss result was: {computer_result}")

else:
    print("Invalid choice. Please select either (1 or 2)")