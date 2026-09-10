print("This program tells which season a month belongs to based on its number.")

seasons = ("winter", "spring", "summer", "autumn")

while True:
    user_input = input("Enter month number or press Enter to quit: ").strip()
    
    if user_input == "":
        print("Goodbye.")
        break

    try:
        month = int(user_input)

        if month == 12 or month == 1 or month == 2:
            season = seasons[0]
        elif 3 <= month <= 5:
            season = seasons[1]
        elif 6 <= month <= 8:
            season = seasons[2]
        elif 9 <= month <= 11:
            season = seasons[3] 
        else:
            season = None

        if season:
            print(f"Season is {season}")
        else:
            print("Invalid month number! Please enter a number between 1 and 12.")

    except ValueError:
        print("Please enter a valid whole number.")