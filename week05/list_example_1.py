# Example 1

def main():
    # Read the contents of a text file named "plants.txt" into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and return the list.
    Each element in the list will contain one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list to store the lines of text from the file.
    text_list = []

    # Open the text file for reading using a with statement.
    with open(filename, "rt") as text_file:
        # Read each line from the text file and strip whitespace.
        for line in text_file:
            clean_line = line.strip()
            # Append the cleaned line to the list.
            text_list.append(clean_line)

    # Return the list containing the lines of text.
    return text_list


# Call the main function to start the program.
if __name__ == "__main__":
    main()
