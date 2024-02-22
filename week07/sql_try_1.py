import mysql.connector

# -----> STEP 1
# create the connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    # you can add the database name to specify you are working with it
    database="mydatabase"
)

# print(mydb)

mycursor = mydb.cursor()


# -----> STEP 2
# to create a new data base
# if it runs without error, it was created succesfully
# mycursor.execute("CREATE DATABASE mydatabase")


# -----> STEP 3
# Check if database exits
# mycursor.execute("SHOW DATABASES")

# this will print all the db created
# for x in mycursor:
#     print(x)


# -----> STEP 4
# creating a table
# if it runs without error, it was created succesfully
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# -----> STEP 5
# check if table exists
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

# -----> STEP 6
# insert into table using INSERT INTO statement
# name_to_insert = "John"
# address_to_insert = "Highway 21"
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

## val = ("John", "Highway 21")
# val = (name_to_insert, address_to_insert)

# mycursor.execute(sql, val)

# Important!: Notice the statement: mydb.commit(). It is
# required to make the changes, otherwise no changes are made to the table.
# mydb.commit()

# -----> STEP 7
# select all records from the "customers" table
# mycursor.execute("SELECT * FROM customers")

# We use the fetchall() method, which fetches all rows from 
# the last executed statement.
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# -----> STEP 8
# fetch one row (will return the first row of the result)
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult) 



# -------------------------------------------
# -----> NO NUMBER STEP
# DROP a table
# mycursor.execute("DROP TABLE customers")

# -----> NO NUMBER STEP
# alter existing table to add PRIMARY KEY
# mycursor.execute(
#     "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# -----> NO NUMBER STEP
# insert multiple rows
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
