class Bank_Account():
    
    def __init__(self, account_holder):
        
        self.account_holder = account_holder
        self.balance = 0.0
        
    def deposit(self, deposites):
        self.balance +=  deposites
        
    def withdraw(self, withdraws):
        if withdraws > self.balance:
            print(f"Your A/C balance is {self.balance} So your unable to withdraw {withdraws}")
            
        else:
            self.balance -= withdraws
        
    def get_balance(self):
        return f"Your Account Balance \n _________________________ \n {self.balance}$ \n _________________________ \n\n "
        
    def __str__(self):
        return f" Account Holder,s Details \n \tName:- {self.account_holder} \n \tBalance:- {self.balance} \n _________________________"
    
    
acc = Bank_Account("Alice")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(800)  # This should raise an error

bal = acc.get_balance()
print(bal)
print(acc)
