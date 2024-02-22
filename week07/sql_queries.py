import mysql.connector

# create the connection with db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    database="tasks"
)
mycursor = mydb.cursor()