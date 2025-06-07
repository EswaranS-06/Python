import random as r
class Bank_Account:
    def __init__(self, customer_name, balance, account_number):
        self.account_number = account_number
        self.balance = float(balance)
        self.customer_name = customer_name
        
    def __str__(self):
        return (self.customer_name)
    
    def de(self):
        self.balance
    
    def print_info(self):
        print(f"_________{self.customer_name}__________\nName: {self.customer_name}\nAccount Number: {self.account_number}\nBank Balance: {self.balance}\n")
    
    
ram = Bank_Account("Ram Kumar", 10000.25, 202525)
ravi = Bank_Account("Ravi Chandran", 2000, 202526)

rex = Bank_Account(input("Enter your Name: "),int(input('Enter your current deposit: ')), r.randrange(1000,10000,10))

rex.print_info()
ram.print_info()
ravi.print_info()