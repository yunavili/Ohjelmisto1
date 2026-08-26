print("This program checks if the Olympics were held in a given year.")

user_input = input("Enter a year: ")

try:
    asked_year = int(user_input)

    if asked_year < 1896 or asked_year > 2016:
        print("Invalid year. Please enter a year between 1896 and 2016.")
    elif asked_year %4 == 0 and asked_year != 2020:
        print(f"The Olympics were held in {asked_year}.")
    else:
        print(f"The Olympics were not held in {asked_year}.")

except ValueError:
    print("Invalid input. Please enter a valid numeric year.")