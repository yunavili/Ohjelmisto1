import random

print("Tämä ohjelma simuloi autokilpailua.")

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self):
        muutos = random.randint(-10, 16)
        if self.tamanhetkinen_nopeus + muutos < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        else:
            self.tamanhetkinen_nopeus += muutos
    
    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.tamanhetkinen_nopeus

    def toString(self):
        return f"{self.rekisteritunnus}"
            

class Kilpailu:
    def __init__(self, nimi, pituus: int, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta()
            auto.kulje(1)

    
    def tulosta_tilanne(self):
        print(f"\nKiplailu {self.nimi}")   
        print(f"\n{'Rekisteritunnus':<16} | {'Huippunopeus':<16} | {'Nykynopeus':<16} | {'Kuljettu matka'}")
        print("-" * 72)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<16} | "
                f"{auto.huippunopeus :<11} km/h | "
                f"{auto.tamanhetkinen_nopeus:<11} km/h | "
            f"{auto.kuljettu_matka} km" 
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False #early return


autos = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
kilp = Kilpailu("The Great Scrap Rally", 8000, autos)


tunnit = 0

while not kilp.kilpailu_ohi():
    kilp.tunti_kuluu()
    tunnit += 1

if tunnit % 10 == 0:
    kilp.tulosta_tilanne()

print("\nKilpailu on päättynyt!")
kilp.tulosta_tilanne()



