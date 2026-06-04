class BankingTransactions:
    def __init__(self,balance):
        #self.name=name
        self.balance=balance

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=amount
        else:
            print("No balance in account")

    def deposit (self,amount):
        self.balance+=amount

    def check_balance(self):
        return self.balance 
    
initial_balance = float(input("Enter initial balance for the account: "))
account = BankingTransactions(initial_balance)
while True:
    action = input("Enter 'deposit', 'withdraw', 'check', or 'exit': ").lower()
    
    if action == 'deposit':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        print(f"Balance after depositing: {account.check_balance()}")
        
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print(f"Balance after withdrawing: {account.check_balance()}")
        
    elif action == 'check':
        print(f"Current balance: {account.check_balance()}")
        
    elif action == 'exit':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid action. Please try again.")


            
