num1 = input("Enter a day of the year (1-365): ")
num2 = 365
result = num2 - int(num1)
if 1 <=int(num1) <= 365:
    print(f"Days before the end of the year: {result}")
else:
    print("Invalid input. Please enter a number between 1 and 365.")
