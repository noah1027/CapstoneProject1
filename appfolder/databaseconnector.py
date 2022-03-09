import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Password1!",
auth_plugin='mysql_native_password')



dbcursor = db.cursor()
#commented these out because the database is already created, the next two lines will show the existing databases
#dbcursor.execute("CREATE DATABASE Appdata2")
#dbcursor.execute("SHOW DATABASES")
#print(dbcursor.execute("SHOW DATABASES"))