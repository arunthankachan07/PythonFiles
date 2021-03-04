import mysql.connector
#step2 establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

#step3 create a cursor object
cursor=db.cursor()
query_read="select * from student"
cursor.execute(query_read)

data=cursor.fetchone()
print(data)