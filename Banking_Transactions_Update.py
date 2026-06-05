##create: BankAccount class, deposit, withdraw, check balance, handling insufficient balance in account by giving inputs by user dynamically 
import datetime

def get_valid_pin():
        while True:
            pin = input("Set a 4‑digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                return pin
            print("Invalid PIN. PIN must be exactly 4 digits (0‑9).")

class BankingTransactions:
    def __init__(self, balance,pin):
        self.balance = balance
        self.history = []  # store all transactions
        self.pin = pin # Set a default PIN for simplicity (in real applications, this should be securely handled)
        self.is_locked = False
        self.wrong_attempts = 0

    # setting PIN for Authentication
    
    def authenticate(self): 
        if self.is_locked:
            print("Account locked due to too many wrong PIN attempts.")
            return False

        entered_pin = input("Enter PIN: ")
        if not (entered_pin.isdigit() and len(entered_pin) == 4):
            print("PIN must be exactly 4 digits.")
            return False

        if entered_pin == self.pin:
            self.wrong_attempts = 0
            return True
        else:
            self.wrong_attempts += 1
            print("Incorrect PIN")

            if self.wrong_attempts >= 3:
                self.is_locked = True
                print("Account locked due to 3 incorrect attempts.")

            return False     

    
    # Method to add transaction history with timestamp, action, amount, and balance

    def add_history(self, action, amount=0):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} | {action} | Amount: {amount} | Balance: {self.balance}"
        self.history.append(entry)

    # Banking Operations  withdraw , deposit , check balance , transfer money to another account and viceversa with authentication and history of transactions

    def withdraw(self, amount,skip_auth=False):
        if not skip_auth: # Allow skipping authentication for withdrawals (e.g., when transferring money to another account)
            if not self.authenticate(): # Authenticate before allowing withdrawal
                return False
        
        if self.balance >= amount:
            self.balance -= amount
            self.add_history("Withdraw", amount) # Add to history
            return True
        else:
            print("No balance in account")
            self.add_history("Failed Withdraw", amount) # Add failed attempt to history
            return False

    def deposit(self, amount,skip_auth=False):
        if not skip_auth: # Allow skipping authentication for deposits (e.g., when receiving a transfer)
            if not self.authenticate(): # Authenticate before allowing deposit
                return
        
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
    
    ## Two‑Way Transfer method that allows transferring money from one account to another and vice versa, with authentication and transaction history

    def transfer_bothways(self, amount, receiver_account):
        if not self.authenticate(): # Authenticate before allowing transfer
            return
        
        if amount <= 0:
            print("Invalid amount")
            self.add_history("Invalid Transfer Attempt", amount) # Add invalid transfer attempt to history
            return

        if self.withdraw(amount,skip_auth=True):  # Withdraw from sender account/ Skip authentication for withdrawal since it's already done at the start of this method
            receiver_account.deposit(amount,skip_auth=True) # Deposit to receiver account / Skip authentication for deposit since it's part of the transfer process
            self.add_history("Transfer Sent", amount) # Add transfer sent to history
            receiver_account.add_history("Transfer Received", amount)
            print(f"Transferred {amount} successfully.")
        else:
            print("Transfer failed due to insufficient funds.")
            self.add_history("Failed Transfer", amount)
            return False


# ------------------------------
# Main Program (CLI)
# ------------------------------

# Create two accounts for transfer demo
initial_balance = float(input("Enter initial balance for Account 1: "))
pin1 = get_valid_pin()  
#input("Set PIN for Account 1: ") # Set PIN for Account 1
account1 = BankingTransactions(initial_balance,pin1)

initial_balance2 = float(input("Enter initial balance for Account 2: "))
pin2 = get_valid_pin()
#input("Set PIN for Account 2: ") # Set PIN for Account 2
account2 = BankingTransactions(initial_balance2,pin2)

print("\nYou can now perform actions on Account 1.")
print("To transfer, money will be sent from Account 1 to Account 2.\n")

while True:
    action = input("Enter 'deposit', 'withdraw', 'check', 'transfer_bothways' , 'history' , or 'exit': ").lower()
    
    if action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        account1.deposit(amount)
        print(f"Balance after depositing: {account1.check_balance()}")
        
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        account1.withdraw(amount)
        print(f"Balance after withdrawing: {account1.check_balance()}")
        
    elif action == 'check':
        #print(f"Current balance: {account1.check_balance()}")

        acc = input("Check balance of Account 1 or 2? Enter 'a' or 'b': ")
        if acc == 'a':
            print(f"Current balance: {account1.check_balance()}")
        elif acc == 'b':
            print(f"Current balance: {account2.check_balance()}")
        else:
            print("Invalid choice")

    #elif action == 'transfer':
    #    amount = float(input("Enter amount to transfer to Account 2: "))
    #    account1.transfer(amount, account2)
    #    print(f"Account 1 balance: {account1.check_balance()}")
    #    print(f"Account 2 balance: {account2.check_balance()}")

    elif action == 'transfer_bothways':
        direction = input("Transfer from 1 to 2 or 2 to 1 ? Enter 'a' or 'b': ").lower()
        
        amount = float(input("Enter amount to transfer: "))
        
        if direction == 'a':
            success = account1.transfer_bothways(amount, account2)
            if success:
                print("Transferred from Account 1 to Account 2")
        elif direction == 'b':
            success = account2.transfer_bothways(amount, account1)
            if success:
                print("Transferred from Account 2 to Account 1")
        else:
            print("Invalid transfer direction")
          
        """
        if direction == 'a':   
            #account1.transfer(amount, account2)
            account1.transfer_bothways(amount, account2)
            print("Transferred from Account 1 to Account 2")
        elif direction == 'b':
            #account2.transfer(amount, account1)
            account2.transfer_bothways(amount, account1)
            print("Transferred from Account 2 to Account 1")
        else:
            print("Invalid transfer direction")
        """ 

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
            

