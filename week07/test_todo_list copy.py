import pytest
from todo_list import delete_task, display_tasks, display_menu, add_task, delete_task
import mysql.connector
import random

# create the connection with db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joPM9Lm8*+C",
    database="tasks"
)
mycursor = mydb.cursor()

def test_add_task():
    """This function will test add a tasks and its importance to
    the db
    Parameters: It take no parameters.
    """
    #create a list and randomly choose the importance level of a task
    importance_list = ["H", "M", "L"]
    random_number = random.randint(0, (len(importance_list)))
    importance_level = importance_list[random_number]
    assert importance_level == "H" or importance_level == "M" or importance_level == "L", "Please enter a valid importance level"

    # insert into table using INSERT INTO statement
    sql = "INSERT INTO tasks (task, importance) VALUES (%s, %s)"
    new_task = "Test task"
    values_to_insert = (new_task, importance_level)

    mycursor.execute(sql, values_to_insert)

    mydb.commit()

def test_display_menu():
    """
    This will test if the elements of the menu are the corrects.
    It will compare the expected items of the menu against
    the actual items at the menu.
    Parameters: It will take no parameters.
    """
    expected_items = ["Add Task", "Delete Task", "Exit"]
    current_items = display_menu()
    assert current_items == expected_items

pytest.main(["-v", "--tb=line", "-rN", __file__])