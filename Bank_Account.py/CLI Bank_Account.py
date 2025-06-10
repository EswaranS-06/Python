class Bank_Account():
    
    def __init__(self, account_holder):
        
        self.account_holder = account_holder
        print(f"\n An Account has been created Successfully under the name of {self.account_holder} \n\n")
        self.balance = 0.0
        
    def deposit(self, deposites):
        if deposites <= 0:
            raise ValueError(f"Amount shoudle be above zero'0'")
        
        self.balance +=  deposites
        print("Deposit successful!\n")
        
    def withdraw(self, withdraws):
        if withdraws > self.balance:
            raise ValueError(f"\nYour A/C balance is {self.balance} So your unable to withdraw {withdraws}")
            
        self.balance -= withdraws
        print("Withdrawal successful!\n")
        
    def get_balance(self):
        print(f"\tYour Account Balance \n _________________________ \n {self.balance}$ \n _________________________ \n\n ")
        
    def __str__(self):
        return f" \tAccount Holder,s Details \n \tName:- {self.account_holder} \n \tBalance:- {self.balance} \n _________________________\n\n"
    
    

print("welcome to CLI Bank ")
acc = Bank_Account(input(f"Enter your Name:- "))
    
flow = True
    
print("""\tSelect an option: 
            1. Deposit
            2. Withdraw
            3. Check Balance
            4. Account Info
            0. Exit
            """)
    
while flow:
    c = int(input("Enter your choise:- "))
        
    if c == 1:
        acc.deposit(int(input("Enter the amount to Deposit:- ")))
        
    elif c == 2:
        acc.withdraw(int(input("Enter the amount to Withdraw:- ")))
            
    elif c == 3:
        acc.get_balance()
            
    elif c == 4:
        print(acc)
            
    elif c == 0:
        
        print("CLI process has been suspended")
        break
    

    