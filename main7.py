print("welcome to 'Whose Wallet?")
print("You will give me a list of names, and I will pick a person to pay")
names_string = input("If you're ready, enter the names separated by a comma..\n")

names = names_string.split(", ")
length_names = len(names) - 1

import random
random_name = random.randint(0, length_names)

print(f"Please ask {names[random_name]} to take his wallet out. Dinner is on him")