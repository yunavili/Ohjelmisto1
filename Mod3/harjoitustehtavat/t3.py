import math

print("This program calculates perimeter and area of the rectangle: ")
length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

try:
    length = float(length)
    width = float(width)
    if length < 0 or width < 0:
        raise ValueError
except ValueError:
    print("Please enter a valid length and width with positive numeric values.")
else:
    area = length * width
    perimeter = 2 * (length + width)
    print(f"The area of the rectangle with length {length} and width {width} is {area}.")
    print(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter}.")