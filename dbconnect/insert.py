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
query_insert="INSERT INTO student VALUES('100','ram',300)"
cursor.execute(query_insert)
db.commit()
#data=cursor.fetchone()
#print(data)