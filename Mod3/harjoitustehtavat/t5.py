
print("This program converts old Swedish weight units to modern units.")

try:
    lispunds = float(input("Enter lispunds: "))
    pounds = float(input("Enter pounds:  "))
    lots = float(input("Enter lots: "))
except ValueError:
    print("Please enter valid numeric values.") 
    exit()
else:
    total_lots = lots + (pounds * 32) + (lispunds * 20 * 32)
    total_grams = total_lots * 13.3

    kilograms = int(total_grams // 1000)
    grams = total_grams % 1000

    print("Weight in modern units:")
    print(f"{kilograms} kilograms and {grams:.2f} grams.")


