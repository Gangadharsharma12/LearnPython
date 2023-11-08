import mysql.connector

mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         passwd="Raghavendra@123",
         database = "book_shop",
         auth_plugin="mysql_native_password"
)
cur = mydb.cursor(buffered=True)
print(mydb)


print('\n'*100)

