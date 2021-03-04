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
sql="CREATE TABLE student(sid varchar(80),s_name varchar(80), marks int)"
#query_insert="INSERT INTO student VALUES('100','ram',300)"
cursor.execute(sql)
#data=cursor.fetchone()
#print(data)