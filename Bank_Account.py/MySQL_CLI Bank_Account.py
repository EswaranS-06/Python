import bank_sql as sql
import random as r

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
        ac = r.randint(1000,9999)
        
        sql.data_insert(name=name, ac=ac, phone=phone, address= address)
    #if to login to the existing account   
    if c == 2:
        ac = int(input('Enter your A/c no: '))
        print("""\t
        Select an option: 
            1. Deposit
            2. Withdraw
            3. Transfer Fund
            4. Check Balance
            5. Account Info
            0. Exit
            """)
        while sql.data_sel(ac=ac):
            c = int(input('Enter your choise: '))
            if c == 1:
                dep = int(input('Enter the amount to Deposit: '))
                sql.add_bal(ac=ac, dep=dep)
                
            
            elif c == 2:
                draw = int(input('Enter the amount to Withdraw: '))
                sql.draw_bal(ac=ac, draw=draw)
                
            elif c == 3:
                tac = int(input("Enter the A/c no to Transfer fund: "))
                fund = int(input("Enter the amount to Transfer: "))
                print(sql.transfer(ac=ac, tac=tac, fund=fund))
            
            elif c == 4:
                sql.check_bal(ac=ac)
            
            elif c == 5:
                sql.ac_info(ac=ac)
            
            elif c == 0:
                break
            
            else:
                print('Invalid selction')
                
    if c == 999:
        sql.all_info()