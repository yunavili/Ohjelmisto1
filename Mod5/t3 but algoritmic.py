import sys

print("This program asks numbers until the user enters an empty string as the terminator")

u_list = []
try:
    add = str(input("Enter the number: "))
    while add != "":
        u_list.append(add)
        print(u_list)
        add = str(input("Enter the number: "))
    #print(min(u_list)) 
    #print(max(u_list))

except ValueError:
    print("Please enter a numeric value.")
    sys.exit()