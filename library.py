# Mariia Semenenko
# Student ID: 22100679

import Pyro5.api
import datetime


@Pyro5.api.expose # Make the class available for remote usage
class Author:
    # Initialize author's name and genre
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    # Compare the equality of two authors based on their name and genre
    def __eq__(self, other):
        return self.name == other.name and self.genre == other.genre

    # Generate a hash value for an object based on its name and genre
    def __hash__(self):
        return hash(self.name + self.genre)

@Pyro5.api.expose
class Book:
    # Initialize book's author and title
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.loaned_to = None
        self.loan_date = None
        self.return_date = None
        self.previous_loaner = None

    # Compare the equality of two books based on their title and author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Generate a hash value for an object based on its title and author
    def __hash__(self):
        return hash(self.title + self.author)


@Pyro5.api.expose
class User:
    # Initialize user's name and number
    def __init__(self, name, number):
        self.name = name
        self.number = number

    # Compare the equality of two users based on their name and number
    def __eq__(self, other):
        return self.name == other.name and self.number == other.number

    # Generate a hash value for an object based on its name and number
    # Convert the latter to the string before hashing
    def __hash__(self):
        return hash(self.name + str(self.number))


@Pyro5.api.expose
class library(object):
    # Initialize users, authors and books
    def __init__(self):
        self.users = set() # Each user is unique in the library -> set
        self.authors = set() # Each author is unique in the library -> set
        self.books = [] # Multiple copies of the same book can exist -> array

    # Task 1. Add a new user to the library
    def add_user(self, user_name, user_number):
        self.users.add(User(user_name, user_number))
        print(f"User {user_name} ({user_number}) has been added to the library system.")

    # Task 2. Return all users from the library
    def return_users(self):
        str = "All users in the library system:"
        for user in self.users:
            str += "\n\t- {0} ({1})".format(user.name, user.number)
        return str

    # Task 3. Add a new author to the library
    def add_author(self, author_name, author_genre):
        self.authors.add(Author(author_name, author_genre))
        print(f"Author {author_name} ({author_genre}) has been added to the library system.")

    # Task 4. Return all authors from the library
    def return_authors(self):
        str = "All authors in the library system:"
        for author in self.authors:
            str += "\n\t- {0} ({1})".format(author.name, author.genre)
        return str

    # Task 5. Add a new book copy to the library
    def add_book_copy(self, author_name, book_title):
        self.books.append(Book(author_name, book_title))
        print(f"A new copy of '{book_title}' by {author_name} has been added to the library system.")

    # Task 6. Return all books not loaned
    def return_books_not_loan(self):
        not_loan_books = set()
        for book in self.books:
            if book.loaned_to is None:
                not_loan_books.add(book)
        if len(not_loan_books) >= 1:
            str = "The following books are available for loan:"
            for book in not_loan_books:
                str += "\n\t- '{0}' by {1}".format(book.title, book.author)
            return str
        else:
            return "There are no books available for loan at the moment."

    # Task 7. Loan a book to a specified user on a specified date
    def loan_book(self, user_name, book_title, year, month, day):
        for book in self.books:
            if book.title == book_title and book.loaned_to is None:
                book.loaned_to = user_name
                book.loan_date = datetime.date(year, month, day)
                print(f"'{book_title}' has been loaned to {user_name} since {year}-{month}-{day}.")
                return 1
        print(f"'{book_title}' is not available for loan at the moment.")
        return 0

    # Task 8. Return all books loaned from the library
    def return_books_loan(self):
        loaned_books = set()
        for book in self.books:
            if book.loaned_to is not None:
                loaned_books.add(book)
        if len(loaned_books) >= 1:
            str = "The following books have been loaned out:"
            for book in loaned_books:
                str += "\n\t- '{0}' by {1}".format(book.title, book.author)
            return str
        else:
            return "There are currently no books on loan."

    # Task 9. Return a loaned book by a specified user on a specified date
    def end_book_loan(self, user_name, book_title, year, month, day):
        for book in self.books:
            if book.title == book_title and book.loaned_to == user_name:
                book.previous_loaner = book.loaned_to
                book.loaned_to = None
                book.return_date = datetime.date(year, month, day)
                print(f"'{book_title}' has been returned by {user_name} on {year}-{month}-{day}.")
                return 1
        print(f"'{book_title}' was not found or was not loaned by {user_name}.")
        return 0

# Task 10. Delete a specified book (all copies) from the library
    def delete_book(self, book_title):
        count = 0
        i = 0
        while i < len(self.books):
            if self.books[i].title == book_title and self.books[i].loaned_to is None:
                self.books.pop(i)
                count +=1
            else:
                i +=1
        if count == 0:
            print(f"No copies of '{book_title}' were found or are currently on loan.")
        elif count == 1:
            print(f"'{book_title}' has been removed from the library system.")
        else:
            print(f"All {count} copies of '{book_title}' have been removed from the library system.")
        return count

    # Task 11. Delete a specified user from the library
    def delete_user(self, user_name):
        for book in self.books:
            if book.loaned_to == user_name or book.previous_loaner == user_name:
                print(f"{user_name} has/had books on loan and cannot be deleted.")
                return 0
        for user in self.users:
            if user.name == user_name:
                self.users.remove(user)
                print(f"{user_name} has been deleted from the library system.")
                return 1
        print(f"{user_name} was not found.")
        return 0

    # Task 12. Return all books a specified user previously has loaned between a specified start and end dates
    def user_loans_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        loaned_books = []
        start_date = datetime.date(start_year, start_month, start_day)
        end_date = datetime.date(end_year, end_month, end_day)
        for book in self.books:
            if book.loaned_to is None and book.previous_loaner == user_name and (start_date <= book.return_date <= end_date) and (start_date <= book.loan_date <= end_date):
                loaned_books.append(book)
        if len(loaned_books) == 0:
            return "{0} has not loaned any books between {1} and {2}.".format(user_name, start_date, end_date)
        else:
            str = "{0} has loaned and returned the following books between {1} and {2}:".format(user_name, start_date, end_date)
            for book in loaned_books:
                str += "\n\t- '{0}' by {1}, between {2} and {3}".format(book.title, book.author, book.loan_date, book.return_date)
        return str
        

# Start the Pyro5 server
daemon = Pyro5.api.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(library)
ns.register("example.library", uri)
print("Library server running.")
daemon.requestLoop()