<div align="center">

<img src="library_banner.svg" alt="Library System Banner" width="100%">

<br>

**A robust, console-based Library Management System engineered with Python OOP.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![OOP](https://img.shields.io/badge/Architecture-OOP-4B5563?style=for-the-badge&logo=gitbook&logoColor=white)](#)
[![Regex](https://img.shields.io/badge/Validation-Regex-059669?style=for-the-badge&logo=regular-expressions&logoColor=white)](#)
[![Terminal](https://img.shields.io/badge/CLI-Terminal-0f172a?style=for-the-badge&logo=gnome-terminal&logoColor=white)](#)

*Demonstrating core backend fundamentals: Abstract Classes, Exception Handling, Serialization, and modular code architecture.*

</div>

<br>

# 📚 Library Management System (Python OOP)

A fully functional **console‑based Library Management System** built using **Python OOP**, with features like user roles, borrowing limits, ISBN validation, and persistent storage using `pickle`.

This project demonstrates strong fundamentals in:

* Object‑Oriented Programming
* Abstract Classes
* Exception Handling
* Serialization (Saving/Loading State)
* Input Validation (Regex)
* Clean, modular code structure

---

## 🚀 Features

### 🧩 Book Management

* Add new books with **ISBN validation** (13‑digit format)
* Prevent duplicate book entries using custom exception
* Search books by **title** or **author**

### 👥 User Management

* Two user types:

  * **Student** (borrow limit: 3)
  * **Staff** (borrow limit: 5)
* Adds user with **email** and **UAE phone number regex validation**

### 📖 Borrowing System

* Users can borrow books only if:

  * They haven't reached their borrow limit
  * The book isn't already borrowed
* Custom exceptions for borrow limit violations
* Returning books updates the book status properly

### 💾 Save / Load System

* Save the entire library state to a file using `pickle`
* Load previously saved system state

---

## 🏗️ Project Structure

```
LibrarySystem/
│── library.py              # Main library classes
│── main.py                 # Entry point with menu
│── README.md               # Documentation
│── saved_state.pkl         # (example saved file)
```

---

## 📦 Installation

```bash
# Clone the repository
$ git clone https://github.com/<your-username>/library-system.git
$ cd library-system

# Run the project
$ python main.py
```

---

## 🖥️ Usage

Once you run the script, the following menu will appear:

```
----- Library System -----
1. Add Book
2. Add User (Student/Staff)
3. Borrow Book
4. Return Book
5. Search Book
6. Save Library State
7. Load Library State
8. Exit
```

Follow the menu prompts to manage your library.

---

## 🧪 Exception Handling Included

* **InvalidISBNException** – triggered when ISBN is not 13 digits
* **BookAlreadyExistException** – prevents duplicate books
* **BorrowLimitExceededException** – prevents users from exceeding borrow limits

---

## ✔️ Example Input Validations

| Field     | Validation                | Regex              |
| --------- | ------------------------- | ------------------ |
| ISBN      | 13 digits                 | `^\d{13}$`         |
| Email     | simple format check       | `^\w+@\w+\.\w{3}$` |
| UAE Phone | +971 followed by 9 digits | `^\+971\d{9}$`     |

---

## 📸 Demo

*(Optional: you can later add screenshots of the console output here)*

---

## 🧱 Technologies Used

* Python 3
* OOP Principles
* ABC (Abstract Base Classes)
* Regular Expressions
* Pickle Module

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## ⭐ Acknowledgment

Written as part of a **Python OOP coursework project**.

---

## 🔗 GitHub Repository

Replace with your link:

```
https://github.com/mishal636/Library-Management-System-Python-OOP-
```

