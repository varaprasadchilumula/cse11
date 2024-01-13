"""
The size of a car tire in the United States is represented with 
three numbers like this: 205/60R15. The first number is the width 
of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the 
tire fits. The volume of space inside a tire can be approximated with this formula:

Where:
    v is the volume in liters,
    π is the constant PI, which is the ratio of the circumference of a 
        circle divided by its diameter (use math.pi),
    w is the width of the tire in millimeters,
    a is the aspect ratio of the tire, and
    d is the diameter of the wheel in inches.

"""
import math

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

total = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

print(f"\nThe approximante volume is: {total: .2f} liters")