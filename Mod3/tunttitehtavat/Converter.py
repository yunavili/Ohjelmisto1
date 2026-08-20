weight = float(input("Enter your weight in grams: "))
weight_kg = int(weight // 1000)
weight_gr = weight % 1000
print(f"Your weight in kilograms and grams is {weight_kg} kg and {weight_gr} g")
