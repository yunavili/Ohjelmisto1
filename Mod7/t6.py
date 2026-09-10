import math

def pizzaPrice (diameter, price):
    radius = diameter/2
    area2 = math.pi * (radius ** 2)
    unitPrice = price/area2
    return unitPrice



diameter1 = float(input("Enter 1st pizza's diameter in centimeters: "))
price1 = float(input("Enter 1st pizza's price in euros: "))

diameter2 = float(input("Enter 2nd pizza's diameter in centimeters: "))
price2 = float(input("Enter 2nd pizza's price in euros: "))

print(f"\nUnit price of the first pizza is {pizzaPrice(diameter1, price1):.2f}€/cm²")
print(f"Unit price of the second pizza is {pizzaPrice(diameter2, price2):.2f}€/cm²")


