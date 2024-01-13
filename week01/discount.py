# get datetime function from datetime library
from datetime import datetime

today = datetime.now()


# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = today.weekday()

# Print the day of the week for the user to see.
# 0 is for Mondays an so on
print(day_of_week)

# next line is to test the different cases
# day_of_week = 2

subtotal = float(input("Please enter the subtotal: "))
tax_rate = 0.06
disccount_rate = 0.10

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    disccount = subtotal * disccount_rate
    subtotal -= disccount
    print(f"Disccount amount: {disccount:.2f}")

tax = subtotal * tax_rate
print(f"Sales tax amount: {tax:.2f}")

total = subtotal + tax
print(f"Total: {total:.2f}")