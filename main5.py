color = [input("Add the first color you like:\n")]
more_color = input("Do you want to add more colors? Yes, or No?\n")
if more_color.lower() == "no":
    print(f"the color you like is: {color}")
elif more_color.lower() == "yes":
    anoter_color = input("Add another color to the list:\n")
    color.append(anoter_color)
    print(f"the colors you like are: {color}")
else:
    print("Invalid choice. Please choose either (yes or no)")