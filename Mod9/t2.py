print("Tämä ohjelma simuloi auton kiihtyvyyttä ja hidastuvuutta kilometerin tuntiin.")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        if self.tamanhetkinen_nopeus + muutos < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos

auto1 = Auto("ABC-123", 200)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus}km/h")
auto1.kiihdyta(-200)
print(f"Auton nopeus nyt: {auto1.tamanhetkinen_nopeus}km/h")