print("Tämä ohjelma simuloi auton kiihtyvyyttä ja hidastuvuutta kilometerin tuntiin.")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto1 = Auto("ABC-123", 142)

print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus}km/h, huippunopeus: {auto1.huippunopeus}km/h, rekisteritunnus: {auto1.rekisteritunnus}, kuljettu matka: {auto1.kuljettu_matka}km")
# Should print 150 km/h