# welcome message

print ("( ͡❛ ͜ʖ ͡❛)")
# doors choice

doors_color = input ("""
welcome to my island!
there are two doors in front of you. 🚪 a red door and 🚪 a blue door
which door do you want to open?
""")

if doors_color.lower() == "blue":
    print("oops! you chose the crocodile door.")
    print("Game over! 🐊🐊🐊")

elif doors_color.lower() == "red":
    print("Great! now you entered a room.")
    print("You found three boxes: 🎁 white, 🎁 black, 🎁 green")
    # boxes choice

    box_color = input("Which box do you open?")
    
    if box_color.lower() == "white":
        print("oops! You opened a box filled with snakes 🐍🐍🐍")
    
    elif box_color.lower() == "black":
        print("oops! you opened a box filled with spiders 🕷️🕷️🕷️")
    
    elif box_color.lower() == "green":
        print("Congratulations! You found the tressure! 💲💲💸💸")
    
    else :
        print("Invalid choice! 🤷‍♂️♂️🤷‍♂️♂️🤷‍♂️♂️")
else :
    print("Invalid choice! 🤷‍♂️♂️🤷‍♂️♂️🤷‍♂️♂️")