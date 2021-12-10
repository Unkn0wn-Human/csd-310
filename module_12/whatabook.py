import sys
import mysql.connector
from mysql.connector import errorcode

# This configures the connection information that the program will use to connect the database.
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
# Function that shows the user the menu when called. 
def display_menu():
    print("\n-- Main Menu --")
    print("1. Display Books\n2. View Store Locations\n3. My Account\n4) Exit Program")

    # this try/except will catch if the user put in an incorrect input. If its incorrect it will show an error message and exit the program.
    try:
        choice = int(input("Choose a number from the options: "))
        return choice

    except ValueError:
        print("\n An invalid entry occurred, Exiting program...")
        sys.exit(0)

# function for when the user selects display books. 
def display_books(_cursor):

    # collects book information from the book table.
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    
    books = cursor.fetchall()

    print("\n-- DISPLAYING BOOK LISTING --")

    # shows the book information.
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[1], book[2], book[3]))

# function for when the user selects view store locations. 
def display_locations(_cursor):

    # gets the store_id and the locations from the store table.
    _cursor.execute("SELECT store_id, locale from store")

    # sets the locations variable equal to the data pulled above.
    locations = _cursor.fetchall()

    print("\n-- DISPLAYING STORE LOCATIONS --")

    # iterates through the locations data to display all the store entries.
    for location in locations:
        print("Locale: {}\n".format(location[1]))

# function for getting the user's user_id and validate it to confirm if it is valid.
def validate_user():
# Array of all the valid User IDs
    validUserIds = ["1", "2", "3"]

    # Storing the users input to check if its valid
    userID = input("Enter your ID: ")

    # Checks if valid. If not it asks again.
    while userID not in validUserIds:
        print("\n** Invalid user ID. **\n")
        userID = input("Enter your user ID: ")
    # if its valid it will return it.
    if userID in validUserIds:
        validUserID = int(userID)
        return user_id

# Shows the account menu
def show_account_menu():
    
    # checks to see if the menu option chosen is valid or not. 
    try:
        print("\n--Customer Menu --")
        print("\n1. Wishlist\n2. Add Book\n3. Main Menu")

        option_chosen = int(input("Choose a number from the options: "))

        return option_chosen

    # if the menu option chosen wasn't valid, this will run.
    except ValueError:
        print("\nInvalid menu option\n")
        sys.exit(0)

# this function can be called to view all the books in a user's wishlist.
def display_wishlist(_cursor, _user_id):

    #this cursor collects information from across multiple tables then uses two inner joins to display the matching information collected.
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    
    wishlist = _cursor.fetchall()

    print("\n --DISPLAYING WISHLIST ITEMS --")

    # printing the wishlist book information.
    for book in wishlist:
        print("\nBook Name: {}\nAuthor: {}\n".format(book[4], book[5]))

# this function when called displays all the books that the whatabook company has that aren't already in the user's wishlist.
def show_books_to_add(_cursor,_user_id):

    # this query selects information from the book table that is not already in the wishlist table.
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    # this sets the cursor to hold the values from the query variable.
    _cursor.execute(query)

    # this sets the books_to_add variable equal to all the information being currently held by the cursor.
    books_to_add = _cursor.fetchall()

    print("\n-- DISPLAYING AVAILABLE BOOKS --")

    # this iterates through all the books that were being held in the books_to_add variable, presenting the available books that can be added to the user's wishlist.
    for book in books_to_add:
        print("\nBook ID: {}\nBook Name: {}\n".format(book[0], book[1]))

# this function can be called when the user wishes to add new books to their wishlist.
def add_book_to_wishlist(_cursor,_user_id,_book_id):

    # this function inserts the book information into the wishlist table based on the user's selection(s)
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

# tries to connect to the database using the config information above.
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("\nWelcome to the WhatABook Application!")

    # this calls the display_menu() method and sets the user_selection equal to the result returned from this.
    user_selection = display_menu()

    # this while statement allows the user to keep choosing different menu options as long as the option is not 4 (to exit the program).
    while user_selection != 4:

        # this if statement allows the user to view all the books that the WhatABook company sells.
        if user_selection == 1:
            display_books(cursor)
        
        # this if statement allows the user to view the different locations for the WhatABook company.
        if user_selection == 2:
            display_locations(cursor)
        
        # this if statement allows the user to verify their user_id then view the account_menu as long as the user_id was valid.
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # this while statement allows the user to stay inside the customer menu as long as the user doesn't enter option 3 to return to main menu.
            while account_option != 3:

                # this if statement is what allows the user to view their wishlist by calling the display_wishlist() method.
                if account_option == 1:
                    display_wishlist(cursor, my_user_id)
                
                # this if statement is what allows the user to add books to their wishlist by calling the show_books_to_add() and add_book_to_wishlist() methods.
                if account_option == 2:
                    display_books_to_add(cursor, my_user_id)
                    book_id = int(input("\nEnter the book ID of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # this commits the changes above to the database.
                    db.commit()

                    print("\nBook ID: {} was added to your wishlist!".format(book_id))

                # this ensures that if the customer is entering negative values or values over 3 that it will keep prompting them to enter the correct value until they do.
                if account_option < 0 or account_option > 3:
                    print("\nInvalid option, please try again...")

                account_option = show_account_menu()

        # this ensures that if the user enters negative values or values over 4 that it will keep prompting them to enter the correct value until they do.
        if user_selection < 0 or user_selection > 4:
            print("\nInvalid option, please try again...")

        # this calls the disply_menu() method after the menu has been left.
        user_selection = display_menu()
    print("\n\nProgram terminated...")

# if the ER_ACCESS_DENIED_ERROR or ER_BAD_DB_ERROR errors are presented
# this prints the appropriate error message based on the error. 
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
# close database connection
finally:
    db.close()