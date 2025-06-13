import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    password='2726',
    database='bank'
)

def all_info():
    mc = mydb.cursor()
    cmd = 'Select * from customers '
    mc.execute(cmd)
    allInfo = mc.fetchall()
    for info in allInfo:
        print(f""" 
        _________________________
        Account Holder,s Details
            - Name:- {info[1]}
            - A/c no:- {info[0]}
            - Balance:- {info[4]}
            - Phone no: - {info[2]}
            - Address:- {info[3]}
        _________________________
        """)
    
    
def data_insert(ac, name, phone, address):

    mc = mydb.cursor()
    
    cmd = 'Select ac_no from customers where ac_no = %s'
    val = (ac, )
    mc.execute(cmd, val)
    
    if mc.fetchall() != []:
        print('Sorry, please Create a new account Thank you')
        return False
    
    cmd = 'insert into customers (ac_no, name, phone_no, address, bal) values (%s,%s,%s,%s,%s)'
    val = (ac, name, phone, address, 0.0)
    
    mc.execute(cmd, val)
    
    mydb.commit()
    
    print(mc.rowcount, 'was inserted')
    print('A/c no: ',ac)
    
def data_sel(ac):
    mc = mydb.cursor()
    cmd = 'Select ac_no from customers where ac_no = %s'
    val = (ac, )
    mc.execute(cmd, val)
    
    if mc.fetchall() == []:
        print('Sorry there is no account that number\nplease check the A/c number or\nCreate a new account\nThank you')
        return False
    
    return True

def add_bal(ac, dep):
    mc = mydb.cursor()
    cmd = 'Select bal from customers where ac_no = %s'
    val = (ac,)
    mc.execute(cmd, val)
    cu_bal = mc.fetchall()[0][0]
    bal = cu_bal + dep
    cmd = 'update customers set bal = %s where ac_no = %s' 
    val = (bal, ac)
    
    mc.execute(cmd, val)
    
    mydb.commit()
    print("The Amount has been Credited\n_________________________________\n")
    
def draw_bal(ac, draw):
    mc = mydb.cursor()
    cmd = 'Select bal from customers where ac_no = %s'
    val = (ac,)
    mc.execute(cmd, val)
    cu_bal = mc.fetchall()[0][0]
    
    if cu_bal <= draw:
        print("Insufficient Balance")
        return
    
    bal = cu_bal - draw
    cmd = 'update customers set bal = %s where ac_no = %s' 
    val = (bal, ac)
    
    mc.execute(cmd, val)
    
    mydb.commit()
    print("The Amount has been Debited\n_________________________________\n")
    
def check_bal(ac):
    mc = mydb.cursor()
    cmd = 'Select bal from customers where ac_no = %s'
    val = (ac,)
    mc.execute(cmd, val)
    cu_bal = mc.fetchall()[0][0]
    print(f"""
    Your Account Balance
    _________________________
        {cu_bal}₹ 
    _________________________ 
    """)
    
def ac_info(ac):
    mc = mydb.cursor()
    cmd = 'Select * from customers where ac_no = %s'
    val = (ac,)
    mc.execute(cmd, val)
    info = mc.fetchone()
    print(f""" 
    _________________________
    Account Holder,s Details
        - Name:- {info[1]}
        - A/c no:- {info[0]}
        - Balance:- {info[4]} ₹
        - Phone no: - {info[2]}
        - Address:- {info[3]}
    _________________________
    """)
    
def transfer(ac, tac, fund):
    mc = mydb.cursor()
    cmd = 'Select ac_no from customers where ac_no = %s'
    val = (tac, )
    mc.execute(cmd, val)
    
    if mc.fetchall() == []:
        return "Sorry Invalid A/c no to Transfer\n_________________________________\n"
    
    #get balance form login user ac
    cmd = 'select bal from customers where ac_no = %s'
    val = (ac,)
    mc.execute(cmd, val)
    cu_bal = mc.fetchone()[0]
    
    if cu_bal < fund:
        return f'Insufficient Balance current balance = {cu_bal}\n_________________________________\n'
    
    #get balance form transfer user ac
    val = (tac,)
    mc.execute(cmd, val)
    tcu_bal = mc.fetchone()[0]
    
    #opreation to tranfer fund
    bal = cu_bal - fund
    
    tbal = tcu_bal + fund
    
    cmd = 'update customers set bal = %s where ac_no = %s'
    #set balance into the login user ac
    val = (bal, ac)
    mc.execute(cmd, val)
    mydb.commit()
    
    #set balance into the transfer user ac
    val = (tbal, tac)
    mc.execute(cmd, val)
    mydb.commit()
    
    return f'The Fund[{fund} ₹] as been successfully Transfered to the A/c no [{tac}]\n_________________________________\n'