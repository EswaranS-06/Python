import mysql.connector as sql

mydb = sql.connect(
    host='localhost',
    user='root',
    password='2726',
    database='bank'
)

cmd = mydb.cursor()

def data_insert(ac, name, phone):
    mydb = sql.connect(
        host='localhost',
        user='root',
        password='2726',
        database='bank'
    )

    cmd = mydb.cursor()
    cm = 'insert into customers (ac_no, name, phone_no) values (%s,%s,%s)'
    val = (ac, name, phone)
    
    cmd.execute(cm, val)
    
    mydb.commit()
    
    print(cmd.rowcount, 'was inserted')