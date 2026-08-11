# 🏦 Bank Management System — Python OOP

A **console-based Bank Management System** built using **Python Object-Oriented Programming (OOP)** concepts.

This project is designed as a practical OOP mini-project to understand how classes, objects, inheritance, abstraction, encapsulation, polymorphism, composition, custom exceptions, and modular project structure work together in a real-world application.

---

## 📌 Project Overview

The Bank Management System allows users to perform basic banking operations through a command-line interface.

### Main Operations

* Create a customer
* Create a savings account
* Create a current account
* Deposit money
* Withdraw money
* Transfer money
* Check account details
* View transaction history
* View all customers
* View all accounts
* Handle invalid transactions using custom exceptions

---

## 🎯 Learning Objectives

The main purpose of this project is to practice:

* Classes and Objects
* Constructors
* Encapsulation
* Abstraction
* Inheritance
* Polymorphism
* Method Overriding
* Composition
* Class Variables
* Static Methods
* Magic Methods
* Custom Exceptions
* Python Packages and Modules
* Separation of Responsibilities

---

# 📂 Project Structure

```text
bank-management-system/
│
├── main.py
│
├── bank/
│   ├── __init__.py
│   ├── bank.py
│   ├── customer.py
│   ├── account.py
│   ├── savings_account.py
│   ├── current_account.py
│   ├── transaction.py
│   └── exceptions.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── data/
│   └── transactions.txt
│
├── tests/
│   ├── __init__.py
│   ├── test_account.py
│   ├── test_customer.py
│   └── test_bank.py
│
├── README.md
└── requirements.txt
```

---

# 🧱 Class Architecture

```text
                         Bank
                          │
             ┌────────────┴────────────┐
             │                         │
         Customers                  Accounts
             │                         │
         Customer              ┌───────┴────────┐
                               │                │
                         SavingsAccount   CurrentAccount
                               │                │
                               └───────┬────────┘
                                       │
                                    Account
                                       │
                                  Transactions
```

---

# 🧩 Classes

## 1. `Customer`

The `Customer` class represents a bank customer.

### Attributes

```text
customer_id
name
email
phone
accounts
```

### Main Methods

```python
add_account()
show_accounts()
```

---

## 2. `Account`

`Account` is an **Abstract Base Class (ABC)**.

It contains common functionality shared by different account types.

### Attributes

```text
account_number
owner
_balance
transactions
```

### Main Methods

```python
deposit()
withdraw()
get_balance()
show_transactions()
```

`withdraw()` is defined as an abstract method because different account types have different withdrawal rules.

---

## 3. `SavingsAccount`

Inherits from:

```python
Account
```

### Rules

* Minimum balance: ₹500
* Maximum withdrawal per transaction: ₹20,000
* Interest rate: 4%

Example:

```text
Account
   ↓
SavingsAccount
```

---

## 4. `CurrentAccount`

Inherits from:

```python
Account
```

### Rule

* Overdraft limit: ₹10,000

Example:

```text
Account
   ↓
CurrentAccount
```

---

## 5. `Transaction`

The `Transaction` class stores information about banking transactions.

### Attributes

```text
transaction_id
transaction_type
amount
description
timestamp
```

Supported transaction types include:

```text
DEPOSIT
WITHDRAW
TRANSFER
```

---

## 6. `Bank`

The `Bank` class acts as the main service/controller of the application.

It manages:

```text
Customers
Accounts
Deposits
Withdrawals
Transfers
Account searches
```

---

# 🧠 OOP Concepts Demonstrated

## 1. Class and Object

Classes act as blueprints for objects.

Example:

```python
customer = Customer(
    "Om",
    "om@gmail.com",
    "7559216096"
)
```

Here:

```text
Customer → Class
customer → Object
```

---

## 2. Encapsulation

The account balance is stored as:

```python
self._balance
```

The balance is modified through controlled methods:

```python
deposit()
withdraw()
```

This prevents other parts of the application from directly modifying the account balance.

---

## 3. Abstraction

The project uses Python's `ABC` module:

```python
from abc import ABC, abstractmethod
```

The `Account` class defines:

```python
@abstractmethod
def withdraw(self, amount):
    pass
```

This forces subclasses to provide their own withdrawal implementation.

---

## 4. Inheritance

`SavingsAccount` and `CurrentAccount` inherit from `Account`.

```python
class SavingsAccount(Account):
    ...
```

```python
class CurrentAccount(Account):
    ...
```

This allows common account functionality to be reused.

---

## 5. Polymorphism

Both account types implement:

```python
withdraw()
```

but their behavior is different.

```text
SavingsAccount
      ↓
withdraw()
      ↓
Minimum balance + withdrawal limit


CurrentAccount
      ↓
withdraw()
      ↓
Overdraft support
```

The Bank class can simply call:

```python
account.withdraw(amount)
```

without knowing which account type it is.

---

## 6. Composition

A customer can have multiple accounts.

```python
self.accounts = []
```

Relationship:

```text
Customer
   │
   ├── Savings Account
   ├── Current Account
   └── Savings Account
```

This represents a **has-a relationship**.

---

## 7. Class Variables

The project uses class variables to generate unique IDs.

Example:

```python
customer_counter = 1000
```

and:

```python
account_counter = 10000
```

This produces IDs such as:

```text
CUST1001
CUST1002

ACC10001
ACC10002
```

---

## 8. Static Methods

The `Bank` class contains validation methods such as:

```python
@staticmethod
def validate_email(email):
    ...
```

These methods don't require access to object-specific data.

---

## 9. Magic Methods

The project uses:

```python
__str__()
```

to provide readable object representations.

For example:

```python
print(customer)
```

produces customer information instead of the default Python object representation.

---

## 10. Custom Exceptions

The project defines banking-specific exceptions:

```python
BankError
InvalidAmountError
InsufficientBalanceError
AccountNotFoundError
CustomerNotFoundError
```

Example:

```python
raise InsufficientBalanceError(
    "Insufficient balance."
)
```

This makes error handling more meaningful and organized.

---

# 🖥️ Application Menu

When the application starts:

```text
======================================================================
              PYTHON OOP BANK
======================================================================
1. Create Customer
2. Create Account
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Check Account Details
7. Transaction History
8. Show All Customers
9. Show All Accounts
10. Exit
======================================================================
Enter your choice:
```

---

# 🚀 How to Run

## Step 1 — Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd bank-management-system
```

---

## Step 2 — Check Python

Make sure Python is installed:

```bash
python --version
```

Recommended:

```text
Python 3.10+
```

---

## Step 3 — Install Dependencies

This project currently uses only Python's standard library.

Therefore:

```bash
pip install -r requirements.txt
```

does not require any third-party packages.

---

## Step 4 — Run the Application

```bash
python main.py
```

---

# 🔄 Example Workflow

### Create Customer

```text
Enter choice: 1

Enter name: Om Jawanjalkar
Enter email: om@example.com
Enter phone: 7559216096

Customer created successfully!

Customer ID: CUST1001
```

### Create Account

```text
Enter choice: 2

Enter customer ID: CUST1001

1. Savings Account
2. Current Account

Choose account type: 1

Enter amount: ₹5000

Account created successfully!

Account Number: ACC10001
```

### Deposit

```text
Enter choice: 3

Enter account number: ACC10001
Enter amount: ₹2000

₹2000.00 deposited successfully.
```

### Check Balance

```text
Enter choice: 6

Account Number : ACC10001
Account Holder : Om Jawanjalkar
Account Type   : SavingsAccount
Balance        : ₹7000.00
```

---

# 🛡️ Error Handling

The application handles common banking errors.

### Invalid Amount

```text
Error: Amount must be greater than zero.
```

### Account Not Found

```text
Error: Account not found.
```

### Insufficient Balance

```text
Error: Savings account must maintain minimum balance of ₹500.
```

### Invalid Phone Number

```text
Error: Phone number must contain exactly 10 digits.
```

---

# 🧪 Testing

Unit tests can be placed inside:

```text
tests/
```

Example:

```text
tests/
├── test_account.py
├── test_customer.py
└── test_bank.py
```

Testing can be added using Python's built-in:

```python
unittest
```

or the third-party:

```text
pytest
```

---

# 🔮 Future Improvements

This project can be extended with:

* [ ] User authentication
* [ ] PIN/password authentication
* [ ] Change PIN
* [ ] Daily transaction limits
* [ ] Savings interest calculation
* [ ] Transaction persistence
* [ ] SQLite database
* [ ] User login system
* [ ] Account statement generation
* [ ] Unit testing
* [ ] Logging
* [ ] REST API using Flask/FastAPI
* [ ] Web interface
* [ ] Docker support

---

# 📚 Concepts Practiced

```text
Python
│
├── OOP
│   ├── Classes & Objects
│   ├── Constructors
│   ├── Encapsulation
│   ├── Abstraction
│   ├── Inheritance
│   ├── Polymorphism
│   ├── Composition
│   ├── Method Overriding
│   ├── Class Variables
│   ├── Static Methods
│   └── Magic Methods
│
├── Exception Handling
│   ├── Custom Exceptions
│   └── try / except
│
└── Project Structure
    ├── Modules
    ├── Packages
    └── Separation of Responsibilities
```

---

# 🎓 Learning Outcome

After completing this project, you should be able to explain:

> **How OOP concepts can be combined to build a real-world application.**

You should particularly be able to explain the difference between:

```text
Encapsulation
       ↓
Protect and control data


Abstraction
       ↓
Hide implementation details


Inheritance
       ↓
Reuse existing functionality


Polymorphism
       ↓
Same interface, different behavior
```

---

# 👨‍💻 Author

**Om Jawanjalkar**

Computer Science & Engineering — Data Science

---

# ⭐ If You Found This Useful

If this project helped you understand Python OOP, consider giving the repository a ⭐ on GitHub.
