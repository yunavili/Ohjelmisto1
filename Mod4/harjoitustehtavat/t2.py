print("1, 2, 3, start!")
print("Tämä ohljelma kysyy käyttäjältä laivan hyttiluokan ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti")

print("Laivan hyttiluokat ovat LUX, A, B, C")
hyttiluokka = str(input("Laittaa laivan hyttiluokan: ")).strip()

if hyttiluokka == "LUX":
    print("LUX on parvekkeelinen hytti yläkannella")
elif hyttiluokka == "A":
    print("A on ikkunnallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella")    
else:
    print("Virheellinen hyttiluokka")

