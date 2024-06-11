#My creativity touch is evident in the input validation loops, which act as guardians to ensure only realistic data enters the calculations. By setting minimum values for tire width, aspect ratio, and diameter, I ensure the accuracy of the program's functionality.
import math  # Importing the math module for mathematical operations
from datetime import datetime

print()  # Print an empty line for better readability

# Get the current date and time
current_date_and_time = datetime.now()

# Extract only the date part (YYYY-MM-DD) from the current date and time
current_date = current_date_and_time.strftime("%Y-%m-%d")

# Getting user inputs for tire specifications
while True:
    width = float(input("Enter the width of the tire in mm (ex: 205, 215, 225): "))  # User input for tire width in millimeters
    if width >= 100:
        width = width
        break
    else:
        print("Error: width must be a positive number and should not be less than 100. ")

while True:
    aspect = float(input("Enter the aspect ratio of the tire (ex: 60, 65, 70): "))  # User input for aspect ratio
    if aspect >= 30:
        aspect = aspect
        break
    else:
        print("Error: Aspect ratio must be positive number and should not be less than 30. ")

while True:        
    diameter = float(input("Enter the diameter of the wheel in inch (ex: 15, 16, 17): "))  # User input for wheel diameter in inches
    if diameter >= 11:
        diameter = diameter
        break
    else:
        print("Error: Diameter must be positive number and should not be less than 11. ")

# Calculating the first term of the formula
first = math.pi * width**2 * aspect  # Formula to calculate the first term (π * w^2 * a)

# Calculating the second term of the formula
second = width * aspect + 2540 * diameter  # Formula to calculate the second term (w * a + 2540 * d)

# Setting a constant value for the third term of the formula
# This constant value represents 10 billion for the third term
third = 10000000000  # Represents 10 billion

# Calculating the volume of the tire using the provided formula
volume = first * second / third  # Formula to calculate the volume of the tire (v = (first * second) / third)

print()  # Print an empty line for better readability

# Displaying the approximate volume of the tire in liters with two decimal places
print(f"The approximate volume is: {volume:.2f} liters")  # Output the approximate volume of the tire
print()

# Append the tire specifications and volume to the volumes.txt file
with open("volumes.txt", mode="a") as volumes_file:
    volumes_file.write(f"{current_date}, {int(width)}, {int(aspect)}, {int(diameter)}, {volume:.2f}\n")

print("Data has been written to volumes.txt successfully.")
print()
