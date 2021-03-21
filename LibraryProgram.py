# This is my coursework for the programming 1 module of my computing science course
# It is a program which reads a list of books in from a file and performs some functions on the file contents

import math
import matplotlib.pyplot as plt

# Creating all the lists that are needed for the program 
authors = []
title = []
backing = []
publisher = []
cost = []
stock = []
genre = []
lists = [authors, title, backing, publisher, cost, stock, genre]
# Below is a list of the headings of the other lists that was initially used for the 'books_formatted' function
# listHeadings = ['AUTHOR', 'TITLE', 'BACKING', 'PUBLISHER', 'COST', 'STOCK', 'GENRE']

# Opening the text file and reading the contents into lists
book_file = open("BookFile.txt", "r")
lines = book_file.readlines()
for l in lines:
    if not l.startswith('#'):  # Ignore any line that starts with a #
        asList = l.split(', ')
        authors.append(asList[0].strip())
        title.append(asList[1].strip())
        backing.append(asList[2].strip())
        publisher.append(asList[3].strip())
        cost.append(float(asList[4]))
        stock.append(int(asList[5]))
        genre.append(asList[6].replace('\n', ''))  # Removes the \n at the end of each line


def main():
    # Where all of the main function will be called 
    print('Book store management\n'
          '1. Show a summary of current stock available\n'
          '2. Output average price of books in stock\n'
          '3. List the number of books in each genre type\n'
          '4. Add a new book and show summary of the increase in number of titles in stock and the cost '
          'difference in average price of books in stock\n'
          '5. Increase or decrease the stock level of a book due to a sale\n'
          '6. List the books in order by title or genre\n'
          '7. Show a bar chart that presents the number of books existing in each genre\n'
          '8. Exit')

    loop = True
    while loop == True:

        spacer()
        choice = input('Enter an option: ')
        spacer()
        if choice == '1':
            books_formatted(range(len(lists[0])))
            spacer()
            print('Total number of titles available:', (len(title)))
            total_stock_price()
        elif choice == '2':
            print('Average price of books in stock: £' + str(avg_book_price()))
        elif choice == '3':
            genre_count(genre)
        elif choice == '4':
            add_book()
        elif choice == '5':
            stock_update()
        elif choice == '6':
            sorted_order()
        elif choice == '7':
            bar_chart()
        elif choice == '8':
            print('Thank you for using this program.')
            loop = False
        else:
            print('You need to enter a valid menu option.')


def spacer():
    # Called to help make distinguishing between function calls easily for the user
    print(
        '_______________________________________________________________________________________________'
        '_______________________')


def books_formatted(index_list):
    # for i in range(len(list_headings)):
    # lists[i].insert(0, list_headings[i])
    # Formats the list of books by calculating the length of the longest element in the list
    # take the difference to each other element
    # use the difference to calculate how many tabs are needed to align every column correctly
    for ei in index_list:
        for li in range(len(lists)):
            longest = 0
            curr_list = lists[li]
            for i in range(len(curr_list)):
                length = len(str(curr_list[i]))  
                # Find the longest element and if it is longer than current longest then
                # replace current longest
                if length > longest:
                    longest = length
            length = len(str(curr_list[ei]))
            difference = longest - length
            after_longest = 4 - (longest % 4)
            tabs_needed = math.ceil((difference + after_longest) / 4.0)  # math.ceil is used to always round up
            # as round() would sometimes leave it short
            print(str(curr_list[ei]) + (tabs_needed * '\t'),
                  end='')  # Print as a string each element and then the amount of tabs needed
        print()  # Take a new line after each list has been indexed by 1
    # for i in range(len(list_headings)):
    # lists[i].pop(0)


def total_stock_price():
    # Finds the total price of all books that are in stock
    # Multiplies each index of stock with respective index of cost and adds that to a total variable
    stock_total = 0
    for i in range(len(authors)):
        total_stock_price = stock[i] * cost[i]
        stock_total += total_stock_price
    print('Total price of stock: £' + str(stock_total))


def avg_book_price():
    # Returns the average price of books that are in stock 
    # Multiplies each index of stock with respective index of cost and divides by total amount of books
    stock_total = 0
    for i in range(len(authors)):
        total_stock_price = stock[i] * cost[i]
        stock_total += total_stock_price
    total_books = (sum(stock))
    avg_price_stock = format(float(stock_total / total_books), '.2f')  # Formats result to 2 decimal places
    return avg_price_stock


def genre_count(genre):
    # Prints out a list of genres from the list genre and the frequency they appear 
    genre_freq = {}
    print('Books in each genre')
    for type in genre:
        # For each time that a genre appears +1 to the value for that genre in the dictionary
        if type in genre_freq:
            genre_freq[type] += 1
        else:
            genre_freq[type] = 1
    for book_genre, count in genre_freq.items():  # Format the dictionary and print each key and value to a new line
        print('% s \t: % d' % (book_genre, count))


def add_book():
    # Takes the details of a new book and appends each detail to the correct list
    # Print how much the total stock has increased
    # Print how the average price of books in stock has changed
    loop = True
    while loop == True:
        print('Please enter the details of the new book')
        stock_before = sum(stock)
        price_before = float(avg_book_price())
        authors.append(input('Authors name: '))
        title.append(input('Book title: '))
        backing.append(input('PB or HB: '))
        publisher.append(input('Publishers name: '))
        # Try/ except argument used to avoid users entering something that isn't an int or float
        while True:
            try:
                cost.append(float(input('How much does the book cost: ')))
            except ValueError:
                print('Please enter a number as the price for the book')
            else:
                break
        while True:
            try:
                stock.append(int(input('Current stock: ')))
            except ValueError:
                print("Please enter a whole number for the current stock")
            else:
                break
        genre.append(input('Book genre: '))
        stock_after = sum(stock)
        price_after = float(avg_book_price())
        spacer()
        print('The total stock has increase by: ' + str(stock_after - stock_before))
        print('The average price of books has changed by ' + str(round(price_after - price_before, 2)) + ' pounds')
        spacer()
        # Check if the user would like to enter details for another book
        y_or_n = input('Would you like to enter the details for another book? Y for yes, anything else for no: ')
        if y_or_n.upper() == 'Y':
            loop = True
        else:
            loop = False


def stock_update():
    # Allows the user to search for a book by the title and change the stock level
    loop = True
    while loop == True:
        stock_dict = dict(
            zip(title, stock))  # Create a dictionary to link the contents of the lists 'title' and 'stock together
        book_search = str(
            input('Enter the name of the book you would like to search or type N if you would like to stop: '))
        spacer()
        if book_search in stock_dict:
            # Takes the user input and checks if there is a match in the dictionary
            print('Yes this book is in our files!')
            print('There are ' + str(stock_dict[book_search]) + ' of this book available in stock')
            spacer()
            nest_loop = True
            while nest_loop == True:
                print('Would you like to increase or decrease stock for this book?')
                # User input to determine how the user would like to change the stock
                stock_change = input('I for increase\n'
                                     'D for decrease\n'
                                     'N for no change\n')
                spacer()
                if stock_change.upper() == 'I':
                    increase = int(input('How many would you like to increase stock by?: '))
                    # book_index finds index of the book title the user entered and uses that to find the relevant
                    # stock, the correct index for stock is then redefined as the current value + the user entered
                    # value
                    book_index = title.index(book_search)
                    stock[book_index] = stock[book_index] + increase
                    print('The stock for this book is now: ', stock[book_index])
                    spacer()
                    loop = stock_update_cont()  # Called to see if the user would like to change another books s11tock
                    # level
                    nest_loop = False
                elif stock_change.upper() == 'D':
                    decrease = int(input('How many would you like to decrease stock by?: '))
                    book_index = title.index(book_search)
                    stock[book_index] = stock[book_index] - decrease
                    nest_loop = False
                    # Check if the new stock level is below 0 and stop that from happening will add the amount
                    # decreased by back to the stock and flag that the amount cannot go below zero
                    if stock[book_index] < 0:
                        print('Stock cannot go below 0')
                        stock[book_index] += decrease
                        spacer()
                        loop = stock_update_cont()
                    elif stock[book_index] == 0:
                        print('Stock for this book is now at 0')
                        spacer()
                        loop = stock_update_cont()
                    else:
                        print('Stock for this book is now at', stock[book_index])
                        spacer()
                        loop = stock_update_cont()

                elif stock_change.upper() == 'N':
                    nest_loop = False
                else:
                    print('You did not enter a correct option, please try again')
                    spacer()
        elif book_search == 'N':
            loop = False
        else:
            print('Either this book does not exist or you have misspelled the title')
            spacer()


def stock_update_cont():
    # Determines if the user would like to search another book, to be used in the function 'stock_update'
    loop = True
    while loop == True:
        y_or_n = input('Would you like to search for another book? Y for yes, N for no: ')
        if y_or_n.upper() == 'Y':
            return True
        elif y_or_n.upper() == 'N':
            return False
        else:
            print('You did not enter a valid option')


def sorted_order():
    # Sorts the books by list title or genre and prints out all the details for each index in the correct order
    sort_method = input('Would you like to sort the books by title or genre?: ')
    if sort_method.upper() == 'TITLE':
        sorted_by_title = []
        title_sorted = sorted(title)
        for i in range(len(title)):
            # Compares the sorted list against the original list and
            # appends the new position of each titles index to a sorted_index
            sorted_index = title.index(title_sorted[i])
            sorted_by_title.append(sorted_index)
        books_formatted(
            sorted_by_title)  # Uses sorted_index as an arg in books_formatted to have details for each book printed
        # on the correct line
    elif sort_method.upper() == 'GENRE':
        sorted_by_genre = []
        nested_title_genre = []
        genre_sorted = sorted(genre)
        for i in range(len(genre)):
            title_and_genre = []
            title_and_genre.append(title[i])
            title_and_genre.append(genre[i])
            nested_title_genre.append(
                title_and_genre)  # Nested list used as .index() would only record the first instance of each type
        nested_title_genre.sort(key=lambda x: x[1])  # Sort the list by genre while keeping the title with the genre
        for i in range(len(genre)):
            # Similar to above although this time is iterating through a nested list so requires a second argument
            sorted_index = title.index(nested_title_genre[i][0])
            sorted_by_genre.append(sorted_index)
        books_formatted(sorted_by_genre)


def bar_chart():
    # Defines a dictionary to record the amount of each genre present and puts the contents into a bar chart
    genre_freq = {}
    for type in genre:  # Adds 1 to value of each genre as it encounters it
        if type in genre_freq:
            genre_freq[type] += 1
        else:
            genre_freq[type] = 1
    # Creates a list from the keys and values of the dictionary to be used in the barchart
    genres = list(genre_freq.keys())
    amount = list(genre_freq.values())
    plt.bar(genres, amount)
    plt.xlabel('Genres')
    plt.ylabel('Amount')
    plt.title('Amount of books per genre')
    plt.show()


main()
