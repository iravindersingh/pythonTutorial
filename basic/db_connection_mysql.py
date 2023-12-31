import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="init@123", database='test',auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
# mycursor.execute("show databases")

# result = mycursor.fetchall()

# result = mycursor.fetchone()
mycursor.execute("select * from student")
result = mycursor.fetchall()
print(result)

