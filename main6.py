book = [input("Enter the name of a book you own:\n")]
another_book = input("Enter the name of another book you own (or press 'Enter' to  skip)\n")
if another_book:
    book.append(another_book)
    print(f"Your library: {book}")
    wish_book = [input("Enter the name of a book you wish to have in the future:\n")]
    another_wish_book = input("Enter the name of anoter book you wish to have (or press 'Enter' to  skip)\n")
    if another_wish_book:
        wish_book.append(another_wish_book)
        print(f"Your Wishlist: {wish_book}")
        get_wish_book = input("Enter the name of a book from your wishlist that you've already got it (or press 'Enter' to  skip)\n")
        if get_wish_book in wish_book:
            book.append(get_wish_book)
            print(f"Updated library: {book}")
            wish_book.remove(get_wish_book)
            print(f"Updated Wishlist: {wish_book}")
            donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
            if donate:
                if donate in book:
                    book.remove(donate)
                    print(f"Final library after Donations: {book}")
                else:
                    print("Sorry, you don't own this book, Enter another book into your library.")
            else:
                print(f"Final library: {book}")
        else:
            print("Sorry, This book is not on your wish list")
            donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
            if donate:
                if donate in book:
                    book.remove(donate)
                    print(f"Final library after Donations: {book}")
                else:
                    print("Sorry, you don't own this book, Enter another book into your library.")
            else:
                print(f"Final library: {book}")
    else:
        print(f"Wishbook list: {wish_book}")
        donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
        if donate:
            if donate in book:
                book.remove(donate)
                print(f"Final library after Donations: {book}")
            else:
                print("Sorry, you don't own this book, Enter another book into your library.")
        else:
            print(f"Final library: {book}")
else:
    print(f"Your library: {book}")
    wish_book = [input("Enter the name of a book you wish to have in the future:\n")]
    another_wish_book = input("Enter the name of anoter book you wish to have (or press 'Enter' to  skip)\n")
    if another_wish_book:
        wish_book.append(another_wish_book)
        print(f"Your Wishlist: {wish_book}")
        get_wish_book = input("Enter the name of a book from your wishlist that you've already got it (or press 'Enter' to  skip)\n")
        if get_wish_book in wish_book:
            book.append(get_wish_book)
            print(f"Updated library: {book}")
            wish_book.remove(get_wish_book)
            print(f"Updated Wishlist: {wish_book}")
            donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
            if donate:
                if donate in book:
                    book.remove(donate)
                    print(f"Final library after Donations: {book}")
                else:
                    print("Sorry, you don't own this book, Enter another book into your library.")
            else:
                print(f"Final library: {book}")
        else:
            print("Sorry, This book is not on your wish list")
            donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
            if donate:
                if donate in book:
                    book.remove(donate)
                    print(f"Final library after Donations: {book}")
                else:
                    print("Sorry, you don't own this book, Enter another book into your library.")
            else:
                print(f"Final library: {book}")
    else:
        print(f"Wishbook list: {wish_book}")
        donate = input("Enter the name of book from your library you wish to donate (or press 'Enter' to  skip)\n")
        if donate:
            if donate in book:
                book.remove(donate)
                print(f"Final library after Donations: {book}")
            else:
                print("Sorry, you don't own this book, Enter another book into your library.")
        else:
            print(f"Final library: {book}")