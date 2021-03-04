import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="db_employee"
)
cursor=db.cursor()
empdata = open("data_employee", "r")
list=[]
for data in empdata:
    emp_dat = data.rstrip("\n").split(",")
    insert_query="INSERT INTO employee(eid,ename,desig,salary) VALUES (%s,%s,%s,%s)"
    cursor.execute(insert_query,emp_dat)
    db.commit()
