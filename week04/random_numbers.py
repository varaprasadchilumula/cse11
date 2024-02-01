import random


def main():
    numbers = [16.2, 75.1, 52.3]
    for number in numbers:
        print(number)
    append_random_numbers(numbers, 16)

    print("\nNew List\n")
    for number in numbers:
        print(number)


def append_random_numbers(numbers_list, quantity=1):
    """This function will create random numbers and
    append those numbers to the end of a list.
    """
    for _ in range(quantity):
        number = random.uniform(1, 120)
        number = round(number, 1)
        numbers_list.append(number)


if __name__ == "__main__":
    main()
