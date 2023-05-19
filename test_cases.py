import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file library.py exists.
import os.path
if(os.path.isfile("library.py")==False):
	print("Error you need to call the Python file library.py!")

# Check that the class is called library. That is, the file library.py contains the expression "library(object):"
file_text = open('library.py', 'r').read()
if("library(object):" not in file_text):
	print("Error you need to call the Python class library!")

sys.excepthook = Pyro5.errors.excepthook
library_obj = Proxy("PYRONAME:example.library")

# Tasks 1 & 2. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
result = library_obj.return_users()
print("Data returned:")
print(result)
print()

# Tasks 3 & 4. Initialize the remote object library_obj
library_obj.add_author("cc", "dd")
library_obj.add_author("ee", "ff")
result = library_obj.return_authors()
print("Data returned:")
print(result)
print()

# Tasks 5 & 6. Initialize the remote object library_obj
result = library_obj.return_books_not_loan()
print("Data returned:")
print(result)
print()

library_obj.add_author("aa", "dd")
library_obj.add_author("bb", "ff")
library_obj.add_book_copy("aa", "gg")
library_obj.add_book_copy("aa", "gg")
library_obj.add_book_copy("bb", "hh")
result = library_obj.return_books_not_loan()
print("Data returned:")
print(result)
print()

# Tasks 7 & 8. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
library_obj.add_author("cc", "zz")
library_obj.add_author("ee", "xx")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("ee", "ff")

result = library_obj.return_books_loan()
print("Data returned:")
print(result)
print()

result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
print("Data returned:")
print(result)
print()

result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
print("Data returned:")
print(result)
print()

result = library_obj.return_books_loan()
print("Data returned:")
print(result)
print()

# Task 9. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
library_obj.add_author("cc", "zz")
library_obj.add_author("ee", "xx")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("ee", "ff")
result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
result = library_obj.loan_book("bb", "dd", 2019, 1, 3)

result = library_obj.return_books_loan()
print("Data returned:")
print(result)
print()

result = library_obj.return_books_not_loan()
print("Data returned:")
print(result)
print()

library_obj.end_book_loan("bb", "dd", 2019, 2, 4)

result = library_obj.return_books_loan()
print("Data returned:")
print(result)
print()

result = library_obj.return_books_not_loan()
print("Data returned:")
print(result)
print()

# Task 10. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
library_obj.add_author("cc", "zz")
library_obj.add_author("ee", "xx")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("ee", "ff")

result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
library_obj.delete_book("ff")
library_obj.delete_book("dd")

result = library_obj.return_books_loan()
print("Data returned:")
print(result)
print()

result = library_obj.return_books_not_loan()
print("Data returned:")
print(result)
print()

# Task 11. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
library_obj.add_author("cc", "zz")
library_obj.add_author("ee", "xx")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("ee", "ff")

result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
library_obj.end_book_loan("aa", "ff", 2019, 2, 4)

print("The method delete_user should return a value of 1...")
result = library_obj.delete_user("aa")
print("Data returned:")
print(result)
print()

result = library_obj.delete_user("bb")
print("Data returned:")
print(result)
print()

result = library_obj.return_users()

print("Data returned:")
print(result)
print()

# Task 12. Initialize the remote object library_obj
library_obj.add_user("aa", 11)
library_obj.add_user("bb", 22)
library_obj.add_author("cc", "zz")
library_obj.add_author("ee", "xx")
library_obj.add_book_copy("cc", "dd")
library_obj.add_book_copy("ee", "ff")

result = library_obj.loan_book("aa", "ff", 2019, 1, 3)
library_obj.end_book_loan("aa", "ff", 2019, 2, 4)
result = library_obj.loan_book("bb", "dd", 2019, 1, 3)
library_obj.end_book_loan("bb", "dd", 2019, 2, 4)

result = library_obj.user_loans_date("aa", 2019, 1, 3, 2019, 3, 4)
print("Data returned:")
print(result)
print()

result = library_obj.user_loans_date("bb", 2019, 1, 3, 2019, 1, 4)
print("Data returned:")
print(result)
print()