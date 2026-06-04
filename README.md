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
