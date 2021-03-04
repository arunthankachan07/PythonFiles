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
query_update="UPDATE student SET s_name='arun',marks=400 WHERE sid='100'"
cursor.execute(query_update)
db.commit()
#data=cursor.fetchone()
#print(data)