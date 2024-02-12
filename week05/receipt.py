from ast import If
import csv
from itertools import product
from datetime import datetime


def main():
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    print("\nWelcome to AMAZING STORE")
    print("************************")
    print("\nOrdered items: ")

    try:
        products_dict = read_dict("week05/products.csv", 0)

        with open("week05/request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            # for the requested elements
            REQUESTED_PRODUCT_INDEX = 0
            REQUESTED_QUANTITY_INDEX = 1

            # for the products_dict elements
            PRODUCT_NAME_INDEX = 1
            PRODUCT_COST_INDEX = 2

            # counter for the amount of ordered items
            ordered_items_total = 0
            subtotal = 0

            for row_list in reader:
                requested_product_number = row_list[REQUESTED_PRODUCT_INDEX]
                requested_quantity = row_list[REQUESTED_QUANTITY_INDEX]

                for key, product in products_dict.items():

                    name = product[PRODUCT_NAME_INDEX]
                    cost = product[PRODUCT_COST_INDEX]

                    if requested_product_number == key:
                        ordered_items_total += int(requested_quantity)
                        same_item_total = float(
                            cost) * float(requested_quantity)
                        subtotal += same_item_total
                        print(
                            f"- {name}: {requested_quantity} | ${cost}")
            tax = subtotal * 0.06
            total = subtotal + tax
            print(f"\n-----------------")
            print(f"\nNumber of items: {ordered_items_total}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: ${total:.2f}")
            print(f"\nThank you for shopping at AMAZING STORE!")
            print(f"{current_date_and_time:%d/%m/%Y %H:%M:%S}")

    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print("Please enter a valid ID.")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            # This will use the column that will be used as key
            key = row_list[key_column_index]
            price = row_list[2]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


if __name__ == "__main__":
    main()
