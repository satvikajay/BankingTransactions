# BankingTransactions

##create: BankAccount class, deposit, withdraw, check balance, handling insufficient balance in account by giving inputs by user dynamically  class BankingTransactions

BankingTransactions is a simple Python class that simulates basic banking operations:

Withdraw money

Deposit money

Check account balance

A small CLI (Command Line Interface) loop is included so users can interact with the account through text input.

Class Structure
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

Future Enhancements (Optional)
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

Example: Above Transfer method is one way that means always Account 1 to Account 2 but transfer takes place Both Ways Account 1 to Account 2 and viceversa

# Account 1 to Account 2
ex: account1.transfer(100, account2)

# Account 2 to Account 1
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

Which ever object calls the method is the sender.

we want to add safety for that
we need to add a check to prevent transferring negative or zero amounts
   ex:      if amount <= 0:
              print("Invalid amount")

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

Feature 3: PIN Authentication (Integrated Into Your Code)
What this feature adds
User must enter a PIN before performing:

deposit

withdraw

transfer_bothways

PIN is set once when the account is created

If PIN is wrong transaction is blocked

After 3 wrong attempts  account locks

How we implement it
We add:

self.pin
Stores the PIN for each account.

self.is_locked
Prevents further transactions after too many wrong attempts.

authenticate()
Checks PIN before allowing any action.

Modify deposit(), withdraw(), transfer_bothways()
Each will call authenticate() first. 
for better understanding adding new file with enhanced feature3  in Banking_Transactions_Update.py


In Banking_Transactions_Update.py

this code is after Feature 3 (PIN Authentication), plus the fixes we added for:

4‑digit PIN validation

Account lock after 3 wrong attempts

Skip double PIN during transfer -- enter pin at the starting point of the transfer amount 

Return success/failure for transfer

Check balance for both accounts

Clean transaction history

Correct transfer messages

this code is now a fully working banking system with Feature 1, 2, and 3 completed.

Below features

Feature 1 — Basic Banking Operations
1. deposit
2. withdraw
3. check balance
4. insufficient balance handling
5. dynamic user input

Status: Completed

Feature 2 — Transaction History
1. timestamp
2. action
3. amount
4. balance
5. logs for:

deposit

withdraw

failed withdraw

transfer sent

transfer received

failed transfer

check balance

Status: Completed

Feature 3 — PIN Authentication
1. 4‑digit PIN
2. PIN validation
3. authenticate() method
4. wrong attempts counter
5. account lock after 3 wrong attempts
6. skip_auth for transfer
7. no double PIN during transfer
8. secure deposit/withdraw

Status: Completed



