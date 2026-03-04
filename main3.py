print("Welcome to the test of whether you live in Tanta or not.")
transportation = input("First, You are now at the train station Will you take a taxi, microbus, or Uber? \n")

if transportation.lower() == "microbus":
    print("Unfortunately, it is difficult to ride a microbus!")
elif transportation.lower() == "uber":
    print("Unfortunately, there is no Uber available in Tanta")
elif transportation.lower() == "taxi":
    print("Excellent choice!")
   
    taxi_color = input("Now you have 3 taxis, red, white and green , choose one:\n")
    
    if taxi_color.lower() == "green" or taxi_color.lower() == "red":
        print("Sorry, this color is not available in Tanta taxis, choice another color.")
    elif taxi_color.lower() == "white":
        payment_method = input("Ok, Will you pay in cash or Visa?\n")
        if payment_method.lower() == "visa":
            print("hey, Where are you from? Aren't you from Tanta?!")
            print("There is no taxi with a visa in Tanta.")
        elif payment_method.lower() == "cash":
            print("ok , Let's go")
        else:
            print("Invalid choice")
    else:
        print("that is not in choices, Follow the instructions!")
else:
    print("This is not in the choices!, please try again.")