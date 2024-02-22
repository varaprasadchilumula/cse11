import imp
from multiprocessing.sharedctypes import Value
import mysql.connector

# create the connection with db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    database="tasks"
)
mycursor = mydb.cursor()

# create a new db
# mycursor.execute("CREATE DATABASE tasks")

# create a new table with the tasks of the user
# the columns where modified
# mycursor.execute(
#     "CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))")


def main():
    run = True
    print("|----------------------------------------------|")
    print("|------------------TO-DO List------------------|")
    print("|----------------------------------------------|")
    print("\n")

    while run:
        print("\n|----------------Current tasks-----------------|")
        print("|--ID |  Task |  Importance -------------------|")
        print("|----   -----   -------------------------------|")
        display_tasks()
        print("|----------------------------------------------|")
        # display menu to the screen
        display_menu()
        # the user will choose what to do
        user_choice = int(input("What you want to do? (1, 2 or 3) "))
        # add task to the todo list
        if user_choice == 1:
            add_task()
        # delete task from the todo list
        elif user_choice == 2:
            delete_task()
        # exit the program
        elif user_choice == 3:
            run = False


def display_tasks():
    """
    This function will make a loop to the elements in the db
    to display all the tasks that need to be performed.
    Parameters: It will take no parameters.
    """
    mycursor.execute("SELECT * FROM tasks")

    myresult = mycursor.fetchall()

    ID_INDEX = 0
    TASK_INDEX = 1
    IMPORTANCE_INDEX = 2

    for row in myresult:
        print(
            f"|---{row[ID_INDEX]} | {row[TASK_INDEX]} | {row[IMPORTANCE_INDEX]}")


def display_menu():
    """This function will display the elements of the menu
    so the user can choose what action to perform.
    Parameters: It will take no parameters.
    """
    menu_items = ["Add Task", "Delete Task", "Exit"]
    counter = 1
    print("\n")
    for item in menu_items:
        print(f"{counter}. {item}")
        counter += 1
    return menu_items


def add_task():
    """This function will add a tasks and its importance to
    the db
    User will have to enter the taks to perform and
    its importance as input
    Parameters: It take no parameters.
    """
    print("\n")
    new_task = input("What are you planning to do? ")
    importance_text = ("\nH=High | M=Medium | L=Low\nLevel of importance? ")
    importance_level = input(importance_text)
    importance_level = importance_level.upper()

    assert importance_level == "H" or importance_level == "M" or importance_level == "L", "Please enter a valid importance level"

    # insert into table using INSERT INTO statement
    sql = "INSERT INTO tasks (task, importance) VALUES (%s, %s)"

    values_to_insert = (new_task, importance_level)

    mycursor.execute(sql, values_to_insert)

    mydb.commit()


def delete_task():
    """ This function will delete a tasks and everything about it 
    from the db
    User will have to enter the ID number of the task you want to delete.
    Parameters: It take no parameters.
    """
    user_choice = input("Enter the ID of the task you want to delete: ")
    # delete from table using DELETE FROM statement
    sql = "DELETE FROM tasks WHERE id = %s"

    task_id = (user_choice, )

    mycursor.execute(sql, task_id)

    mydb.commit()


if __name__ == "__main__":
    main()
