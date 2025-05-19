# === Book Class ===
class Book:
    """
    Represents a book with a title and rating.
    """
    def __init__(self, title: str, rating: float):
        self.title = title
        self.rating = rating

# === Library Class ===
class Library:
    """
    Stores a list of Book objects and provides operations like adding books,
    counting them, and calculating average ratings.
    """
    def __init__(self):
        self.book_list = []

    def add_book(self, title: str, rating: float):
        """
        Creates a new Book object and adds it to the book list.
        """
        book_obj = Book(title, rating)
        self.book_list.append(book_obj)

    def get_total_books(self) -> int:
        """
        Returns the total number of books in the library.
        """
        return len(self.book_list)

    def calculate_avg_rating(self) -> float:
        """
        Calculates and returns the average rating of all books.
        Returns 0.0 if no books are in the list.
        """
        if not self.book_list:
            return 0.0
        total_rating = sum(book.rating for book in self.book_list)
        return total_rating / len(self.book_list)

# === Main Program Logic ===
def main():
    """
    Main function to run the book rating program.
    """
    my_library = Library()

    while True:
        book_title = input("Enter book name or type 'done' to finish: ").strip()
        if book_title.lower() == "done":
            break

        try:
            book_rating = float(input("Enter rating (1.0 to 5.0): "))
            if 1.0 <= book_rating <= 5.0:
                my_library.add_book(book_title, book_rating)
            else:
                print("Invalid rating. Please enter a number between 1.0 and 5.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric rating.")

    total_books = my_library.get_total_books()
    average_rating = my_library.calculate_avg_rating()

    print("--- Library Summary ---")
    print(f"Total number of books: {total_books}")
    print(f"Average rating: {average_rating:.2f}")

# Run the program
if __name__ == "__main__":
    main()
