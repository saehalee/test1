import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rurxnrl707",
    database="testdb"

)

mycursor = mydb.cursor()

sql = "select * from universities where name = ''"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)