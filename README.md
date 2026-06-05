# BankingTransactions

##create: BankAccount class, deposit, withdraw, check balance, handling insufficient balance in account by giving inputs by user dynamically  class BankingTransactions

BankingTransactions is a simple Python class that simulates basic banking operations:

Withdraw money

Deposit money

Check account balance

A small CLI (Command Line Interface) loop is included so users can interact with the account through text input.

🧩 Class Structure
BankingTransactions
This class stores the account balance and provides three main methods:

withdraw(amount) — Deducts money if sufficient balance exists

deposit(amount) — Adds money to the account

check_balance() — Returns the current balance

Code Explanation

1. Initialize Account
python
initial_balance = float(input("Enter initial balance for the account: "))
account = BankingTransactions(initial_balance)
The user enters a starting balance, and an object is created.

2. User Action Loop
The program runs continuously until the user types exit.

Supported actions:

deposit → Add money

withdraw → Remove money

check → Display balance

exit → Stop the program

Example Usage
Code
Enter initial balance for the account: 500
Enter 'deposit', 'withdraw', 'check', or 'exit': deposit
Enter amount to deposit: 200
Balance after depositing: 700.0

Features
Simple and beginner‑friendly

Uses Object-Oriented Programming

Validates insufficient balance during withdrawal

Interactive CLI for real‑time testing

How to Run
Save the script as Banking_Transactions.py

Run in terminal:

Code
python Banking_Transactions.py
Follow the on‑screen prompts.

📌 Future Enhancements (Optional)
Add transfer() between accounts

Add transaction history

Add PIN authentication

Add interest calculation

will enhance one by one 

Add transfer() between accounts  will add this feature now 

Feature 1: Add transfer() Between Accounts

Goal
Allow money to move from one BankingTransactions object to another.

What transfer() must do
Check if sender has enough balance

Deduct amount from sender

Add amount to receiver

Return success/failure message

Update Banking_Transactions.py class with Transfer function 

Reuses withdraw() and deposit()

Avoids duplicate logic

Easy to extend later (e.g., transaction history)

Example: Transfer Both Ways

# A to B
ex: account1.transfer(100, account2)

# B to  A
ex: account2.transfer(50, account1)

No extra conditions needed.
The OOP design handles it naturally.

Visual Understanding
Here’s the mental model:

account1.transfer(100, account2)
   sender = account1
   receiver = account2

account2.transfer(50, account1)
   sender = account2
   receiver = account1

Whichever object calls the method is the sender.

we want to add safety for that
we can add a check to prevent transferring negative or zero amounts:

def transfer(self, amount, receiver_account)  and def transfer_bothways(self, amount, receiver_account) i have added methods to understand but we avoid def transfer(self, amount, receiver_account) in real working environments 

Feature 2: Add Transaction History
What we want
Every time the user performs an action, we store a record:

deposit

withdraw

transfer (sent or received)

balance check

Each record should include:

action type

amount

resulting balance

timestamp

