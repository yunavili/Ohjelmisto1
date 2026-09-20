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
    
    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.tamanhetkinen_nopeus


auto1 = Auto("ABC-123", 200)
auto1.kiihdyta(60)
auto1.kuljettu_matka += 2000
auto1.kulje(1.5)
print(f"Auto  on kulkenut {auto1.kuljettu_matka}")