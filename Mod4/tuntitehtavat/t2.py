print("This program checks which amusement park rides a person can go on.")

try:
    user_height = int(input("Enter your height in centimeters: "))
    user_age = int(input("Enter your age in years: "))

    if user_height >= 100 and user_age >= 8:
        
        if user_height >= 100 and user_height < 140:
            print("You can go to children's rides.")
        elif user_height >= 140 and user_height <= 195:
            print("You can go to all rides.")
        else: 
            print("You can go to all children's rides except Tuliretki.")
    
    elif user_height < 140 and user_age < 8:
                print("You can go to all children's rides except Tuliretki.")
    
    else: 
        print("You can't go to any of rides")
    
except ValueError:
    print("Please enter a valid height in centimeters.")
