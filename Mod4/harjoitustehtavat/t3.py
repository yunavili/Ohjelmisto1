import sys

print("\nThis program characterizes your hemoglobin level in relation to your gender")
print("""Genders:
1. Female
2. Male
3. Other""")
gender = str(input("Enter here a numerical value regarding to your gender choise 1-3: ")).strip()

if gender not in ["1", "2", "3"]:
    print("Invalid choice. Please select 1, 2, or 3.")
    sys.exit()

try:
    hemoglobin = int(input("What's your hemoglobin level?: "))
except ValueError:
    print("Invalid hemoglobin value. Please enter a number.")
    sys.exit()

if gender == "1":
    if hemoglobin < 117:
        print("Your hemoglobin level is lower than normal")
    elif hemoglobin >= 117 and hemoglobin <= 175:
        print("Your hemoglobin level is in normal state")
    else:
        print("Your hemoglobin is above normal levels")

elif gender == "2":
    if hemoglobin < 134:
        print("Your hemoglobin level is lower than normal")
    elif hemoglobin >= 134 and hemoglobin <= 195:
        print("Your hemoglobin level is in normal state")
    else:
        print("Your hemoglobin is above normal levels")

elif gender == "3":
    print("Sorry idunno :( ")

else: 
    print("Invalid choice. Please select 1, 2, or 3.")