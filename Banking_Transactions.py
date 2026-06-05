##create: BankAccount class, deposit, withdraw, check balance, handling insufficient balance in account by giving inputs by user dynamically 
import datetime

class BankingTransactions:
    def __init__(self, balance):
        self.balance = balance
        self.history = []  # store all transactions
    
    # Method to add transaction history with timestamp, action, amount, and balance
    def add_history(self, action, amount=0):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {action} | Amount: {amount} | Balance: {self.balance}"
        self.history.append(entry)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_history("Withdraw", amount) # Add to history
            return True
        else:
            print("No balance in account")
            self.add_history("Failed Withdraw", amount) # Add failed attempt to history
            return False

    def deposit(self, amount):
        self.balance += amount
        self.add_history("Deposit", amount) # Add to history

    def check_balance(self):
        self.add_history("Check Balance", 0) # Add balance check to history
        return self.balance

    #def transfer(self, amount, receiver_account):
    #    if self.withdraw(amount):
    #        receiver_account.deposit(amount)
    #        self.add_history("Transfer Sent", amount) # Add transfer sent to history
    #        receiver_account.add_history("Transfer Received", amount)
    #        print(f"Transferred {amount} successfully.")
    #    else:
    #        print("Transfer failed due to insufficient funds.")

    def transfer_bothways(self, amount, receiver_account):
        if amount <= 0:
            print("Invalid amount")
            self.add_history("Invalid Transfer Attempt", amount) # Add invalid transfer attempt to history
            return

        if self.withdraw(amount):
            receiver_account.deposit(amount)
            self.add_history("Transfer Sent", amount) # Add transfer sent to history
            receiver_account.add_history("Transfer Received", amount)
            print(f"Transferred {amount} successfully.")
        else:
            print("Transfer failed due to insufficient funds.")


# ------------------------------
# Main Program (CLI)
# ------------------------------

# Create two accounts for transfer demo
initial_balance = float(input("Enter initial balance for Account 1: "))
account1 = BankingTransactions(initial_balance)

initial_balance2 = float(input("Enter initial balance for Account 2: "))
account2 = BankingTransactions(initial_balance2)

print("\nYou can now perform actions on Account 1.")
print("To transfer, money will be sent from Account 1 to Account 2.\n")

while True:
    action = input("Enter 'deposit', 'withdraw', 'check', 'transfer', 'transfer_bothways' , 'history' , or 'exit': ").lower()
    
    if action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        account1.deposit(amount)
        print(f"Balance after depositing: {account1.check_balance()}")
        
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)
        print(f"Balance after withdrawing: {account1.check_balance()}")
        
    elif action == 'check':
        print(f"Current balance: {account1.check_balance()}")

    elif action == 'transfer':
        amount = float(input("Enter amount to transfer to Account 2: "))
        account1.transfer(amount, account2)
        print(f"Account 1 balance: {account1.check_balance()}")
        print(f"Account 2 balance: {account2.check_balance()}")

    elif action == 'transfer_bothways':
        direction = input("Transfer from 1 to 2 or 2 to 1 ? Enter 'a' or 'b': ").lower()
        
        amount = float(input("Enter amount to transfer: "))
        
        if direction == 'a':
            account1.transfer(amount, account2)
            print("Transferred from Account 1 to Account 2")
        elif direction == 'b':
            account2.transfer(amount, account1)
            print("Transferred from Account 2 to Account 1")
        else:
            print("Invalid transfer direction")

        print(f"Account 1 balance: {account1.check_balance()}")
        print(f"Account 2 balance: {account2.check_balance()}")

    

    elif action == 'history':
        print("\n--- Account 1 History ---")
        for entry in account1.history:
            print(entry)

        print("\n--- Account 2 History ---")
        for entry in account2.history:
            print(entry)
        print("---------------------------\n")

    elif action == 'exit':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid action. Please try again.")
            
