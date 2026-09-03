import sys

print("This program asks numbers until the user enters an empty string as the terminator")

u_list = []

while True:
    value = input("Enter the number: ")
    if value == "":
        print(min(u_list))
        print(max(u_list))
        break
            
    else:
        try:
            value = int(value)
            u_list.append(value)
            print(u_list)
        except ValueError:
            print("Please enter a numeric value.")
            sys.exit()
   