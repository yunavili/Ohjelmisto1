import math

print("This program calculates the area of a circle with a given radius by using the formula A = πr².")
radius = input("Enter the radius of the circle: ")

try:
    radius = float(radius)
    if radius < 0:
        raise ValueError
except ValueError:
    print("Please enter a valid radius with a positive numeric value.")
else:
    area = math.pi * radius **2
    print(f"The area of the circle with radius {radius} is {area}.")



