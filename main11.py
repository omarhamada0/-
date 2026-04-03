print("***** Welcome to iShop calculator *****\n")
num_items = int(input("How many items are there in your basket today? "))
basket = []
total = []
for i in range(1, num_items + 1):
    item = input(f"\nPlease tell me the name of the item number {i}: ")
    price = int(input(f"What is the price of {item}?\n$"))
    basket.append(item)
    total.append(price)
basket_list = input("Would you like to see your entire basket items?\n ").lower()
if basket_list == "yes":
    print(basket)
cost = input("Would you like to see how much it'll cost? ").lower()
if cost == "yes":
    print("\nBuying these items will cost:")
    print(sum(total))