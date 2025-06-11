import time as t
class Bank():
    
    def __init__(self, account_holder, age):
        
        self.account_holder = account_holder
        print(f"\n An Account has been created Successfully under the name of {self.account_holder} \n\n")
        self.balance = 0.0
        self.age = age
        
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
        return f" \tAccount Holder,s Details \n \tName:- {self.account_holder} \n \tBalance:- {self.balance} \n _________________________\n \tAge:- {self.age}  \n \n"
cus = {}    
print('Welcome to CLI Bank ')
while(True):
    print(f'''
          1. To Create a new A/c
          2. Login to Existing A/c
          ''')
    c = int(input('Enter your choie:'))
    if c == 1:
        name = input('Enter your Name:')
        age = int(input('Enter your Name:'))
        t.sleep(2)
        ac = int(input('Crate a New Account Number 1000-9999: '))
        t.sleep(4)
        if ac 