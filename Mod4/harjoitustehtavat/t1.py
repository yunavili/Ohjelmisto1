print()
kuhan_pituus = float(input("Anna Kuhan pituus senttimetreinä: "))
aikuinenkuha = 37

if kuhan_pituus < 37:
 print("Laske Kuha takaisin järveen!")
 lisää_senttiä = aikuinenkuha - kuhan_pituus
 print(f"Kuhasta puuttuu {lisää_senttiä:.2f} senttimetriä")
else:
    print("Voit pitää tämän pituisia kuhia")