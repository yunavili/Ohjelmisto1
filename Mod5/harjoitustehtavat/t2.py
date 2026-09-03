import sys

print("this program converts centimeters to inches repeatedly based on user input, using the formula 1 inch = 2.54 cm")
try:
    u_inp = float(input("Enter the number: "))
    while u_inp >= 0:
        print(f"{u_inp} cm = {u_inp * 2.54:.2f} inches")
        print("To close the propgram enter a negative number.")
        u_inp = float(input("Enter the number: "))
except ValueError:
    print("Please enter a numeric value.")
    sys.exit()