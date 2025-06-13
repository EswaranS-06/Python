import mysql.connector as sql
mydb = sql.connect(
  host="localhost",
  user="root",
  password="2726",
  database='bank'
)

mc = mydb.cursor('alter table customers add column bal float')
