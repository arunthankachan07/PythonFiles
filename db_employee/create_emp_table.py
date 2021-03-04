import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="db_employee"
)

#step3 create a cursor object
cursor=db.cursor()
sql="CREATE TABLE employee(eid varchar(80),ename varchar(80), desig varchar(80),salary int)"

cursor.execute(sql)
