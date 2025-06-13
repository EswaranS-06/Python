import mysql.connector as sql
mydb = sql.connect(
  host="localhost",
  user="root",
  password="2726",
  database='mydatabase'
)

mc = mydb.cursor()

sql = 'insert into customers (name, address, id) values (%s,%s,%s)'

while True:
    c = int(input("[1] to add , [2] to show and [0] to exit"))
    if c == 1:
        name = input("Enter your name: ")
        address = input("Enter your Address: ")
        id = int(input("Enter your ID: "))
        
        val = (name, address,id)

        mc.execute(sql,val)

        mydb.commit()

        print('1 record inserted, id:', mc.lastrowid)
        
    elif c == 2:
        sel = input('''Select details you want :
                1 -> Name
                2 -> Address
                3 -> Id
Enter the details from the list :''')
        amd = ''
        if '1' in sel:
            amd +='name '
        if '2' in sel:
            amd += 'address '
        if '3' in sel:
            amd += 'id '       
        cmd = 'select '+amd.rstrip().replace(' ',', ')+' from customers'
        print(cmd)
        mc.execute(cmd)
        res = mc.fetchall()
        for x in res:
            print(x)
        
    elif c == 0:
        break
    
print("the datas for add")