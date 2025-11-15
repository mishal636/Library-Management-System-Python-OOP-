from library import *

class MainMenu:
    def __init__(self):
        self.library = Library()

    def menu(self):
        while True:
            print("\n----- Library System -----")
            print("1. Add Book")
            print("2. Add User (Student/Staff)")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Search Book")
            print("6. Save Library State")
            print("7. Load Library State")
            print("8. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                try:
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    ISBN = input("Enter book ISBN (13 digits): ")

                    if not re.match(r"^\d{13}$", ISBN):
                        raise InvalidISBNException("Invalid ISBN")
                except InvalidISBNException as e:
                    print(e)
                else:
                    self.library.addBook(Book(title, author, ISBN))

            elif choice == 2:
                try:
                    name = input("Enter user name: ")
                    email = input("Enter user email: ")
                    telephone = input("Enter user telephone (+971xxxxxxxxx): ")
                    user_type = input("Enter user type (student/staff): ")

                    if not re.match(r"^\w+@\w+\.\w{3}$", email):
                        raise ValueError(f"Invalid email format: {email}")
                    if not re.match(r"^\+971\d{9}$", telephone):
                        raise ValueError(f"Invalid UAE telephone number: {telephone}")
                except ValueError as e:
                    print(e)
                else:
                    if user_type == "student":
                        self.library.addUser(Student(name, email, telephone))
                    else:
                        self.library.addUser(Staff(name, email, telephone))

            elif choice == 3:
                found = False
                name = input("Enter user name: ")
                title = input("Enter book title to borrow: ")

                if len(self.library.users) == 0 or len(self.library.books) == 0:
                    print("User or Book not found.")
                else:
                    for user in self.library.users:
                        if user.name == name:
                            for book in self.library.books:
                                if book.title == title:
                                    self.library.borrowBook(user, book)
                                    found = True
                if not found:
                    print("User or book not found.")

            elif choice == 4:
                name = input("Enter user name: ")
                title = input("Enter book title to return: ")
                found = False

                for user in self.library.users:
                    if user.name == name:
                        for book in user.borrowed_books:
                            if book.title == title:
                                self.library.returnBook(user, book)
                                found = True
                if not found:
                    print("User or book not found.")

            elif choice == 5:
                querytype = input("Search by (title/author): ")
                query = input("Enter search query: ")
                self.library.searchForBook(querytype, query)

            elif choice == 6:
                filename = input("Enter filename to save library state: ")
                self.library.saveState(filename)

            elif choice == 7:
                filename = input("Enter filename to load library state: ")
                self.library.loadState(filename)

            elif choice == 8:
                break

            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
