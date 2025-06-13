import bank_sql as sql

print('Welcome to the CLI Bank')
while True:
    print('''
    1. To Create an Account
    2. To login into the Existing A/c
    0. To Exit
          ''')
    c = int(input('Enter your choise: '))
    
    #if to  create an account
    if c == 1:
        name = input('Enter your Name:- ')
        address = input('Enter your Address:- ')
        phone = int(input('Enter your Phone No:- '))
        