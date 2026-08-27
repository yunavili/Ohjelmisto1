import sys

print("This code checks if the entered year is a leap year.")

try:
    input_year = int(input("Enter any year after the birth of Jesus Christ: "))
except ValueError:
    print("Invalid value. Please enter a number.")
    sys.exit()

if input_year <= 0:
    print("Invalid year. Please enter a valid number.")
    sys.exit()

if input_year % 4 == 0 and input_year % 400 == 0 and input_year % 100 == 0:
    print(f"{input_year} is a leap year, yeah!")
else: 
    print("It's not a leap year, nope.")