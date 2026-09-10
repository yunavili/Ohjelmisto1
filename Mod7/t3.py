print("This program converts volume from US gallons to liters.")

def gallonsToLiters(gallons):
    return gallons * 3.785


gallons = float(input("Enter the amount of gallons to convert them into liters: "))

print(f"{gallons} gallons is {gallonsToLiters(gallons)} liters")


