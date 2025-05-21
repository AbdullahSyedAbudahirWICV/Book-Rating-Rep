# used classes to improve code organization, reliability, and future scalability ensuring the program is easy to read, test, and extend.
class Book:
    def __init__(self, title, rating):  # This line defines the attributes as mentioned in the pseudocode of a book which is the title and rating
        self.title = title
        self.rating = rating

class Library:
    def __init__(self):  # This Define is used to set the data type to a list which is book_list
        self.book_list = []

    def add_book(self, title, rating):  # This creates a new book in the list
        book_obj = Book(title, rating)
        self.book_list.append(book_obj)

    def get_total_books(self):  # This basically is kind of a funtion which calcultes the length of the book_list that we mentioned above
        return len(self.book_list)

    def calculate_avg_rating(self):  # This adds the ratings of the books and divides buy the lenth of the book list which is number of books
        if not self.book_list:
            return 0.0
        total_rating = sum(book.rating for book in self.book_list)
        return total_rating / len(self.book_list)

def main():  # The Class of Library Ends here and now the main program starts
    my_library = Library()

    while True:
        book_title = input("Right then, enter the name of your book - or type 'done' if you've finally had enough: ")# This takes an input from the user and stores it in the list in the above mentioned class.
        if book_title.lower() == "done":
            break

        try:
            book_rating = float(input("Go on, enter the rating (1.00 to 5.00): "))#This does the same thing, Takes the input verifies if its Valid Input (Validation and stores in the above class attribute.)
            if 1.0 <= book_rating <= 5.0:
                my_library.add_book(book_title, book_rating)
            else:
                print("That's not fair. It's between 1.0 and 5.0, not whatever number you just made up.")
        except ValueError:
            print("Brilliant. You've entered something that isn't even a number. Try again using digits.")

    total_books = my_library.get_total_books()#This calls the total_books defintion from above and implements it in our librar as declared above.
    average_rating = my_library.calculate_avg_rating()#This does the same thing as above.

    print("The ratings are in: 5, 4, 3, 2, 1")
    print("Total number of books: " + str(total_books))
    print("Average rating: " + str(round(average_rating, 2)))

# Entry point
main()