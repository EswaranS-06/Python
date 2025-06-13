import time as t
import error_check as ec
import bank_sql as sql
class Bank():
    
    def __init__(self, account_holder, age):
        
        self.account_holder = account_holder
        print(f"\n An Account has been created Successfully under the name of [{self.account_holder}] \n\n")
        self.balance = 0.0
        self.age = age
        
    def deposit(self, deposites):
        if deposites <= 0:
            raise ValueError(f"Amount shoudle be above zero'0'")
        
        self.balance +=  deposites
        print("Deposit successful!\n")
        
    def withdraw(self, withdraws):
        if withdraws > self.balance:
            raise ValueError(f"\nYour A/C balance is [{self.balance}] So your unable to withdraw [{withdraws}]")
            
        self.balance -= withdraws
        print("Withdrawal successful!\n")
        
    def get_balance(self):
        print(f"""
    Your Account Balance
    _________________________
        {self.balance}$ 
    _________________________ 
    """)
        
    def __str__(self):
        return f""" 
    _________________________
    Account Holder,s Details
        - Name:- {self.account_holder}
        - Age:- {self.age}
        - Balance:- {self.balance}
    _________________________
    """
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
        age = int(input('Enter your Age:'))
        t.sleep(1)
        ac = int(input('Crate a New Account Number 1000-9999: '))
        t.sleep(1)
        if ec.none_check(cus, ac):
            acc = Bank(name, age)
            cus.update({ac:acc})
            c = 2
        else:
            print(f'''
        The Account number [{ac}] is Already Taken''')
            
    if c == 2:
        
        ac = int(input('Enter your A/c no: '))
        if ec.none_check(cus, ac):
            print(f'''
        Sorry, You don't have an Account in this [{ac}]
        Please create an Account to continue  
                ''')
        else:        
            print("""\tSelect an option: 
                        1. Deposit
                        2. Withdraw
                        3. Check Balance
                        4. Account Info
                        0. Exit
                        """)
            
            while True:
                c = int(input("Enter your choise:- "))
                op = cus[ac]   
                if c == 1:
                    op.deposit(int(input("Enter the amount to Deposit:- ")))
                    
                elif c == 2:
                    op.withdraw(int(input("Enter the amount to Withdraw:- ")))
                        
                elif c == 3:
                    op.get_balance()
                        
                elif c == 4:
                    print(op)
                    
                elif c == 0:
                    break
                
    if c == 3:
        ec.write(cus)