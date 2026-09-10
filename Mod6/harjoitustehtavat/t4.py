print("This program collects the names of 5 cities and prints them in order.")
#I'm a bit lazy for debugging this time
cities = []

for i in range(5):
    while True:
        city = input(f"Enter city name {i + 1}: ").strip().title()

        if city:
            cities.append(city)
            break
        else:
            print("City name cannot be empty, write something!")
print("\nCities in order:")

for city in cities:
    print(city)