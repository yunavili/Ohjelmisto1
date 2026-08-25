print("This program calculates sum, product, and average of the numbers.")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
except ValueError:
    print("Please enter valid numeric values.")
else:
    sumnum = num1 + num2 + num3
    product = num1 * num2 * num3
    average = sumnum / 3
    print(f"sum of the numbers is: {round(sumnum, 2)}.")
    print(f"product of the numbers is: {round(product, 2)}.")
    print(f"average of the numbers is: {round(average, 2)}.")

