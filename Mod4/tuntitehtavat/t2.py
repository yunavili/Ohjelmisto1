print("This program checks which amusement park rides a person can go on.")

try:
    user_height = int(input("Enter your height in centimeters: "))
    user_age = int(input("Enter your age in years: "))

    if user_age < 8 or user_height < 100:
        print("You can't go to any of rides.")
    elif user_height < 140:
        print("You can go to children's rides including Kirnu but except Tuliretki.")
    elif user_height < 195:
        print("You can go to all rides.")
    else: 
        print("You can go to any of rides including Tuliretki but except Kirnu.")
    
except ValueError:
    print("Please enter valid numbers for height and age.")