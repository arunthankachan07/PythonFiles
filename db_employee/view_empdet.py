import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password",
    database="db_employee"
)
cursor=db.cursor()
view_query="SELECT * FROM employee"
cursor.execute(view_query)
data=cursor.fetchall()
for datas in data:
    print(datas)

#highest salary
max_sal_query="SELECT MAX(salary) FROM employee"
cursor.execute(max_sal_query)
max_sal=cursor.fetchone()
print("Highest Salary ",max_sal)




#print employee name with maximum salary
sql="SELECT ename FROM employee WHERE salary=(SELECT MAX(salary) FROM employee)"
cursor.execute(sql)
maxsal_empname=cursor.fetchone()
print("Employee with maximum salary ",maxsal_empname)


