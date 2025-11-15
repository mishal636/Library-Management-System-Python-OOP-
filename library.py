from abc import ABC
import pickle, re


class InvalidISBNException(Exception):
pass


class BorrowLimitExceededException(Exception):
pass


class BookAlreadyExistException(Exception):
pass


class Book:
def __init__(self, title, author, ISBN):
self.ISBN = ISBN
self.title = title
self.author = author
self.is_borrowed = False


def __str__(self):
return f"Book(title={self.title}, author={self.author}, isbn={self.ISBN})"


class LibraryUser(ABC):
def __init__(self, name, email, telephone, borrow_limit):
self.name = name
self.email = email
self.telephone = telephone
self.borrow_limit = borrow_limit
self.borrowed_books = []


class Student(LibraryUser):
def __init__(self, name, email, telephone):
super().__init__(name, email, telephone, borrow_limit=3)


class Staff(LibraryUser):
def __init__(self, name, email, telephone):
super().__init__(name, email, telephone, borrow_limit=5)


class Library:
def __init__(self):
self.books = []
self.users = []


def addBook(self, newBook):
try:
for book in self.books:
if book.ISBN == newBook.ISBN:
raise BookAlreadyExistException(
f"Book with ISBN {newBook.ISBN} already exists in the library.")
self.books.append(newBook)


except BookAlreadyExistException as e:
print(e)
else:
print(f"Book '{newBook.title}' added successfully!")


def addUser(self, user):
self.users.append(user)
print(f"User '{user.name}' added successfully!")


def borrowBook(self, user, book):
if len(user.borrowed_books) < user.borrow_limit and not book.is_borrowed:
book.is_borrowed = True
user.borrowed_books.append(book)
print(f"Book '{book.title}' borrowed successfully!")
elif len(user.borrowed_books) == user.borrow_limit:
raise BorrowLimitExceededException(f"{user.name} has exceeded their borrowing limit.")
else:
print("Book already borrowed")


def returnBook(self, user, book):
user.borrowed_books.remove(book)
book.is_borrowed = False
print(f"Book '{book.title}' returned successfully!")


def searchForBook(self, querytype, query):
if len(self.books) == 0:
print("No items found.")
return


found_any = False
print(f"File '{filename}' not found.")
