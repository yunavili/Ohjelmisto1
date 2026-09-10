airports = {
    "EFHK": "Helsinki-Vantaa Airport (Finland)",
    "EETN": "Lennart Meri Tallinn Airport (Estonia)",
    "WAW": "Warsaw Chopin Airport (Poland)",
    "LFPG": "Paris Charles de Gaulle Airport (France)",
    "EGLL":"London Heathrow Airport (UK)"
}

while True:
    print("\n Airport Database ")
    print("1. Enter a new airport")
    print("2. Search for an airport")
    print("3. Quit")

    choise = input("Select an option(1-3): ").strip()
    if choise == "1":
        icao = input("Enter new ICAO code: ").strip().upper()
        name = input("Enter airport name: ").strip()
        
        airports[icao] = name
        print(f"Airport {name} with code {icao} saved into directory.")
    
    elif choise == "2":
        icao = input("Enter ICAO code to search: ").strip().upper()

        if icao in airports:
            print(f"Airport name is {airports[icao]}")
        else:
            print("Airport is not found.")

    elif choise == "3":
        print("Goodbye.")
        break
    
    else:
        print("Invalid choice, please select 1, 2, or 3.")